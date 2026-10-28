# TamilNadu TravelAI — Intelligent Travel Assistant

> **A smart, conversational AI chatbot dedicated exclusively to travel, tourism, culture, food, routes, and trip planning across Tamil Nadu, India.**

---

## 🌟 Key Highlights & Features

1. **Strict 4-Tier Domain Guardrails**:
   - Exclusively answers Tamil Nadu travel and tourism queries.
   - Automatically intercepts and politely redirects out-of-scope queries (general coding, mathematics, medical diagnosis, politics, stock trading, homework, general chat).
   - Polite out-of-scope response:
     > *"I'm TamilNadu TravelAI, your dedicated Tamil Nadu travel assistant. I can help you explore destinations, plan trips, discover local food and culture, find travel routes, estimate budgets, and understand travel requirements across Tamil Nadu. What would you like to know about travelling in Tamil Nadu?"*
   - Gently redirects non-Tamil Nadu destination questions while providing relevant transit context if traveling to or from Tamil Nadu.

2. **Multilingual Intelligence (English, தமிழ், Tanglish)**:
   - Natural language comprehension in **English**, **Tamil (தமிழ் script)**, and **Tanglish (Romanized Tamil)**.
   - Preserves destination names, prices, and practical route details accurately.

3. **Rich Destination Database (32+ Hubs)**:
   - Covers Chennai, Coimbatore, Ooty, Coonoor, Kodaikanal, Madurai, Thanjavur, Trichy, Rameswaram, Kanyakumari, Tirunelveli, Courtallam, Thoothukudi, Dhanushkodi, Yercaud, Valparai, Mahabalipuram, Kanchipuram, Kumbakonam, Chettinad/Karaikudi, Hogenakkal, Tiruvannamalai, Mudumalai, and more.
   - Detailed attractions with verified entry fees, ideal duration, local cuisines, transport connectivity, seasonal best times, and emergency helplines.

4. **Dynamic AI & Deterministic Itinerary Engine**:
   - Day-by-day scheduling with Morning, Afternoon, Evening, and curated meal recommendations.
   - Conversational replanning commands:
     - *"Make it cheaper"*
     - *"Add local food"*
     - *"Remove temple visits"*
     - *"Make it more relaxed for parents"*
     - *"Adjust plan for rain"*

5. **Deterministic Budget Calculation**:
   - Deterministic arithmetic engine calculating realistic travel budgets across accommodation, intercity transport, local transit, food, attraction entry tickets, and contingency buffers.
   - User budget limit validation (within budget vs surplus/deficit).

6. **Real-Time Atmospheric Forecasts**:
   - Integrated with the **Open-Meteo live atmospheric API** for authentic live weather, temperature, precipitation probability, and attire recommendations for Tamil Nadu coordinates.

7. **Hybrid AI Engine**:
   - Connects to Google Gemini API (`GEMINI_API_KEY`) when configured.
   - Runs seamlessly out-of-the-box using the built-in Tamil Nadu Travel Reasoning Engine without requiring any paid API key.

---

## 🏗️ Technical Architecture

```
gen/
├── backend/
│   ├── app/
│   │   ├── main.py               # FastAPI server & endpoints
│   │   ├── domain_guardrail.py   # Multi-tier Tamil Nadu scope guardrail
│   │   ├── knowledge_base.py     # 32+ verified Tamil Nadu travel destinations
│   │   ├── itinerary_engine.py   # Structured day-by-day itinerary & replanner
│   │   ├── budget_calculator.py  # Deterministic travel budget engine
│   │   ├── live_weather.py       # Live Open-Meteo weather integration
│   │   ├── language_detector.py  # English, Tamil, and Tanglish classifier
│   │   └── llm_client.py         # Gemini LLM orchestrator & expert RAG engine
│   ├── tests/
│   │   └── test_domain_and_chat.py # Pytest suite (8 comprehensive tests)
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Header.tsx            # Navigation, branding & language toggle
│   │   │   ├── WelcomeHero.tsx       # Welcome message & 8 suggested prompts
│   │   │   ├── ChatMessage.tsx       # Markdown, cards, weather & budget tables
│   │   │   ├── ChatInput.tsx         # Auto-resizing input & quick modifier chips
│   │   │   ├── DestinationDrawer.tsx # 32+ destination catalog drawer
│   │   │   └── SettingsModal.tsx     # Engine status & Gemini key configuration
│   │   ├── types.ts                  # TypeScript definitions
│   │   ├── App.tsx                   # Main React conversation orchestrator
│   │   ├── index.css                 # Modern CSS & design tokens
│   │   └── main.tsx
│   ├── package.json
│   └── vite.config.ts                # Vite config with backend proxy
└── README.md
```

---

## 🚀 Quickstart & Run Instructions

### 1. Prerequisites
- **Python 3.10+** (Python 3.12 verified)
- **Node.js 18+** (Node v22 verified)

---

### 2. Backend Setup & Startup

```bash
# Navigate to backend directory
cd backend

# Install Python dependencies
pip install -r requirements.txt

# (Optional) Set your Gemini API key in .env or environment variable
# copy .env.example .env

# Run unit tests to verify domain guardrails and calculations
python -m pytest tests/test_domain_and_chat.py -v

# Start FastAPI backend server
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000
```
Backend API will be running at `http://127.0.0.1:8000` (API documentation at `http://127.0.0.1:8000/docs`).

---

### 3. Frontend Setup & Startup

```bash
# In a new terminal, navigate to frontend directory
cd frontend

# Install npm packages
npm install

# Start Vite dev server
npm run dev
```
Open `http://localhost:5173/` in your browser.

---

## 🧪 Testing Suite

Run the automated backend test suite:
```bash
python -m pytest backend/tests/test_domain_and_chat.py -v
```

Tests verify:
- ✅ **In-scope queries** (Coimbatore, Ooty, Madurai, Food, Temples, Routes)
- ✅ **Strict out-of-scope rejection** (Python coding, Stocks, Medical, Politics, Homework)
- ✅ **Out-of-state redirection** (Goa, Paris, etc. redirected to Tamil Nadu)
- ✅ **Transit questions involving outside locations** (Allowed: e.g. Mumbai to Chennai)
- ✅ **Language detection** (English, Tamil script, Tanglish)
- ✅ **Deterministic budget math** (Cost per person, nights, rooms, buffer)
- ✅ **Itinerary replanning** (Preferences like `no_temples`, `budget`, `relaxed`)
- ✅ **Knowledge base data integrity** (Districts, attractions, safety tips, emergency contacts)

---

## 💡 Example Conversation Journeys

1. **Destination Inquiry**:
   - *User:* "What are the best places to visit in Coimbatore?"
   - *AI:* Produces overview, Adiyogi, Marudhamalai, Siruvani, Kongu food spots, live weather, and follow-up prompts.

2. **Itinerary Planning**:
   - *User:* "I have two days in Coimbatore. Plan a trip for me."
   - *AI:* Returns structured Day 1 & Day 2 plans with morning, afternoon, evening slots, meal stops, transit times, and budget table.

3. **Dynamic Replanning**:
   - *User:* "Make it cheaper."
   - *AI:* Dynamically revises itinerary and budget breakdown without losing destination context.

4. **Tanglish Conversational Guide**:
   - *User:* "Coimbatore la family oda one day trip ku places sollunga."
   - *AI:* Responds naturally in Tanglish with family-friendly recommendations and timing sequence.

5. **Out-of-Scope Rejection**:
   - *User:* "Write a python script for binary search."
   - *AI:* Strictly rejects with the standardized domain response and redirects to Tamil Nadu travel.
