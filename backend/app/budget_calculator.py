"""
TamilNadu TravelAI - Deterministic Travel Budget Calculation Engine
Performs precise, deterministic arithmetic for trip expense breakdowns across
transport, accommodation, dining, attraction entry fees, local transit, and buffers.
"""

from typing import Dict, Any, Optional

def calculate_trip_budget(
    destination: str,
    days: int = 2,
    travellers: int = 1,
    travel_style: str = "mid_range",  # budget, mid_range, premium
    total_budget_limit: Optional[float] = None
) -> Dict[str, Any]:
    """
    Computes a deterministic cost estimate for a Tamil Nadu trip.
    """
    days = max(1, days)
    nights = max(1, days - 1)
    travellers = max(1, travellers)

    # Number of rooms assumption: 2 adults per room
    rooms = (travellers + 1) // 2

    # Cost benchmarks (INR) per travel style
    rates = {
        "budget": {
            "room_per_night": 1100,
            "intercity_transit_per_head": 450,  # TNSTC / Express Train Sleeper
            "local_transit_per_day": 200,       # City bus / shared autos
            "food_per_person_day": 400,        # Mess meals, idli/dosa, filter coffee
            "entry_and_activities_day": 150,   # Nominal temple / park entry
            "misc_buffer_pct": 0.08
        },
        "mid_range": {
            "room_per_night": 2800,
            "intercity_transit_per_head": 1200, # AC 3-tier train / AC Semi-sleeper bus
            "local_transit_per_day": 600,       # Cab sharing / auto fares
            "food_per_person_day": 850,        # Standard restaurants, specialty dining
            "entry_and_activities_day": 350,   # Boating, museums, camera fees, ropeway
            "misc_buffer_pct": 0.10
        },
        "premium": {
            "room_per_night": 6500,
            "intercity_transit_per_head": 2500, # Flight / Private dedicated AC sedan cab
            "local_transit_per_day": 1800,      # Dedicated private chauffeur cab
            "food_per_person_day": 1800,       # Heritage dining, resort restaurants
            "entry_and_activities_day": 800,   # VIP Darshan, speedboats, private tours
            "misc_buffer_pct": 0.12
        }
    }

    if travel_style == "budget" and total_budget_limit is not None and total_budget_limit <= 3500:
        style_cfg = {
            "room_per_night": 750,              # Clean budget lodge / hostel
            "intercity_transit_per_head": 250,  # Ordinary bus / passenger train
            "local_transit_per_day": 100,       # TNSTC city buses
            "food_per_person_day": 350,         # South Indian vegetarian mess & tiffin
            "entry_and_activities_day": 75,     # Nominal temple / museum entry
            "misc_buffer_pct": 0.05
        }
    else:
        style_cfg = rates.get(travel_style, rates["mid_range"])

    # Calculations
    accommodation_cost = rooms * nights * style_cfg["room_per_night"]
    intercity_transport_cost = travellers * style_cfg["intercity_transit_per_head"] * 2  # Round trip
    local_transport_cost = days * style_cfg["local_transit_per_day"] * ((travellers + 2) // 3)
    food_cost = travellers * days * style_cfg["food_per_person_day"]
    activities_cost = travellers * days * style_cfg["entry_and_activities_day"]

    subtotal = (
        accommodation_cost +
        intercity_transport_cost +
        local_transport_cost +
        food_cost +
        activities_cost
    )

    buffer_cost = round(subtotal * style_cfg["misc_buffer_pct"])
    total_estimated = subtotal + buffer_cost
    per_person_cost = round(total_estimated / travellers)

    remaining_budget = None
    is_within_budget = None
    if total_budget_limit is not None and total_budget_limit > 0:
        remaining_budget = round(total_budget_limit - total_estimated)
        is_within_budget = remaining_budget >= 0

    return {
        "destination": destination.title(),
        "days": days,
        "nights": nights,
        "travellers": travellers,
        "rooms": rooms,
        "travel_style": travel_style,
        "breakdown": {
            "accommodation": {
                "amount": accommodation_cost,
                "notes": f"₹{style_cfg['room_per_night']}/night × {nights} nights × {rooms} room(s)"
            },
            "intercity_transport": {
                "amount": intercity_transport_cost,
                "notes": f"Round-trip approx ₹{style_cfg['intercity_transit_per_head']} × {travellers} person(s)"
            },
            "local_transport": {
                "amount": local_transport_cost,
                "notes": f"Local taxis/autos/buses for {days} days"
            },
            "food_and_dining": {
                "amount": food_cost,
                "notes": f"Breakfast, lunch, dinner & coffee (₹{style_cfg['food_per_person_day']}/person/day)"
            },
            "activities_and_entry": {
                "amount": activities_cost,
                "notes": f"Attraction tickets, camera passes, boating/safari entry"
            },
            "emergency_buffer": {
                "amount": buffer_cost,
                "notes": f"{int(style_cfg['misc_buffer_pct']*100)}% contingency & local shopping"
            }
        },
        "total_estimated": total_estimated,
        "cost_per_person": per_person_cost,
        "user_budget_limit": total_budget_limit,
        "remaining_budget": remaining_budget,
        "is_within_budget": is_within_budget,
        "assumptions": [
            f"Trip duration: {days} days, {nights} night(s).",
            f"Party size: {travellers} traveller(s) accommodated in {rooms} room(s).",
            f"Tier: {travel_style.replace('_', ' ').title()} accommodation and dining standards.",
            "Prices are realistic seasonal estimates; transport fares may vary on festival peak weekends."
        ]
    }
