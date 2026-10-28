"""
TamilNadu TravelAI - Language and Script Detector
Supports English, Tamil (தமிழ்), and Tanglish (Tamil in Roman script).
Detects language intent and preserves destination integrity.
"""

import re
from typing import Literal

LanguageType = Literal["english", "tamil", "tanglish"]

TANGLISH_MARKERS = [
    r"\b(sollunga|solunga|poganum|ponum|pannunga|kattunga|irukku|irukkum|nalla|rendu|oru|moolam)\b",
    r"\b(enga|epdi|eppo|evvalavu|ethana|yaru|edukku|ennaku|ungala|enakku)\b",
    r"\b(naal|naala|sapadu|saapadu|ooru|oorla|kovil|kovilukku|kovilla)\b",
    r"\b(trip\s+ku|places\s+sollunga|plan\s+pannunga|food\s+enga|budget\s+la)\b",
    r"\b(paakkalam|paarkka|vandhu|poittu|vaanga|poonga)\b",
    r"\b(tanglish|tamil\s+la)\b"
]

def detect_language(text: str, session_lang: LanguageType = "english") -> LanguageType:
    """
    Detects language mode from input text or honors explicit user requests.
    """
    lower_text = text.lower()

    # Explicit user requests
    if "in english" in lower_text or "reply in english" in lower_text or "speak english" in lower_text:
        return "english"
    if "tamil la" in lower_text or "tamilil" in lower_text or "தமிழில்" in text:
        # Check if they want pure Tamil script or Tanglish
        if re.search(r"[\u0B80-\u0BFF]", text):
            return "tamil"
        if "tanglish" in lower_text:
            return "tanglish"
        return "tanglish" if "tanglish" in lower_text else "tamil"
    if "tanglish" in lower_text or "tanglish la" in lower_text:
        return "tanglish"

    # Check for Tamil script (Unicode block \u0B80 - \u0BFF)
    tamil_chars = re.findall(r"[\u0B80-\u0BFF]", text)
    if len(tamil_chars) >= 3:
        return "tamil"

    # Check for Tanglish vocabulary
    for marker in TANGLISH_MARKERS:
        if re.search(marker, lower_text):
            return "tanglish"

    # If already set in session and current message is short / ambiguous, retain session language
    if session_lang in ["tamil", "tanglish"] and len(lower_text.split()) < 4:
        return session_lang

    return "english"
