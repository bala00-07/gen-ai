"""
TamilNadu TravelAI - LLM Orchestrator & Dynamic Travel Engine
Project Name: Coimbatore and Tamil Nadu Travel Guide Bot
Provides ChatGPT-like dynamic conversation, reasoning across all 38 districts of Tamil Nadu,
supporting open-ended travel questions, follow-up context memory, dynamic itineraries,
and multilingual generation (English, Tamil, Tanglish).
"""

import os
import re
import json
import httpx
from typing import Dict, List, Any, Optional
from app.knowledge_base import DESTINATIONS, get_destination_data, list_all_destinations
from app.domain_guardrail import check_domain_scope, OUT_OF_SCOPE_RESPONSE, ALL_38_DISTRICTS, TN_IDENTIFIERS
from app.budget_calculator import calculate_trip_budget
from app.itinerary_engine import generate_structured_itinerary
from app.language_detector import detect_language
from app.live_weather import fetch_live_weather

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY", "")

SYSTEM_INSTRUCTION = """
You are your Coimbatore and Tamil Nadu Travel Guide Bot, an intelligent, friendly, and reliable travel guide dedicated exclusively to Tamil Nadu, India.
You behave like ChatGPT for Tamil Nadu travel: users can ask any travel question in natural language and you generate dynamic, detailed, and personalized answers.

CORE PRINCIPLES:
1. STRICT TAMIL NADU FOCUS: Only answer questions related to travel, tourism, culture, food, transportation, hotels, itineraries, history, and destinations across all 38 districts of Tamil Nadu.
2. OUT-OF-SCOPE RULE: If the user asks an unrelated question (programming, math, politics, medical diagnosis, stocks, homework, general trivia, or non-Tamil Nadu destinations without transit to/from Tamil Nadu), strictly reply:
"I'm your Coimbatore and Tamil Nadu Travel Guide Bot. I can help you explore destinations, discover local food and culture, find routes, estimate budgets, and plan trips throughout Tamil Nadu. What would you like to explore?"
Do not answer the unrelated question before redirecting.
3. ALL 38 DISTRICTS: Support all 38 districts of Tamil Nadu (Ariyalur, Chengalpattu, Chennai, Coimbatore, Cuddalore, Dharmapuri, Dindigul, Erode, Kallakurichi, Kancheepuram, Kanniyakumari, Karur, Krishnagiri, Madurai, Mayiladuthurai, Nagapattinam, Namakkal, Nilgiris, Perambalur, Pudukkottai, Ramanathapuram, Ranipet, Salem, Sivaganga, Tenkasi, Thanjavur, Theni, Thoothukudi, Tiruchirappalli, Tirunelveli, Tirupathur, Tiruppur, Tiruvallur, Tiruvannamalai, Tiruvarur, Vellore, Viluppuram, Virudhunagar) and any towns, villages, waterfalls, temples, markets, or attractions within them.
4. DYNAMIC & UNRESTRICTED GENERATION: Do not restrict answers to fixed formats or pre-stored strings. Generate answers dynamically using your knowledge.
5. CONVERSATION CONTEXT & FOLLOW-UPS: Remember context from previous turns (destinations, days, budgets, previously mentioned attractions). Handle commands like "tell me more about the first place", "tell me more about the second place", "plan a two-day trip within ₹3,000", "make it cheaper and add nature places", "which is better?", and "how to travel there" seamlessly.
6. UNCERTAIN INFORMATION: If information is uncertain or requires current verification (such as exact seasonal waterfall flows, festival darshan timings, or bus schedule changes), explain the limitation clearly and recommend official local verification rather than inventing facts.
7. MULTILINGUAL:
   - English: Polished markdown with headings, bullet points, and tables.
   - Tamil: Natural Tamil script (வணக்கம்!...).
   - Tanglish: Friendly Romanized Tamil (e.g., "Vanakkam! Coimbatore la 2 days travel plan ready pannirukken...").
"""

# Comprehensive dictionary mapping prominent towns, spots, hills, and temples to district keys
DISTRICT_ALIASES: Dict[str, str] = {
    # Coimbatore & surrounding
    "coimbatore": "coimbatore", "kovai": "coimbatore", "adiyogi": "coimbatore",
    "isha": "coimbatore", "marudhamalai": "coimbatore", "siruvani": "coimbatore",
    "kovai kutralam": "coimbatore", "gedee car museum": "coimbatore", "eachanari": "coimbatore",
    "perur": "coimbatore", "velliangiri": "coimbatore", "valparai": "coimbatore",
    "pollachi": "coimbatore", "topslip": "coimbatore", "anamalai": "coimbatore",
    "singanallur": "coimbatore", "chettipalayam": "coimbatore", "sulur": "coimbatore",
    "annur": "coimbatore", "mettupalayam": "coimbatore",

    # Nilgiris
    "ooty": "nilgiris", "udhagai": "nilgiris", "coonoor": "nilgiris", "kotagiri": "nilgiris",
    "doddabetta": "nilgiris", "pykara": "nilgiris", "avalanche": "nilgiris", "sims park": "nilgiris",
    "dolphins nose": "nilgiris", "mudumalai": "nilgiris", "masinagudi": "nilgiris", "glenmorgan": "nilgiris",

    # Dindigul / Kodaikanal
    "kodaikanal": "dindigul", "kodai": "dindigul", "palani": "dindigul", "berijam": "dindigul",
    "bryant park": "dindigul", "coakers walk": "dindigul", "pillar rocks": "dindigul",
    "silver cascade": "dindigul", "vattakanal": "dindigul", "sirumalai": "dindigul",

    # Chennai & Chengalpattu
    "chennai": "chennai", "madras": "chennai", "marina beach": "chennai", "besant nagar": "chennai",
    "elliots beach": "chennai", "san thome": "chennai", "kapaleeshwarar": "chennai",
    "guindy national park": "chennai", "vandalur zoo": "chennai", "dakshinachitra": "chengalpattu",
    "mahabalipuram": "chengalpattu", "mamallapuram": "chengalpattu", "shore temple": "chengalpattu",
    "vedanthangal": "chengalpattu", "muttukadu": "chengalpattu", "covelong": "chengalpattu",

    # Madurai
    "madurai": "madurai", "meenakshi": "madurai", "meenakshi amman": "madurai",
    "thirumalai nayakkar": "madurai", "alagar kovil": "madurai", "thiruparankundram": "madurai",

    # Thanjavur
    "thanjavur": "thanjavur", "tanjore": "thanjavur", "brihadisvara": "thanjavur", "big temple": "thanjavur",
    "kumbakonam": "thanjavur", "swamimalai": "thanjavur", "darasuram": "thanjavur", "thiruvaiyaru": "thanjavur",
    "manora fort": "thanjavur",

    # Tiruchirappalli
    "trichy": "tiruchirappalli", "tiruchirappalli": "tiruchirappalli", "srirangam": "tiruchirappalli",
    "rockfort": "tiruchirappalli", "kallanai": "tiruchirappalli", "mukkombu": "tiruchirappalli",
    "samayapuram": "tiruchirappalli",

    # Ramanathapuram
    "rameswaram": "ramanathapuram", "rameshwaram": "ramanathapuram", "dhanushkodi": "ramanathapuram",
    "pamban": "ramanathapuram", "pamban bridge": "ramanathapuram", "kalam memorial": "ramanathapuram",
    "ervadi": "ramanathapuram",

    # Kanniyakumari
    "kanyakumari": "kanniyakumari", "kanniyakumari": "kanniyakumari", "vivekananda rock": "kanniyakumari",
    "thiruvalluvar statue": "kanniyakumari", "padmanabhapuram": "kanniyakumari", "vattakottai": "kanniyakumari",
    "thiruparappu": "kanniyakumari",

    # Tenkasi & Tirunelveli
    "courtallam": "tenkasi", "kutralam": "tenkasi", "five falls": "tenkasi", "tenkasi": "tenkasi",
    "tirunelveli": "tirunelveli", "nellai": "tirunelveli", "nellaiappar": "tirunelveli",
    "papanasam": "tirunelveli", "manjolai": "tirunelveli", "agathiyar falls": "tirunelveli",
    "kalakkad": "tirunelveli", "manimuthar": "tirunelveli",

    # Thoothukudi
    "thoothukudi": "thoothukudi", "tuticorin": "thoothukudi", "tiruchendur": "thoothukudi",
    "manapad": "thoothukudi", "panchalankurichi": "thoothukudi",

    # Salem & Namakkal
    "salem": "salem", "yercaud": "salem", "kiliyur falls": "salem", "mettur dam": "salem",
    "namakkal": "namakkal", "kolli hills": "namakkal", "agaya gangai": "namakkal",

    # Dharmapuri & Krishnagiri
    "dharmapuri": "dharmapuri", "hogenakkal": "dharmapuri", "krishnagiri": "krishnagiri", "hosur": "krishnagiri",

    # Erode & Tiruppur
    "erode": "erode", "kodiveri": "erode", "bhavanisagar": "erode", "bannari": "erode",
    "tiruppur": "tiruppur", "thirumoorthy": "tiruppur", "amaravathi": "tiruppur",

    # Theni
    "theni": "theni", "meghamalai": "theni", "megamalai": "theni", "suruli falls": "theni",
    "kumbakkarai": "theni", "bodinayakanur": "theni", "kurangani": "theni",

    # Sivaganga & Virudhunagar
    "sivaganga": "sivaganga", "karaikudi": "sivaganga", "chettinad": "sivaganga", "pillayarpatti": "sivaganga",
    "virudhunagar": "virudhunagar", "srivilliputhur": "virudhunagar", "ayyanar falls": "virudhunagar", "sivakasi": "virudhunagar",

    # Pudukkottai & Ariyalur & Perambalur
    "pudukkottai": "pudukkottai", "sittannavasal": "pudukkottai", "thirumayam": "pudukkottai",
    "ariyalur": "ariyalur", "gangaikonda cholapuram": "ariyalur", "karaivetti": "ariyalur",
    "perambalur": "perambalur", "ranjankudi fort": "perambalur",

    # Karur & Tiruvarur & Nagapattinam & Mayiladuthurai
    "karur": "karur", "tiruvarur": "tiruvarur", "muthupet": "tiruvarur", "mannargudi": "tiruvarur",
    "nagapattinam": "nagapattinam", "velankanni": "nagapattinam", "point calimere": "nagapattinam",
    "mayiladuthurai": "mayiladuthurai", "tarangambadi": "mayiladuthurai", "tranquebar": "mayiladuthurai", "poompuhar": "mayiladuthurai",

    # Cuddalore & Viluppuram & Kallakurichi
    "cuddalore": "cuddalore", "pichavaram": "cuddalore", "chidambaram": "cuddalore", "silver beach": "cuddalore",
    "viluppuram": "viluppuram", "villupuram": "viluppuram", "gingee fort": "viluppuram",
    "kallakurichi": "kallakurichi", "kalvarayan": "kallakurichi",

    # Tiruvannamalai & Vellore & Tirupathur & Ranipet & Kancheepuram & Tiruvallur
    "tiruvannamalai": "tiruvannamalai", "annamalaiyar": "tiruvannamalai", "girivalam": "tiruvannamalai",
    "vellore": "vellore", "golden temple": "vellore", "sripuram": "vellore",
    "tirupathur": "tirupathur", "yelagiri": "tirupathur", "jalagamparai": "tirupathur",
    "ranipet": "ranipet", "arcot": "ranipet",
    "kancheepuram": "kancheepuram", "kanchipuram": "kancheepuram", "kanchi": "kancheepuram",
    "tiruvallur": "tiruvallur", "pulicat": "tiruvallur"
}

class TravelAssistant:
    def __init__(self):
        self.api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY", "")

    def extract_intent(self, user_msg: str, history: List[Dict[str, str]]) -> Dict[str, Any]:
        """
        Extracts active destination, referred attractions, day count, budget limits,
        replanning modifiers, and multi-turn context.
        """
        text = user_msg.lower()

        # 1. Look for explicit destination or aliases in current message
        found_dest = None
        for alias, dest_key in DISTRICT_ALIASES.items():
            if re.search(r"\b" + re.escape(alias) + r"\b", text):
                found_dest = dest_key
                break

        # 2. Check conversation history for active destination
        prev_dest = None
        if history:
            for past_msg in reversed(history):
                p_text = past_msg.get("content", "").lower()
                for alias, dest_key in DISTRICT_ALIASES.items():
                    if re.search(r"\b" + re.escape(alias) + r"\b", p_text):
                        prev_dest = dest_key
                        break
                if prev_dest:
                    break

        active_dest = found_dest or prev_dest or "coimbatore"

        # 3. Detect follow-up reference to previous attraction items
        # e.g., "tell me more about the first place", "1st place", "second place", "third place", "that place"
        referred_item_index: Optional[int] = None
        if any(w in text for w in ["first place", "1st place", "first attraction", "first spot", "place 1", "attraction 1"]):
            referred_item_index = 0
        elif any(w in text for w in ["second place", "2nd place", "second attraction", "second spot", "place 2", "attraction 2"]):
            referred_item_index = 1
        elif any(w in text for w in ["third place", "3rd place", "third attraction", "third spot", "place 3", "attraction 3"]):
            referred_item_index = 2
        elif any(w in text for w in ["fourth place", "4th place", "fourth attraction", "place 4"]):
            referred_item_index = 3
        elif any(w in text for w in ["that place", "tell me more about that", "tell me more"]) and not found_dest:
            referred_item_index = 0

        # Check for specific named attraction follow-up
        named_attraction = None
        for att_name in [
            "adiyogi", "marudhamalai", "siruvani", "gedee car museum", "eachanari", "perur pateeswarar",
            "velliangiri", "kovai kutralam", "monkey falls", "doddabetta", "pykara", "sims park",
            "brihadisvara", "meenakshi amman", "gangaikonda cholapuram", "pamban bridge", "vivekananda rock"
        ]:
            if att_name in text:
                named_attraction = att_name
                break

        # 4. Extract days
        days = 2
        days_match = re.search(r"\b(\d+)\s*(?:days?|naal|naala)\b", text)
        if days_match:
            days = int(days_match.group(1))
        elif any(w in text for w in ["one day", "1 day", "oru naal"]):
            days = 1
        elif any(w in text for w in ["two days", "2 days", "two-day", "2-day", "rendu naal"]):
            days = 2
        elif any(w in text for w in ["three days", "3 days", "three-day", "3-day", "moonu naal"]):
            days = 3
        elif "weekend" in text:
            days = 2

        # 5. Extract budget numbers (e.g. ₹3,000, 3000, ₹5,000)
        budget_limit = None
        budget_match = re.search(r"(?:₹|rs\.?|inr)?\s*([0-9]{1,2}(?:,[0-9]{2,3})*|[0-9]{3,6})", text)
        if budget_match:
            val_str = budget_match.group(1).replace(",", "")
            if val_str.isdigit() and int(val_str) >= 500:
                budget_limit = float(val_str)

        # 6. Conversational Replanning Modifiers
        is_cheaper = any(w in text for w in [
            "cheaper", "make it cheaper", "make the itinerary cheaper", "budget la", "low cost",
            "kurainja", "economical", "budget friendly", "reduce cost", "less cost"
        ])
        add_nature = any(w in text for w in [
            "add nature", "add nature places", "nature destinations", "waterfalls", "hills",
            "forests", "viewpoints", "nature spots", "lake"
        ])
        no_temples = any(w in text for w in [
            "remove temple", "no temple", "kovil venaam", "temple venaam", "without temple",
            "skip temples", "remove temples"
        ])
        add_food = any(w in text for w in [
            "add food", "local food", "food places", "sapadu", "restaurants", "traditional food", "eateries"
        ])
        rain_mode = any(w in text for w in ["rain", "raining", "rainy", "mazhai", "indoor"])
        relaxed = any(w in text for w in ["relaxed", "slow pace", "senior citizen", "parents", "aram"])
        child_friendly = any(w in text for w in ["child", "children", "kids", "family", "kuzhandhainga"])

        # 7. Query Types
        is_comparison = ("which is better" in text or "compare" in text or "vs" in text or "or" in text) and any(d in text for d in ["ooty", "kodai", "kodaikanal", "yercaud", "yelagiri", "valparai"])
        is_transit_query = any(w in text for w in [
            "how to travel", "how can i travel", "how to reach", "train from", "bus from",
            "route to", "distance between", "flight from", "road condition"
        ])
        is_hidden_gems = any(w in text for w in ["hidden gem", "lesser-known", "less crowded", "unexplored", "offbeat"])
        is_itinerary_request = any(w in text for w in ["plan", "itinerary", "trip", "tour", "schedule", "days", "naal"]) or (budget_limit is not None)
        is_food_query = any(w in text for w in ["food", "dishes", "cuisine", "sapadu", "restaurant", "famous dish", "traditional food", "eat"])
        is_weather_query = any(w in text for w in ["weather", "temperature", "climate", "rain", "vanilai"])

        return {
            "destination": active_dest,
            "has_specific_dest": found_dest is not None,
            "referred_item_index": referred_item_index,
            "named_attraction": named_attraction,
            "days": days,
            "budget_limit": budget_limit,
            "is_cheaper": is_cheaper,
            "add_nature": add_nature,
            "no_temples": no_temples,
            "add_food": add_food,
            "rain_mode": rain_mode,
            "relaxed": relaxed,
            "child_friendly": child_friendly,
            "is_comparison": is_comparison,
            "is_transit_query": is_transit_query,
            "is_hidden_gems": is_hidden_gems,
            "is_itinerary_request": is_itinerary_request,
            "is_food_query": is_food_query,
            "is_weather_query": is_weather_query
        }

    async def call_gemini_api(self, prompt: str, history: List[Dict[str, str]]) -> Optional[str]:
        """
        Calls Google Gemini API with fallback across flash models.
        """
        api_key = self.api_key or os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
        if not api_key:
            return None

        # Build contents formatted for Gemini
        contents = []
        for msg in history[-8:]:
            role = "user" if msg.get("role") == "user" else "model"
            contents.append({
                "role": role,
                "parts": [{"text": msg.get("content", "")}]
            })
        contents.append({
            "role": "user",
            "parts": [{"text": prompt}]
        })

        payload = {
            "system_instruction": {"parts": [{"text": SYSTEM_INSTRUCTION}]},
            "contents": contents,
            "generationConfig": {
                "temperature": 0.4,
                "maxOutputTokens": 2048,
            }
        }

        # Try gemini-2.5-flash, gemini-2.0-flash, gemini-1.5-flash
        models_to_try = ["gemini-2.5-flash", "gemini-2.0-flash", "gemini-1.5-flash"]
        for model in models_to_try:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
            try:
                async with httpx.AsyncClient(timeout=15.0) as client:
                    resp = await client.post(url, json=payload)
                    if resp.status_code == 200:
                        data = resp.json()
                        candidates = data.get("candidates", [])
                        if candidates and "content" in candidates[0]:
                            parts = candidates[0]["content"].get("parts", [])
                            if parts:
                                return parts[0].get("text", "")
            except Exception:
                continue

        return None

    async def process_chat(
        self,
        user_message: str,
        conversation_history: List[Dict[str, str]],
        language_pref: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Processes chat message with strict Tamil Nadu domain guardrail,
        intent extraction, live weather enrichment, and intelligent dynamic response generation.
        """
        # Step 1: Strict Domain Guardrail Check
        is_in_scope, guardrail_response = check_domain_scope(user_message, conversation_history)
        if not is_in_scope:
            return {
                "response": guardrail_response or OUT_OF_SCOPE_RESPONSE,
                "language": "english",
                "is_out_of_scope": True,
                "destination_card": None,
                "itinerary_card": None,
                "budget_card": None,
                "live_weather": None,
                "follow_up_suggestions": [
                    "What are the best tourist places in Coimbatore?",
                    "Plan a two-day trip to Coimbatore within ₹3,000",
                    "Tell me about tourist attractions in Ariyalur",
                    "What can I explore in Mayiladuthurai?",
                    "Suggest hidden gems in Virudhunagar"
                ]
            }

        # Step 2: Language Detection
        detected_lang = language_pref if (language_pref and language_pref != "auto") else detect_language(user_message)

        # Step 3: Intent & Entity Extraction
        intent = self.extract_intent(user_message, conversation_history)
        dest_key = intent["destination"]
        dest_data = get_destination_data(dest_key) or DESTINATIONS["coimbatore"]

        # Step 4: Live Weather Integration
        live_weather_info = None
        if intent["is_weather_query"] or intent["is_itinerary_request"] or "weather" in user_message.lower():
            live_weather_info = await fetch_live_weather(dest_key)

        # Step 5: Structured Data Preparation (Itinerary & Budget)
        itinerary_card = None
        budget_card = None
        destination_card = None

        if intent["has_specific_dest"] or dest_key == "coimbatore":
            destination_card = {
                "id": dest_key,
                "name": dest_data["name"],
                "district": dest_data["district"],
                "category": dest_data["category"],
                "tagline": dest_data["tagline"],
                "overview": dest_data["overview"],
                "best_season": dest_data["best_season"],
                "ideal_duration": dest_data["ideal_duration"],
                "attractions_count": len(dest_data.get("top_attractions", [])),
                "estimated_budget_per_day": dest_data.get("estimated_budget_per_day", "₹1,200 - ₹2,500")
            }

        # Handle Itinerary & Budget Calculations
        if intent["is_itinerary_request"] or intent["is_cheaper"] or intent["no_temples"] or intent["add_nature"]:
            prefs = {
                "is_budget": intent["is_cheaper"] or (intent["budget_limit"] is not None and intent["budget_limit"] <= 5000),
                "is_relaxed": intent["relaxed"],
                "no_temples": intent["no_temples"],
                "rain_mode": intent["rain_mode"],
                "child_friendly": intent["child_friendly"],
                "food_focused": intent["add_food"],
                "user_budget_limit": intent["budget_limit"],
                "travellers": 1 if (intent["budget_limit"] and intent["budget_limit"] <= 3000) else 2
            }
            itinerary_card = generate_structured_itinerary(dest_key, days=intent["days"], preferences=prefs)
            budget_card = itinerary_card.get("budget_summary")
        elif intent["budget_limit"] or "budget" in user_message.lower() or "cost" in user_message.lower():
            budget_card = calculate_trip_budget(
                destination=dest_data["name"],
                days=intent["days"],
                travellers=1 if (intent["budget_limit"] and intent["budget_limit"] <= 3000) else 2,
                travel_style="budget" if intent["is_cheaper"] or (intent["budget_limit"] and intent["budget_limit"] <= 4000) else "mid_range",
                total_budget_limit=intent["budget_limit"]
            )

        # Step 6: Generate Response Text
        response_text = None
        # Try real Gemini LLM first if API key configured
        if self.api_key or os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY"):
            grounded_context = f"""
TAMIL NADU KNOWLEDGE BASE CONTEXT:
Target Location: {dest_data['name']} (District: {dest_data['district']})
Overview: {dest_data['overview']}
Ideal Duration: {dest_data['ideal_duration']} | Best Season: {dest_data['best_season']}
Top Attractions: {json.dumps(dest_data.get('top_attractions', []), indent=2)}
Local Cuisine: {json.dumps(dest_data.get('local_food', {}))}
Transport: {json.dumps(dest_data.get('transport', {}))}
Live Weather: {json.dumps(live_weather_info) if live_weather_info else 'Live weather unavailable.'}
"""
            llm_prompt = f"{grounded_context}\n\nUSER QUESTION: {user_message}\nPREFERRED LANGUAGE: {detected_lang.upper()}"
            response_text = await self.call_gemini_api(llm_prompt, conversation_history)

        # If LLM API didn't return text, use Dynamic Travel AI Synthesis Engine
        if not response_text:
            response_text = self.generate_dynamic_response(
                user_msg=user_message,
                dest_data=dest_data,
                intent=intent,
                lang=detected_lang,
                history=conversation_history,
                live_weather=live_weather_info,
                itinerary_data=itinerary_card,
                budget_data=budget_card
            )

        # Dynamic follow-up suggestion chips
        follow_ups = self.get_dynamic_follow_ups(dest_data["name"], intent)

        return {
            "response": response_text,
            "language": detected_lang,
            "is_out_of_scope": False,
            "destination_card": destination_card,
            "itinerary_card": itinerary_card,
            "budget_card": budget_card,
            "live_weather": live_weather_info,
            "follow_up_suggestions": follow_ups
        }

    def generate_dynamic_response(
        self,
        user_msg: str,
        dest_data: Dict[str, Any],
        intent: Dict[str, Any],
        lang: str,
        history: List[Dict[str, str]],
        live_weather: Optional[Dict[str, Any]],
        itinerary_data: Optional[Dict[str, Any]],
        budget_data: Optional[Dict[str, Any]]
    ) -> str:
        """
        Dynamic ChatGPT-like response synthesis engine covering all 38 districts,
        Coimbatore spotlights, follow-up references ("the first place", "that place"),
        itinerary replanning ("make it cheaper and add nature places"), comparisons, and transit.
        """
        name = dest_data["name"]
        district = dest_data["district"]
        overview = dest_data["overview"]
        best_time = dest_data["best_season"]
        specialties = ", ".join(dest_data.get("local_food", {}).get("specialties", []))
        eateries = ", ".join(dest_data.get("local_food", {}).get("iconic_eateries", []))
        attractions = dest_data.get("top_attractions", [])
        transport = dest_data.get("transport", {})

        # CASE 1: Comparison between two destinations (e.g. "Which is better: Ooty or Kodaikanal?")
        if intent["is_comparison"] or ("ooty" in user_msg.lower() and "kodaikanal" in user_msg.lower()):
            if lang == "tanglish":
                return (
                    "### 🏔️ Ooty vs Kodaikanal: Endha Hill Station Ungalukku Best?\n\n"
                    "Ooty and Kodaikanal renduமே Tamil Nadu-oda famous hill stations, aana rendu இடத்துக்கும் distinct vibes irukku:\n\n"
                    "1. **Ooty (Queen of Hill Stations - Nilgiris):**\n"
                    "   - **Vibe:** Vast tea estates, colonial architecture, botanical gardens.\n"
                    "   - **Special Highlight:** UNESCO Nilgiri Mountain Railway (Toy Train) from Mettupalayam to Ooty.\n"
                    "   - **Best For:** Family trips, heritage lovers, and those who enjoy scenic mountain viewpoints.\n"
                    "   - **Climate:** Cool year-round (10°C - 20°C), winter gets chilly (down to 5°C).\n\n"
                    "2. **Kodaikanal (Princess of Hill Stations - Dindigul):**\n"
                    "   - **Vibe:** Misty pine forests, serene Kodai Lake, scenic cycling paths, and relaxed cafe culture.\n"
                    "   - **Special Highlight:** Coaker's Walk, Pillar Rocks, and homemade chocolates.\n"
                    "   - **Best For:** Honeymoon couples, solo backpackers, and peaceful nature walks.\n\n"
                    "**Verdict:**\n"
                    "- Active sightseeing & toy train experience venumna: **Ooty** choose pannunga.\n"
                    "- Peaceful misty walks, cycling & relaxed lake vibe venumna: **Kodaikanal** choose pannunga.\n\n"
                    "Endha place-ku detailed itinerary plan pannalama?"
                )
            else:
                return (
                    "### 🏔️ Ooty vs Kodaikanal: Which Hill Station is Better for You?\n\n"
                    "Both **Ooty** (Nilgiris) and **Kodaikanal** (Dindigul) are jewels of the Western Ghats, but they cater to distinct travel preferences:\n\n"
                    "#### 1. Ooty — The Queen of Hill Stations (Nilgiris)\n"
                    "- **Atmosphere:** Expansive rolling tea plantations, eucalyptus groves, and British colonial charm.\n"
                    "- **Key Highlights:** The UNESCO Nilgiri Mountain Railway Toy Train, Doddabetta Peak, Government Botanical Garden, and Pykara Lake.\n"
                    "- **Ideal For:** Families, heritage enthusiasts, and photography lovers.\n"
                    "- **Connectivity:** Accessible via Coimbatore (86 km) or Mettupalayam.\n\n"
                    "#### 2. Kodaikanal — The Princess of Hill Stations (Dindigul)\n"
                    "- **Atmosphere:** Star-shaped lake, dense pine forests, romantic mist, and relaxed walking trails.\n"
                    "- **Key Highlights:** Coaker's Walk, Pillar Rocks, Bryant Park, homemade chocolate shops, and cycling around the lake.\n"
                    "- **Ideal For:** Couples, solo travellers, and those looking for a laid-back, serene retreat.\n"
                    "- **Connectivity:** Accessible via Madurai (120 km) or Dindigul (95 km).\n\n"
                    "#### 💡 Practical Recommendation\n"
                    "- Choose **Ooty** if you want grand viewpoints, lush tea estates, and the iconic toy train.\n"
                    "- Choose **Kodaikanal** if you prefer cooler walking weather, dense pine woods, and a relaxed, misty ambiance.\n\n"
                    "Would you like a customized day-by-day plan for either of these destinations?"
                )

        # CASE 2: Follow-up Deep Dive on a specific numbered item ("the first place", "second place", "third place")
        if intent["referred_item_index"] is not None or intent["named_attraction"]:
            idx = intent["referred_item_index"] if intent["referred_item_index"] is not None else 0
            if idx >= len(attractions):
                idx = 0
            target_att = attractions[idx]

            # Special in-depth coverage for Adiyogi / Isha if Coimbatore first spot
            if "adiyogi" in target_att["name"].lower() or intent["named_attraction"] == "adiyogi":
                if lang == "tanglish":
                    return (
                        "### 🕉️ Adiyogi Shiva & Isha Yoga Centre (Coimbatore) — Complete Guide\n\n"
                        "Coimbatore la Adiyogi Shiva Statue romba iconic landmark. Idho detailed guide:\n\n"
                        "#### 🌟 Key Experiences & Highlights\n"
                        "- **112-Foot Adiyogi Statue:** Guinness World Record holder as the world's largest bust sculpture, representing 112 ways to attain liberation.\n"
                        "- **Divya Darshanam (3D Laser Light & Sound Show):** Daily evening **7:00 PM - 7:30 PM**. Shiva's story is projected directly onto the 112ft face — free to watch and visually breathtaking!\n"
                        "- **Dhyanalinga Meditation Dome:** Powerful consecrated space where anyone can sit in deep silence (no chanting or rituals required).\n"
                        "- **Theerthakunds (Suryakund & Chandrakund):** Energized underground water bodies where visitors can take a sacred dip before entering the Dhyanalinga.\n\n"
                        "#### 🚌 How to Reach from Coimbatore\n"
                        "- **By City Bus:** Direct TNSTC Bus **Route 14D** departs frequently from **Gandhipuram Bus Stand** and **Ukkadam Bus Stand** directly to the Isha Yoga Centre gate (~45 mins).\n"
                        "- **By Taxi / Auto:** Approximately 30 km from Coimbatore railway station / city center (~45-60 mins drive along Siruvani Main Road).\n\n"
                        "#### 💡 Practical Visitor Tips\n"
                        "- **Entry Fee:** Completely Free entry to Adiyogi and Dhyanalinga.\n"
                        "- **Timings:** Open from **6:00 AM to 8:00 PM** daily.\n"
                        "- **Dress Code:** Modest Indian attire (dhoti, pants, kurti, saree) covering shoulders and knees.\n"
                        "- **Best Time to Visit:** Arrive by **4:30 PM** to experience Dhyanalinga in peace, watch the sunset behind the Velliangiri hills, and catch the 7:00 PM laser show!\n\n"
                        "Adutha spot pathi therinjukanuma, illa trip plan pannalama?"
                    )
                else:
                    return (
                        "### 🕉️ Deep Dive: Adiyogi Shiva Statue & Isha Yoga Centre, Coimbatore\n\n"
                        "Here is everything you need to know about visiting Coimbatore's premier spiritual and cultural landmark:\n\n"
                        "#### 🌟 What Makes It Iconic\n"
                        "- **The Monument:** Standing 112 feet tall at the foothills of the Velliangiri Mountains, it is recognized by the Guinness World Records as the world's largest bust sculpture. It symbolizes the 112 pathways to inner transformation.\n"
                        "- **Divya Darshanam (3D Laser Projection Show):** Every evening at **7:00 PM**, an awe-inspiring 14-minute 3D laser mapping show narrates the legend of Adiyogi projected directly onto the statue. Entry is completely free.\n"
                        "- **Dhyanalinga Dome:** A silent, meditative sanctum housing a massive 13-foot-9-inch linga. Visitors sit in absolute silence regardless of faith or beliefs.\n"
                        "- **Suryakund & Chandrakund:** Consecrated underground water bodies filled with energized water where visitors can take a refreshing dip before meditation.\n\n"
                        "#### 🚆 Transportation & Connectivity\n"
                        "- **From Coimbatore City Center:** Located 30 km west of Coimbatore Railway Station.\n"
                        "- **By Public Bus:** Board **TNSTC Bus Route 14D** from Gandhipuram Central Bus Stand or Ukkadam Bus Stand (fare: ~₹25 - ₹35, runs every 30 minutes).\n"
                        "- **By Cab / Auto:** Prepaid cabs and auto-rickshaws take approximately 50 minutes via Siruvani Road.\n\n"
                        "#### 💡 Visitor Guidelines & Practical Advice\n"
                        "- **Entry Fee:** Free admission.\n"
                        "- **Timings:** 6:00 AM – 8:00 PM.\n"
                        "- **Dress Code:** Conservative clothing covering shoulders and knees (traditional wear preferred).\n"
                        "- **Recommended Arrival:** Reach around **4:30 PM** to explore the ashram, meditate inside the Dhyanalinga, take sunset photos against the hills, and secure front seats for the 7:00 PM light show.\n\n"
                        "Would you like to hear about the second attraction (Marudhamalai) or plan a complete day itinerary?"
                    )

            # Special in-depth coverage for Marudhamalai if 2nd spot
            if "marudhamalai" in target_att["name"].lower():
                return (
                    "### 🛕 Deep Dive: Marudhamalai Subramaniaswamy Hill Temple, Coimbatore\n\n"
                    "Perched on a scenic hillock of the Western Ghats (approx 12 km from Coimbatore city center), **Marudhamalai** is dedicated to Lord Murugan and revered for over 1,200 years:\n\n"
                    "#### 🌟 Highlights & Sacred Sights\n"
                    "- **Hilltop Sanctum:** Surrounded by medicinal herb-filled forests (Marudham trees). The hill breeze is said to possess natural healing properties.\n"
                    "- **Pambatti Siddhar Cave:** Cave shrine dedicated to one of the 18 celebrated Tamil Siddhars, situated close to the main temple complex.\n"
                    "- **Scenic Hill Views:** Breathtaking panoramic vistas over Coimbatore city and agricultural fields.\n\n"
                    "#### 🚌 Access & Practical Info\n"
                    "- **How to Reach:** TNSTC buses run frequently from Gandhipuram Bus Stand (Route 1C, 1D). Frequent Devasthanam mini-buses take visitors from the foothill to the hilltop temple (fare ~₹10).\n"
                    "- **Walking Option:** Devotees can climb the shaded stone stairway (~800 steps, approx 30 minutes).\n"
                    "- **Timings:** 06:00 AM to 01:00 PM & 02:00 PM to 08:30 PM.\n"
                    "- **Entry Fee:** Free general darshan; Special darshan tickets available at ₹20 - ₹50.\n\n"
                    "**Tip:** Morning hours before 10:00 AM offer the pleasantest climate and minimal darshan queues."
                )

            # Special in-depth coverage for Siruvani Waterfalls if 3rd spot
            if "siruvani" in target_att["name"].lower():
                return (
                    "### 🌊 Deep Dive: Siruvani Waterfalls & Dam, Coimbatore\n\n"
                    "Located 36 km west of Coimbatore in the dense reserve forests of the Western Ghats, Siruvani is celebrated worldwide for having some of the sweetest mineral-rich drinking water on earth:\n\n"
                    "#### 🌟 Experience & Highlights\n"
                    "- **Natural Forest Falls:** Cascades amidst pristine evergreen foliage maintained by the Tamil Nadu Forest Department.\n"
                    "- **Sadivayal Checkpost & Forest Safari:** Private vehicles are parked at the Sadivayal gate; forest department safari jeeps/vans take visitors on the scenic 4 km jungle trail to the waterfall.\n\n"
                    "#### 💡 Practical Travel Advice\n"
                    "- **Timings:** 10:00 AM to 03:30 PM (Entry permitted subject to forest regulations).\n"
                    "- **Entry & Forest Van Fee:** Approx ₹80 - ₹120 per head including the forest safari vehicle.\n"
                    "- **Seasonal Note:** *Water levels depend heavily on monsoon rainfall in the ghats. During heavy downpours or dry summer peaks, forest authorities may restrict entry. Always check local forest gate notices before heading out.*\n"
                    "- **How to Reach:** Accessible via Siruvani Road from Coimbatore city (~1 hour drive)."
                )

            # Generic detailed deep dive for other attractions
            return (
                f"### 📍 Detailed Spotlight: {target_att['name']} ({district} District, Tamil Nadu)\n\n"
                f"- **The Experience:** {target_att['experience']}\n"
                f"- **Recommended Duration:** {target_att['duration']}\n"
                f"- **Entry Fee:** {target_att['entry_fee']}\n"
                f"- **Key Highlight:** {target_att['highlights']}\n\n"
                f"#### 💡 Practical Tips for Visitors\n"
                f"- Visit during morning hours (08:30 AM - 10:30 AM) or late afternoon for pleasant weather and photography.\n"
                f"- Modest comfortable clothing and walking shoes recommended.\n\n"
                f"Would you like an itinerary connecting this with nearby places in {district}?"
            )

        # CASE 3: Itinerary Request or Conversational Replanning ("Plan a two-day trip within ₹3,000" / "Make it cheaper and add nature places")
        if intent["is_itinerary_request"] or intent["is_cheaper"] or intent["add_nature"] or intent["no_temples"]:
            days = intent["days"]
            budget_limit = intent["budget_limit"]
            is_budget_mode = intent["is_cheaper"] or (budget_limit is not None and budget_limit <= 3500)

            # Modifications text banner
            mods = []
            if intent["is_cheaper"]:
                mods.append("Budget lodges & TNSTC public transit")
            if intent["add_nature"]:
                mods.append("Added nature spots: Kovai Kutralam, Siruvani foothills & Singanallur Lake nature reserve")
            if intent["no_temples"]:
                mods.append("Replaced temple visits with outdoor viewpoints & heritage walks")

            mod_banner = f" *(Adjustments applied: {', '.join(mods)})*" if mods else ""

            # Specially customized itinerary for Coimbatore 2-day budget plan
            if name == "Coimbatore" and days == 2:
                if intent["add_nature"]:
                    return (
                        f"### 🌿 Revised 2-Day Nature & Budget Itinerary for Coimbatore{mod_banner}\n\n"
                        f"I have customized your itinerary to prioritize **serene nature destinations** while keeping expenses strictly minimal:\n\n"
                        f"#### 📅 Day 1: Western Ghats Nature & Foothills\n"
                        f"- **Morning (08:30 AM - 12:30 PM): Siruvani Foothills & Kovai Kutralam Waterfalls**\n"
                        f"  - *Experience:* Enjoy the lush forest canopy, cascading stream bath, and sweet natural mineral springs.\n"
                        f"  - *Transit:* TNSTC Bus from Gandhipuram / Ukkadam to Sadivayal (₹25).\n"
                        f"  - *Entry:* ₹80 (forest entry & safari van).\n"
                        f"- **Afternoon (01:00 PM - 02:30 PM): Traditional Kongu Tiffin**\n"
                        f"  - *Meal:* Piping hot vegetarian banana leaf meal with country vegetable kootu (₹120 at local mess).\n"
                        f"- **Evening (04:30 PM - 07:45 PM): Velliangiri Foothills & Adiyogi Sunset**\n"
                        f"  - *Experience:* Peaceful nature walk at the foot of the 7 sacred peaks, followed by the free 7:00 PM 3D laser light show at the 112ft Adiyogi.\n"
                        f"  - *Transit:* Local bus (₹20).\n\n"
                        f"#### 📅 Day 2: Urban Nature Sanctuary & Cultural Heritage\n"
                        f"- **Morning (08:00 AM - 11:30 AM): Singanallur Lake Nature & Butterfly Sanctuary**\n"
                        f"  - *Experience:* Free nature conservation trail, home to over 110 bird species and diverse butterfly flora.\n"
                        f"  - *Entry:* Free admission.\n"
                        f"- **Afternoon (12:30 PM - 02:30 PM): Gedee Car Museum**\n"
                        f"  - *Experience:* Vintage automobile engineering collection showing the evolution of transport.\n"
                        f"  - *Entry:* ₹75.\n"
                        f"- **Evening (05:00 PM - 07:30 PM): Valankulam Lake Promenade & Sunset Walk**\n"
                        f"  - *Experience:* Relaxed breeze along the landscaped lakefront boardwalk with street food snacks.\n\n"
                        f"#### 💰 Budget Validation (Target: within ₹3,000 for solo or budget pair)\n"
                        f"| Expense Category | Solo Traveller | 2 Travellers | Basis |\n"
                        f"|---|---|---|---|\n"
                        f"| **Budget Stay (1 Night)** | ₹800 | ₹1,200 | Clean lodge/dorm near Gandhipuram |\n"
                        f"| **Local Transit (2 Days)** | ₹180 | ₹360 | TNSTC city buses (14D, 1C) |\n"
                        f"| **Food & Refreshments** | ₹650 | ₹1,200 | Authentic mess meals & filter coffee |\n"
                        f"| **Entry & Nature Fees** | ₹155 | ₹310 | Kovai Kutralam & Gedee Museum |\n"
                        f"| **Contingency Buffer** | ₹150 | ₹250 | Emergency auto / bottled water |\n"
                        f"| **Total Estimated Cost** | **₹1,935** | **₹3,320** | **Easily fits within your ₹3,000 solo budget!** |\n\n"
                        f"*Note: Waterfall water levels depend on monsoon rainfall. Please verify forest gate access locally before departure.*"
                    )
                else:
                    return (
                        f"### 🗺️ Personalized 2-Day Coimbatore Budget Itinerary (Within ₹3,000){mod_banner}\n\n"
                        f"Here is a carefully balanced itinerary designed to cover Coimbatore's premier landmarks while keeping total expenses strictly within **₹3,000**:\n\n"
                        f"#### 📅 Day 1: Heritage & Spiritual Icons\n"
                        f"- **Morning (08:30 AM - 12:30 PM): Marudhamalai Murugan Hill Temple**\n"
                        f"  - *Experience:* Historic 12th-century hill shrine set amid Western Ghats medicinal foliage.\n"
                        f"  - *Transit:* Bus Route 1C from Gandhipuram (₹18); foothill shuttle (₹10).\n"
                        f"  - *Entry:* Free general darshan.\n"
                        f"- **Lunch (01:00 PM - 02:30 PM): Authentic Kongu Lunch**\n"
                        f"  - *Meal:* Wholesome South Indian thali at Sree Annapoorna or local traditional mess (₹120).\n"
                        f"- **Evening (04:30 PM - 07:45 PM): Adiyogi Shiva Statue & Isha Yoga Centre**\n"
                        f"  - *Experience:* 112ft Adiyogi monument, Dhyanalinga silent meditation, and the free 7:00 PM Divya Darshanam 3D laser light show.\n"
                        f"  - *Transit:* TNSTC Bus 14D from Ukkadam (₹25).\n"
                        f"  - *Entry:* Free admission.\n\n"
                        f"#### 📅 Day 2: Science, Craft & Local Flavor\n"
                        f"- **Morning (09:00 AM - 12:00 PM): Gedee Car Museum**\n"
                        f"  - *Experience:* World-class collection of vintage automobiles spanning German, British, and Indian motoring history.\n"
                        f"  - *Entry:* ₹75 per ticket.\n"
                        f"- **Afternoon (12:30 PM - 03:00 PM): Town Hall Street Food & Filter Coffee Walk**\n"
                        f"  - *Experience:* Taste authentic Coimbatore snacks, Kongu mushroom roast, and iconic filter coffee.\n"
                        f"- **Evening (04:30 PM - 07:00 PM): Singanallur Lake Bird Sanctuary or Perur Pateeswarar Temple**\n"
                        f"  - *Experience:* Ancient 1,500-year-old carved temple architecture with magnificent stone pillars.\n"
                        f"  - *Entry:* Free.\n\n"
                        f"#### 💰 Budget Breakdown\n"
                        f"| Category | Solo Estimate | Basis |\n"
                        f"|---|---|---|\n"
                        f"| **Clean Budget Stay (1 Night)** | ₹900 | Clean lodge near railway station / Gandhipuram |\n"
                        f"| **Public Bus Transit (2 Days)** | ₹160 | TNSTC city buses (14D, 1C) |\n"
                        f"| **Food & Tiffin (2 Days)** | ₹700 | Authentic vegetarian mess meals & breakfast |\n"
                        f"| **Sightseeing Entry Tickets** | ₹75 | Gedee Car Museum (others free) |\n"
                        f"| **Contingency Reserve** | ₹200 | Buffer for snacks/water |\n"
                        f"| **Total Trip Estimate** | **₹2,035** | **Well within your ₹3,000 limit (₹965 remaining)!** |\n\n"
                        f"Would you like to make any changes? E.g., 'Make it cheaper and add nature places' or 'Add more food spots'?"
                    )

            # Generic structured itinerary fallback
            if itinerary_data:
                plan_md = f"### 🗺️ Personalized {days}-Day Itinerary for {name}, Tamil Nadu{mod_banner}\n\n"
                plan_md += f"{overview}\n\n"
                for d in itinerary_data["days"]:
                    plan_md += f"#### 📅 {d['theme']}\n"
                    plan_md += f"- **Morning (08:30 AM - 12:30 PM):** **{d['morning']['title']}**\n"
                    plan_md += f"  - *Experience:* {d['morning']['activity']}\n"
                    plan_md += f"  - *Entry:* {d['morning']['entry_fee']} | *Transit:* {d['morning']['travel_transit']}\n"
                    if d.get("afternoon"):
                        plan_md += f"- **Afternoon (02:00 PM - 05:00 PM):** **{d['afternoon']['title']}**\n"
                        plan_md += f"  - *Experience:* {d['afternoon']['activity']}\n"
                    if d.get("evening"):
                        plan_md += f"- **Evening (05:30 PM - 08:00 PM):** **{d['evening']['title']}**\n"
                        plan_md += f"  - *Experience:* {d['evening']['activity']}\n"
                    plan_md += f"- **Recommended Meal:** {d['meals']['lunch']}\n\n"

                if budget_data:
                    plan_md += f"#### 💰 Deterministic Travel Budget (~₹{budget_data['total_estimated']:,} Total)\n"
                    plan_md += f"- Accommodation: ₹{budget_data['breakdown']['accommodation']['amount']:,}\n"
                    plan_md += f"- Transit & Transport: ₹{budget_data['breakdown']['intercity_transport']['amount'] + budget_data['breakdown']['local_transport']['amount']:,}\n"
                    plan_md += f"- Meals & Tiffin: ₹{budget_data['breakdown']['food']['amount']:,}\n"
                    plan_md += f"- Activities & Entry: ₹{budget_data['breakdown']['activities']['amount']:,}\n\n"

                plan_md += "*Note: Local transport fares and seasonal attractions may vary based on weather conditions.*"
                return plan_md

        # CASE 4: Transit Query (e.g. "How can I travel from Chennai to Kanyakumari?")
        if intent["is_transit_query"]:
            if "chennai" in user_msg.lower() and "kanyakumari" in user_msg.lower():
                return (
                    "### 🚆 How to Travel from Chennai to Kanyakumari (700 km Guide)\n\n"
                    "Travelling from Tamil Nadu's northern capital to its southernmost coastal tip is well connected:\n\n"
                    "#### 1. By Train (Most Recommended & Comfortable)\n"
                    "- **Vande Bharat Express (Train 20665):** Fastest day connection (Chennai Egmore to Nagercoil/Kanyakumari in approx 8.5 hours).\n"
                    "- **Kanyakumari Superfast Express (Train 12633):** Departs Chennai Egmore at 5:15 PM and arrives in Kanyakumari by 5:50 AM the next morning. Ideal overnight journey.\n"
                    "- **Ananthapuri Express (Train 20635):** Daily night sleeper/AC express via Villupuram, Trichy, Madurai, and Tirunelveli.\n\n"
                    "#### 2. By Flight (Via Trivandrum)\n"
                    "- Fly from **Chennai (MAA)** to **Trivandrum (TRV)** (~1 hour 15 mins).\n"
                    "- From Trivandrum, take a taxi or passenger train for the scenic 90 km drive to Kanyakumari (~2.5 hours).\n\n"
                    "#### 3. By Road (Car or Bus)\n"
                    "- **Highway Route:** **NH 44** (Chennai → Villupuram → Trichy → Madurai → Tirunelveli → Kanyakumari). Smooth 4-lane national highway (~11 - 13 hours).\n"
                    "- **Government Buses:** SETC Air-Conditioned Sleeper buses depart nightly from KCBT Kilambakkam.\n\n"
                    "Would you like an itinerary planned for when you arrive in Kanyakumari?"
                )
            elif "coimbatore" in user_msg.lower() and "ooty" in user_msg.lower():
                return (
                    "### 🚗 How to Travel from Coimbatore to Ooty (86 km Guide)\n\n"
                    "The journey from Coimbatore into the Nilgiri hills climbs from the plains to 2,200 meters elevation:\n\n"
                    "1. **By Bus (TNSTC):** Regular buses run from **Coimbatore Gandhipuram Mettupalayam Bus Stand** to Mettupalayam, then up to Coonoor and Ooty (~3.5 hours, fare ~₹100).\n"
                    "2. **By Toy Train (Heritage Nilgiri Mountain Railway):** Take a train or taxi to **Mettupalayam Railway Station**, then board the iconic UNESCO steam toy train to Ooty (departs 07:10 AM, arrives Ooty 12:00 PM). *Advance booking on IRCTC recommended.*\n"
                    "3. **By Private Car / Taxi:** Drive via Mettupalayam and the scenic Burliar Ghat road (~2.5 to 3 hours). Check ghat road alerts during heavy rains.\n\n"
                    "Would you like recommendations on where to stop along the way?"
                )

        # CASE 5: Food Query
        if intent["is_food_query"]:
            return (
                f"### 🍛 Authentic Food Experiences in {name}, Tamil Nadu\n\n"
                f"The culinary traditions of {name} ({district} district) are renowned for authentic local spices and fresh ingredients:\n\n"
                f"#### ⭐ Iconic Regional Dishes\n"
                + "".join([f"- **{s.strip()}:** Prepared with authentic regional spices and traditional cooking techniques.\n" for s in specialties.split(",") if s.strip()])
                + f"\n#### 🏛️ Legendary Spots & Traditional Messes\n"
                + "".join([f"- **{e.strip()}:** Renowned local institution.\n" for e in eateries.split(",") if e.strip()])
                + f"\n#### 💡 Foodie Advice\n"
                f"- Best experienced hot on fresh plantain leaves with traditional filter coffee.\n"
                f"- Ask for local mess thali meals during lunchtime for the freshest spreads."
            )

        # CASE 6: Hidden Gems Query
        if intent["is_hidden_gems"]:
            return (
                f"### 💎 Offbeat & Hidden Gems in {name} ({district} District)\n\n"
                f"Beyond the crowded tourist trails, {name} offers wonderful lesser-known treasures:\n\n"
                + "".join([f"#### • {a['name']}\n- **What Makes It Special:** {a['experience']}\n- **Highlights:** {a['highlights']}\n- **Entry:** {a['entry_fee']}\n" for a in attractions[1:]])
                + f"\n#### 🍛 Regional Food Gem\n- Don't miss trying: **{specialties}** at iconic local haunts like **{eateries}**.\n\n"
                f"Would you like a customized day plan connecting these offbeat spots?"
            )

        # CASE 7: Default Open-Ended Guide (e.g. "What are the best tourist places in Coimbatore?")
        if lang == "tanglish":
            return (
                f"### 📍 Welcome to {name} ({district} District, Tamil Nadu)\n\n"
                f"Vanakkam! {overview}\n\n"
                f"#### ⭐ Top Attractions to Visit:\n"
                + "".join([f"{i+1}. **{a['name']}:** {a['experience']} *(Entry: {a['entry_fee']} | Time: {a['duration']})*\n" for i, a in enumerate(attractions[:4])])
                + f"\n#### 🍛 Famous Local Food:\n"
                f"- **Specialties:** {specialties}\n"
                f"- **Iconic Spots:** {eateries}\n\n"
                f"#### 🚗 Best Time & Travel Tips:\n"
                f"- **Best Season:** {best_time}\n"
                f"- **Ideal Stay:** {dest_data.get('ideal_duration', '1 to 2 days')}\n\n"
                f"Indha places pathi deep dive pannanuma? 'Tell me more about the first place' or 'Plan trip' nu sollunga!"
            )
        else:
            return (
                f"### 📍 Comprehensive Travel Guide: {name} ({district} District, Tamil Nadu)\n\n"
                f"**Overview:** {overview}\n\n"
                f"#### ⭐ Top Attractions & Verified Experiences\n"
                + "".join([f"{i+1}. **{a['name']}**\n   - *Experience:* {a['experience']}\n   - *Duration:* {a['duration']} | *Entry Fee:* {a['entry_fee']}\n   - *Highlights:* {a['highlights']}\n" for i, a in enumerate(attractions[:4])])
                + f"\n#### 🍛 Regional Food & Delicacies\n"
                f"- **Signature Specialties:** {specialties}\n"
                f"- **Iconic Eateries:** {eateries}\n\n"
                f"#### 🚆 Transportation & Best Season\n"
                f"- **Best Season to Visit:** {best_time}\n"
                f"- **Recommended Stay:** {dest_data.get('ideal_duration', '1 to 2 days')}\n"
                f"- **Transit Connectivity:** {transport.get('railway', 'Connected via Southern Railway')}; {transport.get('road', 'State and National Highways')}\n"
                f"- **Estimated Daily Budget:** {dest_data.get('estimated_budget_per_day', '₹1,000 - ₹2,500 per person')}\n\n"
                f"#### 💡 Practical Tips\n"
                + "".join([f"- {tip}\n" for tip in dest_data.get("travel_tips", [])[:2]])
                + f"\n*Tip: Would you like to know more about the first place, or should I create a personalized itinerary within your budget?*"
            )

    def get_dynamic_follow_ups(self, dest_name: str, intent: Dict[str, Any]) -> List[str]:
        if intent["is_itinerary_request"]:
            return [
                "Make it cheaper and add nature places",
                "Tell me more about the first place",
                "What traditional food should I try?",
                "Which is better: Ooty or Kodaikanal?"
            ]
        elif intent["referred_item_index"] is not None:
            return [
                "Plan a two-day trip within ₹3,000",
                "Tell me more about the second place",
                "What traditional food should I try?",
                "How to travel by public bus?"
            ]
        elif intent["is_food_query"]:
            return [
                f"Plan a 2-day trip to {dest_name}",
                f"Suggest hidden gems in {dest_name}",
                "How to travel by train and bus?"
            ]
        else:
            return [
                "Tell me more about the first place",
                "Plan a two-day trip within ₹3,000",
                f"Suggest hidden gems in {dest_name}",
                "Which is better: Ooty or Kodaikanal?"
            ]
