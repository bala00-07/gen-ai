"""
TamilNadu TravelAI - Live Real-Time Weather Integration
Fetches authentic real-time weather data for Tamil Nadu destinations using Open-Meteo API.
No fake or simulated data: if network fails, explicitly handles the error.
"""

import httpx
from typing import Dict, Any, Optional
from app.knowledge_base import DESTINATIONS, get_destination_data

# WMO Weather interpretation codes
WMO_CODES = {
    0: "Clear sky ☀️",
    1: "Mainly clear 🌤️",
    2: "Partly cloudy ⛅",
    3: "Overcast ☁️",
    45: "Foggy 🌫️",
    48: "Depositing rime fog 🌫️",
    51: "Light drizzle 🌧️",
    53: "Moderate drizzle 🌧️",
    55: "Dense drizzle 🌧️",
    61: "Slight rain 🌦️",
    63: "Moderate rain 🌧️",
    65: "Heavy rain ⛈️",
    80: "Slight rain showers 🌦️",
    81: "Moderate rain showers 🌧️",
    82: "Violent rain showers ⛈️",
    95: "Thunderstorm ⚡",
    96: "Thunderstorm with slight hail ⛈️",
    99: "Thunderstorm with heavy hail ⛈️",
}

async def fetch_live_weather(dest_key: str) -> Optional[Dict[str, Any]]:
    """
    Fetches real-time live weather using Open-Meteo for the destination coordinates.
    """
    dest = get_destination_data(dest_key)
    if not dest:
        return None

    lat = dest.get("lat")
    lon = dest.get("lon")
    if not lat or not lon:
        return None

    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}"
        f"&current=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,weather_code,wind_speed_10m"
        f"&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max"
        f"&timezone=Asia%2FKolkata"
    )

    try:
        async with httpx.AsyncClient(timeout=4.0) as client:
            resp = await client.get(url)
            if resp.status_code == 200:
                data = resp.json()
                current = data.get("current", {})
                daily = data.get("daily", {})
                wcode = current.get("weather_code", 0)
                condition = WMO_CODES.get(wcode, "Pleasant")

                temp = current.get("temperature_2m")
                feels_like = current.get("apparent_temperature")
                humidity = current.get("relative_humidity_2m")
                wind = current.get("wind_speed_10m")
                
                max_temp = daily.get("temperature_2m_max", [temp])[0] if daily.get("temperature_2m_max") else temp
                min_temp = daily.get("temperature_2m_min", [temp])[0] if daily.get("temperature_2m_min") else temp
                rain_prob = daily.get("precipitation_probability_max", [0])[0] if daily.get("precipitation_probability_max") else 0

                # Formulate travel attire and activity recommendation
                advice = []
                if temp is not None and temp < 16:
                    advice.append("Cool mountain weather! Carry light woollens, jackets, and thermal wear.")
                elif temp is not None and temp > 33:
                    advice.append("Warm and sunny! Wear breathable light cottons, carry sunscreen, sunglasses, and stay hydrated.")
                else:
                    advice.append("Pleasant outdoor sightseeing conditions! Comfortable cotton or casual wear is ideal.")

                if rain_prob > 40:
                    advice.append(f"Rain likelihood is {rain_prob}%. Carry an umbrella or waterproof jacket.")

                return {
                    "destination": dest["name"],
                    "district": dest["district"],
                    "temperature_c": temp,
                    "feels_like_c": feels_like,
                    "condition": condition,
                    "humidity_pct": humidity,
                    "wind_speed_kmh": wind,
                    "forecast_max_c": max_temp,
                    "forecast_min_c": min_temp,
                    "rain_probability_pct": rain_prob,
                    "travel_advice": " ".join(advice),
                    "source": "Live Open-Meteo Atmospheric Forecast (Asia/Kolkata)"
                }
    except Exception as e:
        # Gracefully handle network/API absence without hallucinating
        return None
