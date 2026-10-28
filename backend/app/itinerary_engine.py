"""
TamilNadu TravelAI - Dynamic Itinerary Planning & Replanning Engine
Generates realistic, day-by-day structured itineraries with morning/afternoon/evening slots,
meal stops, realistic transit times, and supports dynamic conversational modifications.
"""

from typing import Dict, List, Any, Optional
from app.knowledge_base import get_destination_data, DESTINATIONS
from app.budget_calculator import calculate_trip_budget

def generate_structured_itinerary(
    destination_key: str,
    days: int = 2,
    preferences: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Creates a structured day-by-day travel plan with realistic time slots,
    transit durations, and local cultural meal stops.
    """
    prefs = preferences or {}
    dest_data = get_destination_data(destination_key) or DESTINATIONS.get("coimbatore")
    dest_name = dest_data["name"]
    
    # Flags from preferences / dynamic replanning
    is_budget = prefs.get("is_budget", False)
    is_relaxed = prefs.get("is_relaxed", False)
    no_temples = prefs.get("no_temples", False)
    rain_mode = prefs.get("rain_mode", False)
    child_friendly = prefs.get("child_friendly", False)
    food_focused = prefs.get("food_focused", False)

    attractions = dest_data.get("top_attractions", [])
    
    # Filter attractions according to preferences
    filtered_attractions = []
    for att in attractions:
        att_name = att["name"].lower()
        if no_temples and ("temple" in att_name or "kovil" in att_name or "shrine" in att_name):
            continue
        if rain_mode and ("falls" in att_name or "peak" in att_name or "lake" in att_name):
            # De-prioritize purely outdoor waterfalls in severe rain
            continue
        filtered_attractions.append(att)

    if not filtered_attractions:
        filtered_attractions = attractions

    # Group into days
    days_count = max(1, min(days, 5))
    itinerary_days: List[Dict[str, Any]] = []

    # Local dining suggestions
    specialties = dest_data.get("local_food", {}).get("specialties", ["Traditional Tamil Meals", "Filter Coffee"])
    eateries = dest_data.get("local_food", {}).get("iconic_eateries", ["Local Traditional Mess"])

    att_idx = 0
    total_att_count = len(filtered_attractions)

    for day_num in range(1, days_count + 1):
        # Pick 2-3 attractions per day depending on pace
        daily_capacity = 2 if is_relaxed else 3
        day_attractions = []
        for _ in range(daily_capacity):
            if att_idx < total_att_count:
                day_attractions.append(filtered_attractions[att_idx])
                att_idx += 1
            else:
                # Loop around or pick relaxed stroll
                break

        # Construct morning, afternoon, evening
        morn_att = day_attractions[0] if len(day_attractions) > 0 else filtered_attractions[0]
        aft_att = day_attractions[1] if len(day_attractions) > 1 else None
        eve_att = day_attractions[2] if len(day_attractions) > 2 else None

        breakfast_spot = eateries[0] if len(eateries) > 0 else "Local South Indian Tiffin Centre"
        lunch_spot = eateries[1] if len(eateries) > 1 else eateries[0]
        dinner_spot = eateries[2] if len(eateries) > 2 else eateries[-1]

        # Morning slot
        morning = {
            "time": "08:00 AM - 12:30 PM",
            "title": f"Morning Exploration: {morn_att['name']}",
            "activity": morn_att["experience"],
            "duration": morn_att["duration"],
            "entry_fee": morn_att["entry_fee"],
            "travel_transit": "20 - 35 mins from city center",
            "highlights": morn_att["highlights"]
        }

        # Afternoon slot
        if aft_att:
            afternoon = {
                "time": "02:00 PM - 05:00 PM",
                "title": f"Afternoon Sight: {aft_att['name']}",
                "activity": aft_att["experience"],
                "duration": aft_att["duration"],
                "entry_fee": aft_att["entry_fee"],
                "travel_transit": "15 - 25 mins transit from lunch spot",
                "highlights": aft_att["highlights"]
            }
        else:
            afternoon = {
                "time": "02:30 PM - 05:00 PM",
                "title": "Leisurely Cultural Walk & Local Handicrafts",
                "activity": f"Explore traditional spice markets and boutique handlooms in {dest_name}.",
                "duration": "2 hours",
                "entry_fee": "Free",
                "travel_transit": "Central walking zone",
                "highlights": "Direct interaction with local artisans"
            }

        # Evening slot
        if eve_att:
            evening = {
                "time": "05:30 PM - 08:30 PM",
                "title": f"Evening Sunset & Vibe: {eve_att['name']}",
                "activity": eve_att["experience"],
                "duration": eve_att["duration"],
                "entry_fee": eve_att["entry_fee"],
                "travel_transit": "20 mins transit",
                "highlights": eve_att["highlights"]
            }
        else:
            evening = {
                "time": "05:30 PM - 08:30 PM",
                "title": "Evening Stroll & Street Delicacies",
                "activity": f"Experience the gentle sunset breeze, promenade walk, and sample fresh {specialties[0]}.",
                "duration": "2.5 hours",
                "entry_fee": "Free",
                "travel_transit": "10 - 15 mins",
                "highlights": "Sunset panorama, evening lights, street food stalls"
            }

        # Suggested meals
        meals = {
            "breakfast": f"Hot tiffin at {breakfast_spot} (Try {specialties[0] if len(specialties) > 0 else 'Idli-Vada'})",
            "lunch": f"Traditional banana leaf thali at {lunch_spot} (Sample {specialties[1] if len(specialties) > 1 else 'Meals'})",
            "dinner": f"Dinner feast at {dinner_spot} (Don't miss {specialties[-1]})"
        }

        practical_notes = [
            f"Start Day {day_num} early at 8:00 AM to beat afternoon heat or tourist peak hours.",
            "Keep comfortable slip-on footwear handy for quick barefoot entry into monuments or temples.",
            f"Sample authentic local filter coffee or fresh tender coconut during midday breaks."
        ]
        if rain_mode:
            practical_notes.append("Carry compact umbrellas and light rain protection coats.")
        if child_friendly:
            practical_notes.append("Schedule ample rest stops between 1:00 PM - 2:30 PM for kids.")

        itinerary_days.append({
            "day": day_num,
            "theme": f"Day {day_num}: Cultural Heritage & Landscapes of {dest_name}",
            "morning": morning,
            "afternoon": afternoon,
            "evening": evening,
            "meals": meals,
            "practical_notes": practical_notes
        })

    # Calculate budget summary for this itinerary
    budget_tier = "budget" if is_budget else "mid_range"
    budget_summary = calculate_trip_budget(
        destination=dest_name,
        days=days_count,
        travellers=prefs.get("travellers", 2),
        travel_style=budget_tier,
        total_budget_limit=prefs.get("user_budget_limit")
    )

    return {
        "destination": dest_name,
        "district": dest_data["district"],
        "days_count": days_count,
        "preferences_applied": {
            "is_budget": is_budget,
            "is_relaxed": is_relaxed,
            "no_temples": no_temples,
            "rain_mode": rain_mode,
            "child_friendly": child_friendly,
            "food_focused": food_focused
        },
        "days": itinerary_days,
        "budget_summary": budget_summary,
        "travel_tips": dest_data.get("travel_tips", []),
        "emergency_contacts": dest_data.get("emergency_contacts", {})
    }
