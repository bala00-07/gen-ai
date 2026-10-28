"""
TamilNadu TravelAI - Strict Domain Guardrail
Implements multi-level domain enforcement ensuring the assistant exclusively
answers questions concerning Tamil Nadu travel and tourism across all 38 districts.
"""

import re
from typing import Tuple, Optional

# Exact required out-of-scope response
OUT_OF_SCOPE_RESPONSE = (
    "I'm your Coimbatore and Tamil Nadu Travel Guide Bot. "
    "I can help you explore destinations, discover local food and culture, "
    "find routes, estimate budgets, and plan trips throughout Tamil Nadu. What would you like to explore?"
)

# Unrelated topics keyword/pattern matches
PROGRAMMING_PATTERNS = [
    r"\b(python|javascript|typescript|c\+\+|java|react|html|css|sql|function|def\s+|algorithm|regex|git|docker|api\s+key|code|debug|compile|npm|pip)\b",
    r"\b(write a script|programming|recursion|sorting algorithm|binary tree|leetcode|oop|variable|database query)\b"
]

FINANCE_PATTERNS = [
    r"\b(stock\s+market|nifty|sensex|crypto|bitcoin|ethereum|shares|trading|forex|invest\s+in\s+stocks|mutual\s+fund\s+portfolio|dividend|cryptocurrency)\b"
]

MEDICAL_PATTERNS = [
    r"\b(diagnos(e|is)|prescri(be|ption)|symptoms of cancer|treat\s+diabetes|medical\s+advice|antibiotic\s+dosage|cure\s+for\s+disease|blood pressure medicine)\b"
]

POLITICS_PATTERNS = [
    r"\b(who should i vote for|election prediction|prime minister debate|political party manifesto|bjp vs congress|dmk vs admk politics)\b"
]

HOMEWORK_PATTERNS = [
    r"\b(solve this math problem|quadratic equation|calculus|derive the formula|write an essay on global warming|chemistry reaction|quantum mechanics|algebraic equation)\b"
]

GENERAL_KNOWLEDGE_NON_TRAVEL = [
    r"\b(capital of (france|spain|italy|germany|usa|uk|japan|australia|canada|russia|china))\b",
    r"\b(who invented|who is elon musk|who is bill gates|who won the (fifa|world cup|olympics))\b",
    r"\b(explain photosynthesis|theory of relativity|how does a rocket work|explain black holes)\b"
]

# Non-TN destinations that should be politely redirected unless asking transit to/from Tamil Nadu
NON_TN_REGIONS = [
    "goa", "paris", "london", "switzerland", "dubai", "new york", "singapore", "bali",
    "ladakh", "manali", "shimla", "kashmir", "jaipur", "udaipur", "varanasi", "agra",
    "mumbai", "delhi", "kolkata", "amritsar", "rishikesh", "darjeeling", "sikkim",
    "andaman", "maldives", "thailand", "vietnam", "kerala", "bangalore", "bengaluru",
    "mysore", "hyderabad", "kochi", "munnar", "wayanad", "alleppey", "varkala"
]

# Transit intent keywords (e.g., "how to reach Coimbatore from Bangalore/Kerala/Delhi")
TRANSIT_KEYWORDS = ["from", "to", "reach", "travel to", "how to go", "flight", "train to", "bus to", "route", "distance"]

# ALL 38 DISTRICTS OF TAMIL NADU AND MAJOR HUBS
ALL_38_DISTRICTS = [
    "ariyalur", "chengalpattu", "chennai", "coimbatore", "cuddalore",
    "dharmapuri", "dindigul", "erode", "kallakurichi", "kancheepuram", "kanchipuram",
    "kanniyakumari", "kanyakumari", "karur", "krishnagiri", "madurai",
    "mayiladuthurai", "nagapattinam", "namakkal", "nilgiris", "perambalur",
    "pudukkottai", "ramanathapuram", "ranipet", "salem", "sivaganga",
    "tenkasi", "thanjavur", "theni", "thoothukudi", "tiruchirappalli",
    "tirunelveli", "tirupathur", "tiruppur", "tiruvallur", "tiruvannamalai",
    "tiruvarur", "vellore", "viluppuram", "villupuram", "virudhunagar"
]

# Prominent towns, heritage sites, hills, beaches, and attractions across the 38 districts
TN_HUBS_AND_ATTRACTIONS = [
    "tamil nadu", "tamilnadu", "ooty", "coonoor", "kotagiri", "kodaikanal", "kodai",
    "tanjore", "thanjavur", "trichy", "tiruchirappalli", "rameswaram", "rameshwaram",
    "nellai", "tirunelveli", "courtallam", "kutralam", "tuticorin", "thoothukudi",
    "dhanushkodi", "yercaud", "yelagiri", "valparai", "pollachi", "topslip", "anamalai",
    "mahabalipuram", "mamallapuram", "kanchi", "kanchipuram", "chidambaram",
    "kumbakonam", "chettinad", "karaikudi", "hogenakkal", "velankanni",
    "pichavaram", "mudumalai", "masinagudi", "sathyamangalam", "palani",
    "siruvani", "marudhamalai", "adiyogi", "isha", "isha yoga", "gedee car museum",
    "eachanari", "perur", "velliangiri", "kovai kutralam", "monkey falls", "aliyar dam",
    "singanallur", "meenakshi amman", "meenakshi temple", "thirumalai nayakkar", "alagar kovil",
    "brihadisvara", "big temple", "rockfort", "srirangam", "kallanai", "pamban", "pamban bridge",
    "vivekananda rock", "thiruvalluvar statue", "gangaikonda cholapuram", "tarangambadi",
    "tranquebar", "poompuhar", "suruli falls", "megamalai", "ayyanar falls", "bannari",
    "kodiveri", "bhavanisagar", "thirumoorthy", "amaravathi", "srivilliputhur", "sivakasi",
    "kolli hills", "agaya gangai", "namakkal fort", "gingee fort", "rajagiri", "kalvarayan",
    "jawadhu hills", "sripuram", "golden temple vellore", "annamalaiyar", "girivalam",
    "ramana ashram", "marina beach", "elliots beach", "besant nagar", "kapaleeshwarar",
    "san thome", "vandalur zoo", "guindy national park", "silver beach", "manapad",
    "tiruchendur", "papanasam", "manjolai", "agathiyar falls", "darasuram", "swamimalai",
    "thiruvaiyaru", "sittannavasal", "thirumayam", "avudaiyarkoil", "pillayarpatti",
    "karaivetti", "varanavasi", "ranjankudi fort", "pulicat lake", "poondi reservoir",
    "doddabetta", "pykara", "avalanche", "sims park", "dolphins nose", "pillar rocks",
    "coakers walk", "berijam lake", "silver cascade", "sirumalai", "kumbakkarai", "kurangani",
    "cheyyur", "arcot", "padmanabhapuram palace", "vattakottai", "thiruparappu", "chettipalayam"
]

TN_IDENTIFIERS = list(set(ALL_38_DISTRICTS + [h.lower() for h in TN_HUBS_AND_ATTRACTIONS]))

# Tamil/Tanglish travel intent words
TAMIL_TRAVEL_WORDS = [
    "trip", "tour", "places", "sollunga", "poganum", "ponum", "plan", "bus", "train", "budget", "sapadu",
    "food", "hotel", "stay", "room", "kattunga", "neram", "evvalavu", "cost", "family",
    "vanakkam", "paarkka", "edangal", "ooru", "kovil", "temple", "malai", "aruvi",
    "kuzhandhainga", "nalla", "epdi", "irukkum", "enga", "kulla", "valiyur", "sutri"
]

def check_domain_scope(query: str, conversation_history: Optional[list] = None) -> Tuple[bool, Optional[str]]:
    """
    Evaluates whether the user's message is strictly in the domain of Tamil Nadu travel & tourism.
    Supports all 38 districts and dynamic conversation context.
    Returns: (is_in_scope: bool, reason_or_redirect_message: Optional[str])
    """
    text = query.strip().lower()

    if not text:
        return False, OUT_OF_SCOPE_RESPONSE

    # Greetings in Tamil/English are in-scope
    greetings = ["hi", "hello", "vanakkam", "hey", "good morning", "good evening", "namaste", "help", "வணக்கம்"]
    if text in greetings or any(text.startswith(g) for g in ["vanakkam", "hello", "hi ", "வணக்கம்"]):
        return True, None

    # Step 1: Check for strictly forbidden out-of-scope domains
    # Programming / coding
    for pattern in PROGRAMMING_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            # Exception: 'python' in snakes at Guindy snake park
            if "snake park" in text or "guindy" in text:
                continue
            return False, OUT_OF_SCOPE_RESPONSE

    # Finance / Stock market
    for pattern in FINANCE_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            return False, OUT_OF_SCOPE_RESPONSE

    # Medical diagnosis
    for pattern in MEDICAL_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            return False, OUT_OF_SCOPE_RESPONSE

    # General politics
    for pattern in POLITICS_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            return False, OUT_OF_SCOPE_RESPONSE

    # General homework / academic math
    for pattern in HOMEWORK_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            return False, OUT_OF_SCOPE_RESPONSE

    # General knowledge non-travel
    for pattern in GENERAL_KNOWLEDGE_NON_TRAVEL:
        if re.search(pattern, text, re.IGNORECASE):
            return False, OUT_OF_SCOPE_RESPONSE

    # Step 2: Check for purely non-Tamil Nadu geographic destinations
    for foreign_loc in NON_TN_REGIONS:
        if re.search(r"\b" + re.escape(foreign_loc) + r"\b", text):
            # Transit check: "How to travel from Mumbai to Chennai?"
            has_tn_dest = any(tn in text for tn in TN_IDENTIFIERS)
            has_transit = any(tr in text for tr in TRANSIT_KEYWORDS)
            
            if has_tn_dest and has_transit:
                return True, None
            
            # Check conversation history for transit or TN focus
            has_history_tn = False
            if conversation_history:
                for msg in conversation_history[-4:]:
                    content = msg.get("content", "").lower()
                    if any(tn in content for tn in TN_IDENTIFIERS):
                        has_history_tn = True
                        break

            if not has_tn_dest and not has_history_tn:
                return False, OUT_OF_SCOPE_RESPONSE

    # Step 3: Check if query has explicit Tamil Nadu identifiers
    has_explicit_tn = any(re.search(r"\b" + re.escape(tn) + r"\b", text) for tn in TN_IDENTIFIERS)
    has_tamil_travel = any(w in text for w in TAMIL_TRAVEL_WORDS)
    
    # Generic travel keywords
    travel_keywords = [
        "travel", "visit", "trip", "tour", "hotel", "resort", "food", "itinerary", "places to see",
        "attractions", "sightseeing", "weather", "best time", "budget", "cost", "train", "bus",
        "flight", "taxi", "cab", "temple", "beach", "waterfall", "hill station", "forest", "safari",
        "shopping", "market", "handicrafts", "festivals", "entry fee", "cheaper", "relaxed", "children",
        "hidden gems", "explore", "traditional food", "stay", "things to do", "distance", "route",
        "hills", "falls", "darshan", "timings", "tickets", "booking", "offbeat"
    ]
    has_travel_keyword = any(re.search(r"\b" + re.escape(tk) + r"\b", text) for tk in travel_keywords)

    # Conversational follow-up phrases that refer to prior travel dialogue
    followup_phrases = [
        "make it cheaper", "make the itinerary cheaper", "add food", "what about transport",
        "is it suitable", "tell me more", "tell me more about", "second place", "third place",
        "first place", "1st place", "2nd place", "3rd place", "4th place", "that place",
        "suggest another", "make it shorter", "remove temples", "add nature", "add nature places",
        "replace outdoor", "how much", "plan for me", "give me the complete plan",
        "2 days", "3 days", "one day", "two days", "three days", "weekend", "rendu naal",
        "family trip", "budget la", "child friendly", "relaxed trip", "which is better",
        "which one is better", "which is better:", "compare", "recommend between",
        "within 3000", "within 5000", "within 10000", "within ₹3,000", "within ₹5,000",
        "under 3000", "under 5000", "under ₹3,000", "how far", "how to reach", "can we go by"
    ]
    is_followup = any(fp in text for fp in followup_phrases)

    # If the user has prior messages in conversation history about Tamil Nadu
    has_active_tn_conversation = False
    if conversation_history and len(conversation_history) > 0:
        for msg in conversation_history[-4:]:
            content = msg.get("content", "").lower()
            if any(tn in content for tn in TN_IDENTIFIERS) or any(w in content for w in TAMIL_TRAVEL_WORDS):
                has_active_tn_conversation = True
                break

    if has_explicit_tn or has_tamil_travel or is_followup:
        return True, None

    if has_active_tn_conversation and (is_followup or has_travel_keyword or "better" in text or "more" in text or "first" in text or "second" in text or "plan" in text):
        return True, None

    if has_travel_keyword:
        return True, None

    # Default out of scope if none matched
    return False, OUT_OF_SCOPE_RESPONSE
