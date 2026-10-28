"""
TamilNadu TravelAI - FastAPI Backend Server
Provides RESTful APIs for AI chat with strict domain guardrails,
session conversation memory, live weather, destination discovery, and budget tools.
"""

import os
import uuid
from typing import Dict, List, Optional, Any
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from dotenv import load_dotenv

# Load local environment variables from .env
load_dotenv()

from app.knowledge_base import list_all_destinations, get_destination_data
from app.live_weather import fetch_live_weather
from app.llm_client import TravelAssistant
from app.domain_guardrail import OUT_OF_SCOPE_RESPONSE

app = FastAPI(
    title="Coimbatore and Tamil Nadu Travel Guide Bot",
    description="Intelligent AI Travel Assistant dedicated exclusively to travel and tourism in Tamil Nadu, India.",
    version="1.0.0"
)

# Enable CORS for React/Vite development server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Session Conversation Memory Store (In-memory store keyed by session_id)
# Maps session_id -> list of {"role": "user"|"assistant", "content": str, "timestamp": float}
SESSION_HISTORIES: Dict[str, List[Dict[str, str]]] = {}

# Initialize AI Travel Assistant
assistant = TravelAssistant()

# Pydantic Schemas
class ChatRequest(BaseModel):
    session_id: Optional[str] = Field(default=None, description="Unique session ID for conversation memory")
    message: str = Field(..., min_length=1, max_length=2000, description="User's query")
    language: Optional[str] = Field(default="auto", description="Language preference: 'auto', 'english', 'tamil', or 'tanglish'")

class ChatResponse(BaseModel):
    session_id: str
    response: str
    language: str
    is_out_of_scope: bool
    destination_card: Optional[Dict[str, Any]] = None
    itinerary_card: Optional[Dict[str, Any]] = None
    budget_card: Optional[Dict[str, Any]] = None
    live_weather: Optional[Dict[str, Any]] = None
    follow_up_suggestions: List[str] = []

class ResetSessionRequest(BaseModel):
    session_id: str

class ApiKeyUpdate(BaseModel):
    api_key: str

@app.get("/")
def root():
    return {
        "app": "TamilNadu TravelAI API",
        "status": "online",
        "domain": "Tamil Nadu Travel & Tourism Only",
        "documentation": "/docs"
    }

@app.get("/api/health")
def health_check():
    has_key = bool(os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY"))
    return {
        "status": "healthy",
        "gemini_api_configured": has_key,
        "engine_mode": "Hybrid (Gemini + Built-in RAG Reasoning Engine)" if has_key else "Built-in Expert Tamil Nadu Travel Engine",
        "destinations_loaded": len(list_all_destinations())
    }

@app.get("/api/destinations")
def get_destinations():
    """Returns catalog of all verified Tamil Nadu tourism hubs."""
    return {"destinations": list_all_destinations()}

@app.get("/api/destinations/{dest_id}")
def get_destination_details(dest_id: str):
    """Returns rich details of a specific Tamil Nadu destination."""
    data = get_destination_data(dest_id)
    if not data:
        raise HTTPException(status_code=404, detail="Destination not found in Tamil Nadu knowledge base.")
    return data

@app.get("/api/weather/{dest_id}")
async def get_weather(dest_id: str):
    """Fetches real-time live atmospheric forecast for a Tamil Nadu destination."""
    weather = await fetch_live_weather(dest_id)
    if not weather:
        raise HTTPException(status_code=503, detail="Live weather service temporarily unavailable.")
    return weather

@app.post("/api/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    """
    Main conversation endpoint with multi-tier domain restriction,
    conversation memory, live weather retrieval, and structured cards.
    """
    session_id = request.session_id or str(uuid.uuid4())
    
    # Retrieve or initialize session history
    if session_id not in SESSION_HISTORIES:
        SESSION_HISTORIES[session_id] = []
    
    history = SESSION_HISTORIES[session_id]

    try:
        # Process message through assistant
        result = await assistant.process_chat(
            user_message=request.message,
            conversation_history=history,
            language_pref=request.language
        )

        # Update session memory
        history.append({"role": "user", "content": request.message})
        history.append({"role": "assistant", "content": result["response"]})

        # Cap memory at last 20 messages for efficiency
        if len(history) > 20:
            SESSION_HISTORIES[session_id] = history[-20:]

        return ChatResponse(
            session_id=session_id,
            response=result["response"],
            language=result["language"],
            is_out_of_scope=result["is_out_of_scope"],
            destination_card=result["destination_card"],
            itinerary_card=result["itinerary_card"],
            budget_card=result["budget_card"],
            live_weather=result["live_weather"],
            follow_up_suggestions=result["follow_up_suggestions"]
        )

    except Exception as e:
        # Graceful error handling
        return ChatResponse(
            session_id=session_id,
            response="I experienced a temporary glitch while retrieving travel information. Please ask again or specify a destination in Tamil Nadu like Ooty, Madurai, or Coimbatore.",
            language="english",
            is_out_of_scope=False,
            follow_up_suggestions=["Explore Coimbatore", "Plan a 2-Day Ooty Trip", "Madurai Culture & Temples"]
        )

@app.post("/api/session/reset")
def reset_session(req: ResetSessionRequest):
    """Clears conversation memory for a session to start fresh."""
    if req.session_id in SESSION_HISTORIES:
        SESSION_HISTORIES[req.session_id] = []
    return {"status": "success", "message": "Conversation history reset."}

@app.post("/api/settings/key")
def update_gemini_key(req: ApiKeyUpdate):
    """Allows user to configure or update their Gemini API key dynamically."""
    key = req.api_key.strip()
    if key:
        os.environ["GEMINI_API_KEY"] = key
        assistant.api_key = key
        return {"status": "success", "message": "Gemini API key updated successfully."}
    else:
        os.environ.pop("GEMINI_API_KEY", None)
        assistant.api_key = ""
        return {"status": "success", "message": "Reverted to Built-in Expert Engine."}
