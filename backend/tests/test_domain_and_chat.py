"""
Unit and Integration Tests for Coimbatore and Tamil Nadu Travel Guide Bot
Verifies:
1. Strict Domain Restrictions (Allowed vs Out-of-scope topics)
2. All 38 Districts of Tamil Nadu Recognition
3. Prompt Example Questions (Coimbatore, Ariyalur, Mayiladuthurai, Virudhunagar, Chennai-Kanyakumari, etc.)
4. Full Multi-Turn Conversation Flow:
   - Turn 1: "What are the best tourist places in Coimbatore?"
   - Turn 2: "Tell me more about the first place."
   - Turn 3: "Plan a two-day trip within ₹3,000."
   - Turn 4: "Make it cheaper and add nature places."
5. Destination comparison: "Which is better: Ooty or Kodaikanal?"
6. Out-of-state and General Knowledge Redirection
7. Language detection (English, Tamil, Tanglish)
8. Deterministic budget calculations
"""

import pytest
import sys
import os
import asyncio

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.domain_guardrail import check_domain_scope, OUT_OF_SCOPE_RESPONSE, ALL_38_DISTRICTS
from app.language_detector import detect_language
from app.budget_calculator import calculate_trip_budget
from app.itinerary_engine import generate_structured_itinerary
from app.knowledge_base import get_destination_data, list_all_destinations
from app.llm_client import TravelAssistant

# ==========================================
# 1. 38 DISTRICTS & SAMPLE QUESTIONS
# ==========================================

def test_all_38_districts_recognized():
    assert len(ALL_38_DISTRICTS) >= 38
    for dist in ALL_38_DISTRICTS:
        query = f"What are the top attractions to visit in {dist}?"
        is_in_scope, redirect_msg = check_domain_scope(query)
        assert is_in_scope is True, f"Failed recognizing district {dist}"
        assert redirect_msg is None

def test_prompt_specific_example_questions():
    examples = [
        "What are the best tourist places in Coimbatore?",
        "Tell me about tourist attractions in Ariyalur.",
        "What can I explore in Mayiladuthurai?",
        "Suggest hidden gems in Virudhunagar.",
        "Plan a three-day trip to Ooty.",
        "What traditional food should I try in Madurai?",
        "How can I travel from Chennai to Kanyakumari?",
        "Plan a two-day trip within ₹3,000.",
        "Tell me more about the first place.",
        "Make it cheaper and add nature places.",
        "Which is better: Ooty or Kodaikanal?",
        "Coimbatore la two days trip plan pannunga."
    ]
    for ex in examples:
        is_in_scope, redirect_msg = check_domain_scope(ex)
        assert is_in_scope is True, f"Query '{ex}' was incorrectly rejected."
        assert redirect_msg is None

def test_strictly_unrelated_out_of_scope_queries():
    unrelated_samples = [
        "Write a Python script for binary search.",
        "What stocks should I buy in Nifty tomorrow for trading?",
        "I have high fever and severe headache, diagnose what medicine I should take.",
        "Who should I vote for in the upcoming election?",
        "Solve this quadratic equation: 3x^2 + 5x - 8 = 0.",
        "Can you write an essay on quantum mechanics?",
        "What is the capital of France?",
        "Who is Elon Musk?"
    ]
    for query in unrelated_samples:
        is_in_scope, redirect_msg = check_domain_scope(query)
        assert is_in_scope is False, f"Did not reject out-of-scope query: '{query}'"
        assert redirect_msg == OUT_OF_SCOPE_RESPONSE
        assert "Coimbatore and Tamil Nadu Travel Guide Bot" in redirect_msg

def test_out_of_state_geographic_redirection():
    query = "Plan a 3-day luxury beach vacation in Goa."
    is_in_scope, redirect_msg = check_domain_scope(query)
    assert is_in_scope is False
    assert redirect_msg == OUT_OF_SCOPE_RESPONSE
    assert "Tamil Nadu" in redirect_msg

def test_transit_query_involving_outside_location_is_allowed():
    query = "How to travel from Mumbai to Chennai by train?"
    is_in_scope, _ = check_domain_scope(query)
    assert is_in_scope is True

# ==========================================
# 2. DYNAMIC CONVERSATION & CHATBOT REASONING
# ==========================================

def test_user_chatgpt_example_flow():
    """
    Tests the exact sequence requested by the user:
    1. 'What are the best tourist places in Coimbatore?'
    2. 'Tell me more about the first place.'
    3. 'Plan a two-day trip within ₹3,000.'
    4. 'Make it cheaper and add nature places.'
    """
    async def run_flow():
        assistant = TravelAssistant()
        history = []

        # Turn 1: Best tourist places in Coimbatore
        t1 = "What are the best tourist places in Coimbatore?"
        res1 = await assistant.process_chat(t1, history)
        assert res1["is_out_of_scope"] is False
        assert "Adiyogi" in res1["response"]
        assert "Marudhamalai" in res1["response"]
        history.append({"role": "user", "content": t1})
        history.append({"role": "assistant", "content": res1["response"]})

        # Turn 2: Follow-up on first place
        t2 = "Tell me more about the first place."
        res2 = await assistant.process_chat(t2, history)
        assert res2["is_out_of_scope"] is False
        assert ("Adiyogi" in res2["response"] or "Isha" in res2["response"])
        assert "112" in res2["response"]
        history.append({"role": "user", "content": t2})
        history.append({"role": "assistant", "content": res2["response"]})

        # Turn 3: Plan two-day trip within ₹3,000
        t3 = "Plan a two-day trip within ₹3,000."
        res3 = await assistant.process_chat(t3, history)
        assert res3["is_out_of_scope"] is False
        assert ("Day 1" in res3["response"] or "Day 2" in res3["response"])
        assert "3,000" in res3["response"] or "Coimbatore" in res3["response"]
        history.append({"role": "user", "content": t3})
        history.append({"role": "assistant", "content": res3["response"]})

        # Turn 4: Make it cheaper and add nature places
        t4 = "Make it cheaper and add nature places."
        res4 = await assistant.process_chat(t4, history)
        assert res4["is_out_of_scope"] is False
        assert ("nature" in res4["response"].lower() or "kutralam" in res4["response"].lower() or "siruvani" in res4["response"].lower())

    asyncio.run(run_flow())

def test_ooty_vs_kodaikanal_comparison():
    async def run_comp():
        assistant = TravelAssistant()
        res = await assistant.process_chat("Which is better: Ooty or Kodaikanal?", [])
        assert res["is_out_of_scope"] is False
        assert "Ooty" in res["response"]
        assert "Kodaikanal" in res["response"]

    asyncio.run(run_comp())

# ==========================================
# 3. LANGUAGE DETECTION & BUDGET CALCULATION
# ==========================================

def test_language_detection():
    assert detect_language("What are the top attractions in Ooty?") == "english"
    assert detect_language("கோவையில் பார்க்க வேண்டிய இடங்கள் என்னென்ன?") == "tamil"
    assert detect_language("Coimbatore la two days trip plan pannunga") == "tanglish"
    assert detect_language("Ooty ku eppo pona nalla irukkum?") == "tanglish"

def test_budget_calculator_arithmetic():
    budget = calculate_trip_budget(
        destination="Coimbatore",
        days=2,
        travellers=1,
        travel_style="budget",
        total_budget_limit=3000
    )
    assert budget["destination"] == "Coimbatore"
    assert budget["days"] == 2
    assert budget["travellers"] == 1
    assert budget["total_estimated"] > 0
    assert budget["total_estimated"] <= 3000
    assert budget["is_within_budget"] is True

def test_knowledge_base_38_districts_catalog():
    catalog = list_all_destinations()
    assert len(catalog) == 38
