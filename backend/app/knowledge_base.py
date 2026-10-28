"""
TamilNadu TravelAI - Comprehensive Tamil Nadu Travel Knowledge Base
Contains detailed, verified facts on ALL 38 DISTRICTS across Tamil Nadu.
"""

from typing import Dict, List, Optional, Any

DESTINATIONS: Dict[str, Dict[str, Any]] = {
    "ariyalur": {
        "name": "Ariyalur",
        "district": "Ariyalur",
        "category": "UNESCO Chola Capital & Fossil Heritage",
        "tagline": "The Land of Great Chola Rajendra I & Cretaceous Fossils",
        "lat": 11.1398,
        "lon": 79.0768,
        "overview": "Ariyalur is famous for the monumental Gangaikonda Cholapuram temple built by Emperor Rajendra Chola I to celebrate his victorious expedition to the Ganges. The district is also an internationally recognized geological wonder containing million-year-old marine fossils, dinosaur eggs, and Cretaceous limestone quarries.",
        "ideal_duration": "1 to 2 days",
        "best_season": "October to March (Mild weather, 20°C - 30°C)",
        "weather_notes": "Summers are dry and warm. Best visited during early mornings or late afternoons.",
        "top_attractions": [
            {
                "name": "Brihadisvara Temple, Gangaikonda Cholapuram (UNESCO)",
                "experience": "11th-century architectural masterpiece built by Rajendra Chola I, featuring a concave 55-meter Vimana, giant Nandi, and the monumental lion-faced well (Simhakinaru).",
                "duration": "2.5 hours",
                "entry_fee": "Free; UNESCO World Heritage Monument",
                "highlights": "Dancing Nataraja sculptures, Saraswathi idol, historic Cholagangam sacred lake (Ponneri)"
            },
            {
                "name": "Varanavasi Fossil Site & Geological Museum",
                "experience": "Ancient paleontological discovery zone containing fossilized marine invertebrates, gastropods, ammonites, and plant fossils dating back over 65 million years.",
                "duration": "1.5 hours",
                "entry_fee": "Free",
                "highlights": "Hands-on fossil stone exhibits, prehistoric ocean bed evidence"
            },
            {
                "name": "Karaivetti Bird Sanctuary",
                "experience": "One of the largest inland bird sanctuaries in Tamil Nadu, hosting thousands of migratory bar-headed geese, pelicans, and painted storks during winter.",
                "duration": "2 hours",
                "entry_fee": "Free / Camera ₹25",
                "highlights": "Watchtowers, serene winter wetlands, exotic migratory waterbirds"
            }
        ],
        "local_food": {
            "specialties": ["Ariyalur Cashew nut sweets & roasted cashews", "Traditional Delta Banana leaf meals with country vegetable kootu", "Thirumanur special murukku"],
            "iconic_eateries": ["Hotel Gangai (Jayamkondam)", "Sri Balaji Bhavan (Ariyalur)", "New Trichy Mess"]
        },
        "transport": {
            "railway": "Ariyalur Railway Station (ALU) - Key mainline railhead connected with Chennai, Trichy, and Madurai",
            "road": "Well connected to Trichy (65 km), Thanjavur (45 km), and Kumbakonam (35 km)",
            "airport": "Trichy International Airport (75 km)"
        },
        "accommodation": {
            "budget": "₹800 - ₹1,400 / night (Ariyalur town or Jayamkondam)",
            "mid_range": "₹2,000 - ₹3,500 / night (Many visitors stay in Kumbakonam or Thanjavur nearby)"
        },
        "estimated_budget_per_day": "₹1,000 - ₹2,000 per person",
        "travel_tips": [
            "Combine Gangaikonda Cholapuram with Kumbakonam or Thanjavur for a complete Great Living Chola Temples UNESCO circuit.",
            "Winter (Dec-Feb) is ideal to combine the temple visit with migratory birdwatching at Karaivetti Sanctuary."
        ],
        "emergency_contacts": {"police": "100", "ambulance": "108"}
    },

    "chengalpattu": {
        "name": "Chengalpattu",
        "district": "Chengalpattu",
        "category": "Coastal Heritage & Eco Lagoons",
        "tagline": "Gateway to Pallava Wonders & Bird Sanctuaries",
        "lat": 12.6841,
        "lon": 79.9836,
        "overview": "Carved out of Kanchipuram district, Chengalpattu spans the scenic East Coast Road (ECR), the world-famous UNESCO rock reliefs of Mahabalipuram, the tranquil Vedanthangal Bird Sanctuary, and the golden shores of Kovalam and Muttukadu backwaters.",
        "ideal_duration": "2 days",
        "best_season": "October to March (Pleasant coastal breezes, 21°C - 30°C)",
        "weather_notes": "Summers are warm; breezy coastal evenings along the Bay of Bengal.",
        "top_attractions": [
            {
                "name": "Mahabalipuram Monuments (UNESCO)",
                "experience": "7th-century rock-cut monolithic Rathas, Shore Temple facing the ocean, Arjuna's Penance, and Krishna's Butterball.",
                "duration": "3-4 hours",
                "entry_fee": "₹40 for Indians, ₹600 for foreigners",
                "highlights": "Oceanfront Shore Temple, granite chariot monoliths"
            },
            {
                "name": "Vedanthangal Bird Sanctuary",
                "experience": "India's oldest water bird sanctuary (dating back to 1798), home to over 40,000 migratory herons, spoonbills, and egrets in Barringtonia trees.",
                "duration": "2 hours",
                "entry_fee": "₹25 for adults, ₹5 for children",
                "highlights": "Spectacular bird nesting in winter, telescope towers"
            },
            {
                "name": "Muttukadu & Kovalam (Covelong) Beach",
                "experience": "Windsurfing and surfing school hub, speed-boating in backwaters, and pristine sandy beaches.",
                "duration": "2 hours",
                "entry_fee": "Free beach; Boating ₹200 - ₹500",
                "highlights": "Surfing lessons, kayaking, scenic ECR drive"
            }
        ],
        "local_food": {
            "specialties": ["Fresh seashore grilled fish & jumbo prawns", "Chengalpattu roadside tender coconuts", "Traditional South Indian tiffin & filter coffee"],
            "iconic_eateries": ["Moonrakers (Mahabalipuram)", "Hotel Arya Bhavan (Chengalpattu)", "Sangeetha Veg on ECR"]
        },
        "transport": {
            "railway": "Chengalpattu Junction (CGL) - Major junction connecting southern Tamil Nadu to Chennai",
            "airport": "Chennai International Airport (35 km)",
            "road": "Connected directly by GST Road (NH 45) and scenic East Coast Road (ECR)"
        },
        "accommodation": {
            "budget": "₹900 - ₹1,800 / night",
            "mid_range": "₹2,500 - ₹5,000 / night (Beach resorts on ECR)",
            "luxury": "₹7,000 - ₹18,000+ / night (Radisson Blu Temple Bay, InterContinental)"
        },
        "estimated_budget_per_day": "₹1,400 - ₹3,000 per person",
        "travel_tips": ["Visit Vedanthangal between November and February for peak migratory bird nesting season."],
        "emergency_contacts": {"police": "100", "ambulance": "108"}
    },

    "chennai": {
        "name": "Chennai",
        "district": "Chennai",
        "category": "Metropolitan & Cultural Capital",
        "tagline": "Gateway to South India & Cultural Capital of Tamil Nadu",
        "lat": 13.0827,
        "lon": 80.2707,
        "overview": "Chennai, the bustling capital of Tamil Nadu on the Coromandel Coast, blends 400-year-old colonial heritage, classical Carnatic music and Bharatanatyam arts, iconic Dravidian temples, and the second longest natural urban beach in the world.",
        "ideal_duration": "2 to 3 days",
        "best_season": "November to February (Pleasant winter, 20°C - 28°C)",
        "weather_notes": "Summers are warm and humid. Northeast monsoon brings rain in Oct-Nov.",
        "top_attractions": [
            {
                "name": "Marina Beach & Lighthouse",
                "experience": "Second-longest natural urban beach in the world with historic statues and panoramic bay-view lighthouse.",
                "duration": "2-3 hours",
                "entry_fee": "Free; Lighthouse ₹20",
                "highlights": "Evening breeze, sundal & crispy fish fry stalls"
            },
            {
                "name": "Kapaleeshwarar Temple, Mylapore",
                "experience": "7th-century classic Dravidian temple dedicated to Lord Shiva with an ornate rainbow gopuram.",
                "duration": "1.5 hours",
                "entry_fee": "Free",
                "highlights": "Gopuram sculptures, sacred Punnai tree, Mylapore cultural heritage"
            },
            {
                "name": "San Thome Basilica",
                "experience": "Neo-Gothic cathedral built over the tomb of St. Thomas the Apostle.",
                "duration": "1 hour",
                "entry_fee": "Free",
                "highlights": "Underground museum, serene prayer chapel"
            },
            {
                "name": "Fort St. George & Museum",
                "experience": "First British fortress in India (1644) featuring St. Mary's Church and colonial artifacts.",
                "duration": "2 hours",
                "entry_fee": "₹25 for Indians, ₹300 for foreigners",
                "highlights": "Historic weaponry, coins, colonial paintings"
            }
        ],
        "local_food": {
            "specialties": ["Chennai Degree Filter Coffee", "Ghee Podi Idli & Medu Vada", "Marina Beach Sundal", "Chettinad Banana Leaf Meals"],
            "iconic_eateries": ["Murugan Idli Shop", "Saravana Bhavan (Mylapore)", "Rayar's Mess", "Ratna Cafe (Triplicane)"]
        },
        "transport": {
            "airport": "Chennai International Airport (MAA) at Meenambakkam",
            "railway": "Chennai Central (MAS) & Chennai Egmore (MS)",
            "local_travel": "Chennai Metro, Suburban Electric Trains, MTC Buses, OLA/Uber"
        },
        "accommodation": {
            "budget": "₹900 - ₹1,600 / night",
            "mid_range": "₹2,200 - ₹4,500 / night",
            "luxury": "₹5,500 - ₹15,000+ / night (ITC Grand Chola, Taj Coromandel)"
        },
        "estimated_budget_per_day": "₹1,200 - ₹2,500 per person",
        "travel_tips": ["Take the Chennai Metro directly from the airport to Central or Anna Salai for a fast, air-conditioned transfer."],
        "emergency_contacts": {"police": "100", "ambulance": "108", "tourist_helpline": "044-25333333"}
    },

    "coimbatore": {
        "name": "Coimbatore",
        "district": "Coimbatore",
        "category": "Western Ghats Foothills & Heritage",
        "tagline": "Manchester of South India & Gateway to the Nilgiris",
        "lat": 11.0168,
        "lon": 76.9558,
        "overview": "Nestled at the foot of the Nilgiri Hills, Coimbatore is famed for its pleasant year-round climate, world-renowned Siruvani drinking water, textile heritage, and rich Kongu Nadu culinary traditions.",
        "ideal_duration": "1 to 2 days",
        "best_season": "October to March (Mild cool breeze, 18°C - 30°C)",
        "weather_notes": "Pleasant evenings year-round thanks to Palakkad gap winds.",
        "top_attractions": [
            {
                "name": "Isha Yoga Centre & Adiyogi Shiva Statue",
                "experience": "Guinness Record 112-foot bust of Adiyogi Shiva, Dhyanalinga meditative dome, and evening 3D projection show.",
                "duration": "3-4 hours",
                "entry_fee": "Free",
                "highlights": "Dhyanalinga silence meditation, Adiyogi Divya Darshanam light show"
            },
            {
                "name": "Marudhamalai Murugan Hill Temple",
                "experience": "1200-year-old hilltop shrine surrounded by medicinal herbal flora and scenic Western Ghats views.",
                "duration": "2 hours",
                "entry_fee": "Free; Special Darshan ₹20 - ₹100",
                "highlights": "Paambatti Siddhar cave, holy spring, valley panorama"
            },
            {
                "name": "Siruvani Waterfalls & Dam",
                "experience": "Source of Siruvani water, reputed as the second sweetest natural water in the world.",
                "duration": "Half day",
                "entry_fee": "Forest entry ₹50",
                "highlights": "Crystal clear water, pristine rainforest trek"
            }
        ],
        "local_food": {
            "specialties": ["Kongu Nadu Chicken & Mutton Chinthamani", "Annapoorna Ghee Sambar Mini Idli", "Pallipalayam Chicken", "Siruvani Tap Filter Coffee", "Elaneer Payasam"],
            "iconic_eateries": ["Sree Annapoorna (RS Puram)", "Hari Bhavanam", "Junior Kuppanna", "Velan Mess"]
        },
        "transport": {
            "airport": "Coimbatore International Airport (CJB) at Peelamedu",
            "railway": "Coimbatore Junction (CBE)",
            "bus": "Gandhipuram, Singanallur, Ukkadam Central Bus stands"
        },
        "accommodation": {
            "budget": "₹800 - ₹1,500 / night",
            "mid_range": "₹2,000 - ₹4,000 / night",
            "luxury": "₹4,500 - ₹9,000+ / night (The Residency Towers, Vivanta)"
        },
        "estimated_budget_per_day": "₹1,000 - ₹2,200 per person",
        "travel_tips": ["Coimbatore is the primary transit gateway to Ooty (85 km) and Valparai (105 km)."],
        "emergency_contacts": {"police": "100", "ambulance": "108"}
    },

    "cuddalore": {
        "name": "Cuddalore",
        "district": "Cuddalore",
        "category": "Mangrove Wetlands, Ancient Temples & Coast",
        "tagline": "Land of Silver Beach, Nataraja Sanctum & Mangrove Canals",
        "lat": 11.7480,
        "lon": 79.7714,
        "overview": "Cuddalore district extends from the sacred cosmic dance stage of Chidambaram Nataraja Temple to the world's second-largest mangrove forest at Pichavaram and the wide expanse of Silver Beach.",
        "ideal_duration": "1 to 2 days",
        "best_season": "October to March (21°C - 30°C)",
        "weather_notes": "Comfortable winter coastal climate.",
        "top_attractions": [
            {
                "name": "Pichavaram Mangrove Forest",
                "experience": "World's second largest mangrove forest spread over 1,100 hectares with 4,400 interconnected water canals navigated by wooden rowboats.",
                "duration": "2 hours",
                "entry_fee": "Rowboat ₹400 - ₹800",
                "highlights": "Gliding under natural mangrove stilt root arches, birdwatching"
            },
            {
                "name": "Thillai Nataraja Temple, Chidambaram",
                "experience": "Ancient temple representing Space (Akasha) in the Pancha Bhoota Sthalams, where Lord Shiva performs the cosmic Ananda Tandava dance.",
                "duration": "2 hours",
                "entry_fee": "Free",
                "highlights": "Golden Roof (Pon Ambalam), Chidambara Rahasyam, 108 Bharatanatyam postures"
            },
            {
                "name": "Silver Beach, Devanampattinam",
                "experience": "One of the longest beaches in Asia, peaceful and uncrowded with historic British Fort St. David nearby.",
                "duration": "1.5 hours",
                "entry_fee": "Free",
                "highlights": "Sunset walks, coastal sea breeze, boat rides"
            }
        ],
        "local_food": {
            "specialties": ["Fresh lagoon crab curry & mangrove tiger prawns", "Chidambaram Ghost Parotta", "Temple Prasadam Puliyodharai"],
            "iconic_eateries": ["Hotel Krishna (Chidambaram)", "Sri Radha Bhavan", "Beach shacks at Silver Beach"]
        },
        "transport": {
            "railway": "Cuddalore Port Junction (CUPJ) & Chidambaram Railway Station (CDM)",
            "road": "Well connected to Pondicherry (22 km), Chennai (180 km via ECR)",
            "airport": "Pondicherry Airport (25 km) or Chennai (180 km)"
        },
        "accommodation": {
            "budget": "₹800 - ₹1,400 / night (Chidambaram or Cuddalore)",
            "mid_range": "₹2,000 - ₹3,800 / night"
        },
        "estimated_budget_per_day": "₹1,000 - ₹2,200 per person",
        "travel_tips": ["Choose a manual paddle rowboat over a motorboat at Pichavaram to explore the narrowest, most scenic canopy tunnels."],
        "emergency_contacts": {"police": "100", "ambulance": "108"}
    },

    "dharmapuri": {
        "name": "Dharmapuri",
        "district": "Dharmapuri",
        "category": "River Canyons, Coracles & Waterfalls",
        "tagline": "The Land of Smoky Waterfalls & Ancient Kaveri Gorges",
        "lat": 12.1211,
        "lon": 78.1582,
        "overview": "Dharmapuri is home to Hogenakkal Falls ('The Niagara of India') on the Kaveri River, ancient rock-cut cave temples, and the serene hill village of Vathalmalai.",
        "ideal_duration": "1 to 2 days",
        "best_season": "October to March (Moderate river flow, 20°C - 30°C)",
        "weather_notes": "July-August monsoon increases Kaveri water volume tremendously.",
        "top_attractions": [
            {
                "name": "Hogenakkal Waterfalls & Coracle Boating",
                "experience": "Round basket bamboo boat rides through carbonatite rock canyons directly beneath roaring waterfalls.",
                "duration": "2-3 hours",
                "entry_fee": "Regulated coracle ₹750 (fits 4-5)",
                "highlights": "Spinning coracle under misty falls, fresh river fish fry"
            },
            {
                "name": "Theerthamalai Temple",
                "experience": "Ancient hilltop Shiva shrine with five sacred water springs believed to have been created by Lord Rama.",
                "duration": "2 hours",
                "entry_fee": "Free",
                "highlights": "Medicinal spring water, hilltop forest panoramic views"
            },
            {
                "name": "Vathalmalai Hill Station",
                "experience": "Less-crowded tribal hill station at 1,400 meters with coffee plantations and scenic hairpin bends.",
                "duration": "Half day",
                "entry_fee": "Free",
                "highlights": "Offbeat cool breeze, coffee gardens, scenic valley view"
            }
        ],
        "local_food": {
            "specialties": ["Fresh caught Kaveri river fish (Katla, Rohu) marinated in village spices", "Naatu Kozhi Kulambu (Country chicken curry)", "Ragi mudde"],
            "iconic_eateries": ["Hogenakkal riverfront fish stalls", "Hotel TamilNadu TTDC Restaurant", "Sri Saravana Bhavan Dharmapuri"]
        },
        "transport": {
            "railway": "Dharmapuri Railway Station (DPJ) on Bangalore-Salem line",
            "road": "NH 44 connects to Bangalore (130 km) and Salem (65 km)"
        },
        "accommodation": {
            "budget": "₹800 - ₹1,400 / night (TTDC Hotel TamilNadu Hogenakkal or Dharmapuri)",
            "mid_range": "₹2,000 - ₹3,500 / night"
        },
        "estimated_budget_per_day": "₹1,200 - ₹2,200 per person",
        "travel_tips": ["Always wear the provided life jacket while riding the bamboo coracle boat."],
        "emergency_contacts": {"police": "100", "ambulance": "108"}
    },

    "dindigul": {
        "name": "Dindigul",
        "district": "Dindigul",
        "category": "Princess of Hills, Rock Fort & Biryani Capital",
        "tagline": "Cradle of Kodaikanal, Historic Rock Fort & Seeraga Samba Biryani",
        "lat": 10.3673,
        "lon": 77.9803,
        "overview": "Dindigul district encompasses the world-famous hill station of Kodaikanal, the 17th-century Dindigul Rock Fort built by Madurai Nayaks, the sacred pilgrimage hill of Palani Murugan temple, and the legendary Dindigul Thalappakatti biryani.",
        "ideal_duration": "2 to 3 days",
        "best_season": "October to June (Pleasant weather in hills and plains)",
        "weather_notes": "Kodaikanal stays cool (12°C - 20°C); plains are warm in summer.",
        "top_attractions": [
            {
                "name": "Kodaikanal Lake & Coaker's Walk",
                "experience": "60-acre star-shaped mountain lake surrounded by pine forests, with cycling and pedal boating.",
                "duration": "2-3 hours",
                "entry_fee": "Free lake; Boating ₹200 - ₹450",
                "highlights": "Tandem cycling, valley cloud views from Coaker's Walk"
            },
            {
                "name": "Palani Murugan Temple (Arulmigu Dhandayuthapani Swamy)",
                "experience": "One of the Six Abodes (Arupadaiveedu) of Lord Murugan, crowned atop Sivagiri hill and reached via 693 stone steps, ropeway, or winch train.",
                "duration": "2-3 hours",
                "entry_fee": "Free; Ropeway/Winch ₹30 - ₹50; Special Darshan ₹100",
                "highlights": "Navapashanam consecrated idol by Siddhar Bogar, famous Panchamirtham prasadam"
            },
            {
                "name": "Dindigul Rock Fort (Malai Kottai)",
                "experience": "Massive 280-foot monolithic rock fortress built by Muthu Krishnappa Nayak in 1605, featuring ancient cannons and 360-degree city views.",
                "duration": "1.5 hours",
                "entry_fee": "₹25 for ASI",
                "highlights": "Historic brick bastions, artillery rooms, climbing ancient rock steps"
            }
        ],
        "local_food": {
            "specialties": ["Original Dindigul Thalappakatti Mutton Biryani (Seeraga samba rice & tender meat)", "Palani Panchamirtham (GI-tagged sacred 5-ingredient fruit confection)", "Kodaikanal artisan homemade chocolates"],
            "iconic_eateries": ["Dindigul Thalappakatti (Original branch since 1957)", "Venu Biriyani", "Ponram Biriyani", "Pastry Corner Kodai"]
        },
        "transport": {
            "railway": "Dindigul Junction (DG) & Kodai Road (KQN)",
            "road": "Centrally connected via NH 44 and NH 83 to Madurai (65 km) and Trichy (100 km)",
            "airport": "Madurai Airport (70 km)"
        },
        "accommodation": {
            "budget": "₹900 - ₹1,600 / night (Dindigul plains or Kodai town)",
            "mid_range": "₹2,500 - ₹5,000 / night (Kodai lakeview resorts)",
            "luxury": "₹6,500 - ₹16,000+ / night (The Carlton Kodaikanal, Tamara)"
        },
        "estimated_budget_per_day": "₹1,400 - ₹2,800 per person",
        "travel_tips": ["Taste genuine GI-tagged Palani Panchamirtham available at official Devasthanam counters on the hill."],
        "emergency_contacts": {"police": "100", "ambulance": "108"}
    },

    "erode": {
        "name": "Erode",
        "district": "Erode",
        "category": "Cauvery River Confluence, Textile & Turmeric Hub",
        "tagline": "The Turmeric City & Confluence of Sacred Rivers",
        "lat": 11.3410,
        "lon": 77.7172,
        "overview": "Erode is nestled on the fertile banks of the Cauvery and Bhavani rivers. Celebrated as the 'Turmeric City' and handloom textile capital, it features the sacred Triveni confluence at Bhavani Kooduthurai, the Kodiveri Dam cascade, and the Bannari Amman forest temple.",
        "ideal_duration": "1 to 2 days",
        "best_season": "October to March (21°C - 31°C)",
        "weather_notes": "Comfortable winter climate; agricultural greenery throughout.",
        "top_attractions": [
            {
                "name": "Bhavani Sangameshwarar Temple (Kooduthurai)",
                "experience": "The 'Triveni Sangam of South India' where the Cauvery, Bhavani, and the invisible subterranean Amutha rivers merge.",
                "duration": "2 hours",
                "entry_fee": "Free",
                "highlights": "River confluence bath, ancient Chola stone shrines"
            },
            {
                "name": "Kodiveri Dam & Waterfalls",
                "experience": "Scenic stepped masonry dam built across the Bhavani River in the 17th century, creating a wide cascading curtain of water safe for family bathing.",
                "duration": "2 hours",
                "entry_fee": "₹10 per adult",
                "highlights": "Splashing in safe river cascades, coracle rides, park"
            },
            {
                "name": "Bannari Amman Temple, Sathyamangalam",
                "experience": "Renowned forest shrine dedicated to Goddess Mariamman situated at the foot of Western Ghats forest ranges.",
                "duration": "1.5 hours",
                "entry_fee": "Free",
                "highlights": "Kundam (fire-walking) annual festival, peaceful forest aura"
            },
            {
                "name": "Chennimalai Murugan Temple & Handloom Weaving",
                "experience": "Hill temple reached via 1320 steps or ghat road, famous for the world-renowned Chennimalai handwoven cotton bedspreads and sarees.",
                "duration": "2 hours",
                "entry_fee": "Free",
                "highlights": "Hilltop breeze, shopping authentic handloom bedspreads"
            }
        ],
        "local_food": {
            "specialties": ["Kongu Nadu Pallipalayam Chicken (cooked without water using shallots and red chilies)", "Erode Halwa & Butter Bun", "Tender Coconut Kheer", "Kongu style parotta & salna"],
            "iconic_eateries": ["Hotel Sivaranjani", "Junior Kuppanna (Original Erode)", "Thottathu Virundhu", "Erode Saravana Bhavan"]
        },
        "transport": {
            "railway": "Erode Junction (ED) - Major A1 category junction connecting North, South, East, and West India",
            "airport": "Coimbatore Airport (80 km)",
            "road": "Well connected via NH 544 (Salem - Coimbatore highway)"
        },
        "accommodation": {
            "budget": "₹800 - ₹1,400 / night",
            "mid_range": "₹2,000 - ₹3,800 / night"
        },
        "estimated_budget_per_day": "₹1,000 - ₹2,000 per person",
        "travel_tips": ["Buy authentic GI-tagged Bhavani Jamakkalam (traditional heavy carpets) and Chennimalai handlooms directly from cooperative weavers."],
        "emergency_contacts": {"police": "100", "ambulance": "108"}
    },

    "kallakurichi": {
        "name": "Kallakurichi",
        "district": "Kallakurichi",
        "category": "Forested Hills, Waterfalls & Tribal Culture",
        "tagline": "The Green Gateway to Kalvarayan Hills & Scenic Falls",
        "lat": 11.7384,
        "lon": 78.9639,
        "overview": "Kallakurichi is a lush agricultural and forested district nestled against the Eastern Ghats. It is famed for the unspoiled Kalvarayan Hills, the gushing Megam and Periyar waterfalls, Gomukhi Dam reservoir, and serene tribal settlements.",
        "ideal_duration": "1 to 2 days",
        "best_season": "October to February (Post-monsoon greenery & cool breeze, 19°C - 29°C)",
        "weather_notes": "Pleasant monsoon and winter climate; waterfalls flow vigorously post-monsoon.",
        "top_attractions": [
            {
                "name": "Kalvarayan Hills",
                "experience": "Part of the Eastern Ghats rising up to 1,000 meters, featuring dense forests, scenic viewpoints, and peaceful cool weather.",
                "duration": "Full day excursion",
                "entry_fee": "Free",
                "highlights": "Winding mountain roads, tribal culture, untouched nature"
            },
            {
                "name": "Megam Falls & Periyar Falls",
                "experience": "Twin natural cascades tucked inside the forested valleys of Kalvarayan hills dropping over rocky ledges into clear pools.",
                "duration": "2 hours",
                "entry_fee": "Free",
                "highlights": "Forest trekking, natural outdoor freshwater bathing"
            },
            {
                "name": "Gomukhi Dam",
                "experience": "Picturesque reservoir constructed at the foothills of Kalvarayan hills with botanical gardens and boating.",
                "duration": "1.5 hours",
                "entry_fee": "Free; Park ₹10",
                "highlights": "Picnic spot, sunset view of hill backdrop"
            }
        ],
        "local_food": {
            "specialties": ["Fresh organic country vegetables and tapioca", "Traditional village millets (Kambu Koozh & Ragi Kali)", "Local Salem-style crispy parotta"],
            "iconic_eateries": ["Sri Saravana Bhavan Kallakurichi", "Highway mess on NH 79"]
        },
        "transport": {
            "railway": "Chinnasalem Railway Station (15 km) on Salem-Vridhachalam line",
            "road": "Located directly on NH 79 (Salem - Ulundurpet highway)",
            "airport": "Trichy Airport (110 km) or Salem Airport (90 km)"
        },
        "accommodation": {
            "budget": "₹800 - ₹1,400 / night (Kallakurichi town lodges)"
        },
        "estimated_budget_per_day": "₹900 - ₹1,800 per person",
        "travel_tips": ["Kalvarayan hills offer a very quiet, offbeat hill-station alternative without the heavy tourist commercialization of major hill towns."],
        "emergency_contacts": {"police": "100", "ambulance": "108"}
    },

    "kancheepuram": {
        "name": "Kancheepuram (Kanchipuram)",
        "district": "Kancheepuram",
        "category": "City of Thousand Temples & Silk Capital",
        "tagline": "The Golden City of Ancient Sanctuaries & Pure Mulberry Silk",
        "lat": 12.8342,
        "lon": 79.7036,
        "overview": "Kanchipuram is one of India's seven sacred pilgrimage cities (Sapta Puri) and was the grand royal capital of the Pallava dynasty. Renowned for spectacular 7th-century Dravidian sandstone temples and world-famous handwoven Kanchipuram pure silk sarees.",
        "ideal_duration": "1 to 2 days",
        "best_season": "October to March (20°C - 30°C)",
        "weather_notes": "Summers are warm; pleasant winter mornings.",
        "top_attractions": [
            {
                "name": "Kailasanathar Temple",
                "experience": "The oldest structural sandstone temple in Kanchipuram built in 700 CE by Pallava King Rajasimha, featuring 58 small circumambulatory shrines.",
                "duration": "1.5 hours",
                "entry_fee": "Free",
                "highlights": "Sandstone circumambulatory tunnel symbolizing rebirth, Somaskanda sculptures"
            },
            {
                "name": "Ekambareswarar Temple",
                "experience": "Pancha Bhoota Sthalam for the Earth element (Prithvi Lingam) with a massive 59-meter gopuram and a sacred 3,500-year-old mango tree.",
                "duration": "2 hours",
                "entry_fee": "Free",
                "highlights": "Earth Lingam, sacred 4-mango tree, 1000-pillar hall"
            },
            {
                "name": "Kanchi Kamakshi Amman Temple",
                "experience": "One of the 51 Shakti Peethas with the sacred Sri Chakra consecrated by Adi Shankaracharya.",
                "duration": "1.5 hours",
                "entry_fee": "Free",
                "highlights": "Golden vimana, Sri Chakra worship, peaceful sanctum"
            },
            {
                "name": "Silk Weaving Cooperative Societies",
                "experience": "Watch master weavers crafting pure mulberry silk sarees with heavy gold zari on traditional Jacquard handlooms.",
                "duration": "1.5 hours",
                "entry_fee": "Free",
                "highlights": "Live handloom demo, purchasing Silk Mark certified sarees"
            }
        ],
        "local_food": {
            "specialties": ["Authentic Kanchipuram Kovil Idli (steamed in mandharai leaves with pepper and cumin)", "Traditional banana leaf meals", "Pure South Indian filter coffee"],
            "iconic_eateries": ["Sri Krishna Sweets", "Hotel Saravana Bhavan (Gandhi Road)", "Upashana Hotel"]
        },
        "transport": {
            "railway": "Kanchipuram Railway Station (CJ)",
            "road": "Smooth 6-lane NH 48 from Chennai (75 km / 1.5 hours)",
            "airport": "Chennai International Airport (65 km)"
        },
        "accommodation": {
            "budget": "₹800 - ₹1,400 / night",
            "mid_range": "₹2,000 - ₹4,000 / night (Regency Kanchipuram by GRT, MM Hotels)"
        },
        "estimated_budget_per_day": "₹1,000 - ₹2,000 per person",
        "travel_tips": ["Buy silk sarees directly from certified cooperative societies (Co-optex or Kamakshi Weavers Co-op) to avoid middlemen commissions."],
        "emergency_contacts": {"police": "100", "ambulance": "108"}
    },

    "kanniyakumari": {
        "name": "Kanniyakumari (Kanyakumari)",
        "district": "Kanniyakumari",
        "category": "Southernmost Tip & Spiritual Landmark",
        "tagline": "Where Three Oceans Converge & The Sun Both Rises and Sets over the Sea",
        "lat": 8.0883,
        "lon": 77.5385,
        "overview": "The southernmost mainland tip of India where the Arabian Sea, Indian Ocean, and Bay of Bengal merge (Triveni Sangam). Famous for magical sunrises and sunsets, the rock memorial of Swami Vivekananda, the 133-foot stone statue of Thiruvalluvar, and Padmanabhapuram Palace.",
        "ideal_duration": "1 to 2 days",
        "best_season": "October to March (Crisp ocean breeze, 22°C - 31°C)",
        "weather_notes": "Chitra Pournami (Full moon in Apr/May) lets visitors see sunset and moonrise simultaneously.",
        "top_attractions": [
            {
                "name": "Vivekananda Rock Memorial & Thiruvalluvar Statue",
                "experience": "Monumental sea rock memorial where Swami Vivekananda meditated in 1892, alongside the towering 133-foot stone statue of Thiruvalluvar.",
                "duration": "2.5 hours",
                "entry_fee": "Ferry ₹50; Rock Entry ₹20",
                "highlights": "Ferry boat ride over crashing waves, Dhyana Mandapam meditation hall"
            },
            {
                "name": "Bhagavathy Amman Temple",
                "experience": "3,000-year-old seashore shrine dedicated to the virgin Goddess Kanyakumari, renowned for her sparkling diamond nose ring.",
                "duration": "1 hour",
                "entry_fee": "Free",
                "highlights": "Ancient sea entrance gate, spiritual atmosphere"
            },
            {
                "name": "Sunset View Point & Triveni Sangam",
                "experience": "The rocky beach promenade where travelers gather to watch the glowing sunset into the ocean.",
                "duration": "1.5 hours",
                "entry_fee": "Free",
                "highlights": "Colorful multi-mineral sand, sunset and sunrise panorama"
            },
            {
                "name": "Padmanabhapuram Palace (35 km)",
                "experience": "16th-century wooden palace masterpiece of Kerala architecture with carved rosewood ceilings and Belgian glass mirrors.",
                "duration": "2.5 hours",
                "entry_fee": "₹40 for adults, ₹15 for children",
                "highlights": "Medicinal beds, secret underground chambers, intricate woodwork"
            }
        ],
        "local_food": {
            "specialties": ["Nanjil Nadu Fish Curry Meals with red matta rice", "Kanyakumari Red Banana (Sevvaazhai)", "Pazha Bajji (Plantain fritters)", "Kothu Parotta"],
            "iconic_eateries": ["Hotel Saravana (Seashore)", "The Ocean Restaurant", "Hotel Sea View Dining"]
        },
        "transport": {
            "railway": "Kanniyakumari Railway Station (CAPE) - Southernmost terminus of Indian Railways",
            "airport": "Trivandrum International Airport (TRV - 90 km / 2.5 hours)",
            "road": "Terminal point of NH 44 (Srinagar to Kanyakumari)"
        },
        "accommodation": {
            "budget": "₹800 - ₹1,600 / night",
            "mid_range": "₹2,200 - ₹4,500 / night (Hotel Sea View, Hotel TamilNadu TTDC)",
            "luxury": "₹5,000 - ₹11,000+ / night (Sparsa Resort)"
        },
        "estimated_budget_per_day": "₹1,200 - ₹2,500 per person",
        "travel_tips": ["Line up for the Vivekananda Rock ferry before 8:30 AM to beat midday lines."],
        "emergency_contacts": {"police": "100", "ambulance": "108"}
    },

    "karur": {
        "name": "Karur",
        "district": "Karur",
        "category": "Ancient Sangam Capital & Textile City",
        "tagline": "Ancient Chera Capital & Textile Export Hub of the Amaravathi River",
        "lat": 10.9601,
        "lon": 78.0766,
        "overview": "Karur was the ancient royal capital of the Sangam Cheras on the banks of the Amaravathi and Cauvery rivers. Renowned for the Pasupatheeswarar temple, the scenic Mayanur Barrage, and world-class home textile exports.",
        "ideal_duration": "1 day",
        "best_season": "October to March (21°C - 31°C)",
        "weather_notes": "Pleasant in winter. Central transit hub between Trichy, Salem, and Dindigul.",
        "top_attractions": [
            {
                "name": "Arulmigu Pasupatheeswarar Temple",
                "experience": "Ancient 7th-century temple featuring a five-foot Lingam with footprints of the divine cow Kamadhenu and exquisite Chola pillar carvings.",
                "duration": "1.5 hours",
                "entry_fee": "Free",
                "highlights": "100-pillar hall, Kamadhenu holy carvings"
            },
            {
                "name": "Mayanur Barrage & Cauvery River Park",
                "experience": "Large water regulator constructed across the Cauvery with children's parks, gardens, and wide water views.",
                "duration": "1.5 hours",
                "entry_fee": "Free",
                "highlights": "River breeze, picnic gardens, viewing wide Cauvery flow"
            },
            {
                "name": "Nerur Sadasiva Brahmendra Samadhi",
                "experience": "Sacred riverside Samadhi of the renowned 18th-century avadhuta saint Sadasiva Brahmendra amidst serene vilva groves.",
                "duration": "1 hour",
                "entry_fee": "Free",
                "highlights": "Deep spiritual silence, Cauvery riverbank walks"
            }
        ],
        "local_food": {
            "specialties": ["Karur fresh river fish fry", "Traditional banana leaf meals", "Kongu country chicken curry"],
            "iconic_eateries": ["Hotel Hemala", "Aasife Biriyani Karur", "Hotel Archana"]
        },
        "transport": {
            "railway": "Karur Junction (KRR) - Connected with Trichy, Erode, Dindigul, and Salem",
            "airport": "Trichy Airport (80 km)",
            "road": "Connected via NH 81 and NH 44"
        },
        "accommodation": {
            "budget": "₹800 - ₹1,400 / night",
            "mid_range": "₹1,800 - ₹3,500 / night (Hotel Hemala, The Royal Grand)"
        },
        "estimated_budget_per_day": "₹1,000 - ₹1,800 per person",
        "travel_tips": ["Karur is an excellent, affordable textile shopping destination for export-quality curtains, bed linens, and kitchen fabrics."],
        "emergency_contacts": {"police": "100", "ambulance": "108"}
    },

    "krishnagiri": {
        "name": "Krishnagiri",
        "district": "Krishnagiri",
        "category": "Granite Hill Forts, Mango Orchards & Lakes",
        "tagline": "The Mango Capital of Tamil Nadu & Land of Majestic Forts",
        "lat": 12.5266,
        "lon": 78.2146,
        "overview": "Bordering Karnataka and Andhra Pradesh, Krishnagiri is framed by black granite boulder hills, historic forts ruled by King Vyasaraja and Tipu Sultan, sprawling mango orchards, and the serene Krishnagiri Reservoir Dam (KRP Dam).",
        "ideal_duration": "1 day (Excursion from Bangalore or Salem)",
        "best_season": "October to March (Pleasant weather, 18°C - 28°C)",
        "weather_notes": "Comfortable climate due to altitude of around 600m.",
        "top_attractions": [
            {
                "name": "Krishnagiri Fort (Syed Basha Hill)",
                "experience": "Dramatic hilltop fortress built by the Vijayanagara king Krishna Deva Raya, offering panoramic views of the plains below.",
                "duration": "2 hours (Moderate climb up stone steps)",
                "entry_fee": "Free",
                "highlights": "Climbing massive granite steps, historical ramparts, sweeping landscape"
            },
            {
                "name": "Krishnagiri Reservoir Project (KRP Dam)",
                "experience": "Scenic dam built across the Thenpennai River flanked by landscaped gardens, fountains, and boat rides.",
                "duration": "1.5 hours",
                "entry_fee": "₹10 per adult",
                "highlights": "Picnic gardens, cool water breeze, children's park"
            },
            {
                "name": "Rayakottai Hill Fort",
                "experience": "18th-century British and Tipu Sultan military garrison built on a towering granite peak, popular among trekkers.",
                "duration": "2.5 hours",
                "entry_fee": "Free",
                "highlights": "Trekking trail, rock-cut reservoirs, historical cannons"
            }
        ],
        "local_food": {
            "specialties": ["World-famous Krishnagiri Totapuri and Alphonso mangoes (in summer)", "Crispy spiced onion pakodas", "South Indian filter coffee along NH 44"],
            "iconic_eateries": ["Hotel TamilNadu KRP Dam", "Saravana Bhavan (NH 44 highway)", "Hotel Mangalam"]
        },
        "transport": {
            "road": "Strategically located on NH 44, just 90 km from Bangalore and 45 km from Hosur",
            "railway": "Hosur Railway Station (45 km) or Jolarpettai (60 km)",
            "airport": "Bangalore Kempegowda Airport (100 km)"
        },
        "accommodation": {
            "budget": "₹800 - ₹1,400 / night (Krishnagiri or Hosur)",
            "mid_range": "₹2,000 - ₹3,800 / night"
        },
        "estimated_budget_per_day": "₹900 - ₹1,800 per person",
        "travel_tips": ["During peak mango season (May-June), roadside stalls offer dozens of fresh farm-plucked mango varieties at wholesale prices."],
        "emergency_contacts": {"police": "100", "ambulance": "108"}
    },

    "madurai": {
        "name": "Madurai",
        "district": "Madurai",
        "category": "Ancient Temple City & Cultural Hub",
        "tagline": "The Athens of the East & Thoonga Nagaram (City That Never Sleeps)",
        "lat": 9.9252,
        "lon": 78.1198,
        "overview": "Madurai has flourished on the banks of the Vaigai River for over 2,500 years. Centered around the awe-inspiring Meenakshi Sundareswarar Temple, it is renowned for classical Tamil literature, vibrant midnight street food, and jasmine flowers (Madurai Malli).",
        "ideal_duration": "2 days",
        "best_season": "October to March (Warm winter, 20°C - 31°C)",
        "weather_notes": "Summers are warm; pleasant winter evenings.",
        "top_attractions": [
            {
                "name": "Arulmigu Meenakshi Sundareswarar Temple",
                "experience": "Monumental Dravidian temple complex with 14 soaring gopurams (highest 52 m), the Hall of Thousand Pillars, and Golden Lotus Sacred Tank.",
                "duration": "3-4 hours",
                "entry_fee": "Free; Thousand Pillar Museum ₹50",
                "highlights": "Night procession at 9:00 PM, musical pillars, 33,000 stone sculptures"
            },
            {
                "name": "Thirumalai Nayakkar Mahal",
                "experience": "17th-century Indo-Saracenic royal palace built in 1636, featuring grand giant circular pillars (12 m high) and celestial pavilion.",
                "duration": "1.5 hours",
                "entry_fee": "₹10; Light show ₹50",
                "highlights": "Grand courtyard, stucco artwork on arches, evening light and sound show"
            },
            {
                "name": "Gandhi Memorial Museum (Tamukkam Palace)",
                "experience": "One of India's five original Gandhi Sangrahalayas, preserving the bloodstained dhoti worn during his assassination.",
                "duration": "1.5 hours",
                "entry_fee": "Free",
                "highlights": "Rare photographic exhibits of India's freedom struggle"
            },
            {
                "name": "Alagar Kovil & Pazhamudircholai",
                "experience": "Scenic Vishnu temple at the foot of Alagar hills and one of the Arupadaiveedu shrines of Lord Murugan at the hilltop.",
                "duration": "2.5 hours",
                "entry_fee": "Free",
                "highlights": "Holy mountain spring, natural hill setting"
            }
        ],
        "local_food": {
            "specialties": ["Original Madurai Famous Jigarthanda (Nannari, Badam pisin, Basundi ice cream)", "Madurai Kari Dosa (Three-layered minced mutton dosa)", "Fluffy Bun Parotta with spicy Salna", "Kola Urundai"],
            "iconic_eateries": ["Famous Jigarthanda (East Marret St)", "Amma Mess", "Murugan Idli Shop", "Konar Mess (Simmakkal)", "Sree Sabarees"]
        },
        "transport": {
            "airport": "Madurai Airport (IXM - 12 km from city)",
            "railway": "Madurai Junction (MDU) - Major Southern Railway division",
            "bus": "Mattuthavani (MGR Integrated Bus Stand) & Arappalayam"
        },
        "accommodation": {
            "budget": "₹800 - ₹1,500 / night",
            "mid_range": "₹2,200 - ₹4,500 / night",
            "luxury": "₹5,000 - ₹14,000+ / night (Heritage Madurai, Gateway Hotel Pasumalai)"
        },
        "estimated_budget_per_day": "₹1,100 - ₹2,300 per person",
        "travel_tips": ["Strict dress code at Meenakshi Temple (dhoti/pants for men, saree/salwar for women; no shorts/sleeveless). Mobile phones are prohibited inside; use locker counters."],
        "emergency_contacts": {"police": "100", "ambulance": "108", "tourist_helpline": "0452-2334757"}
    },

    "mayiladuthurai": {
        "name": "Mayiladuthurai",
        "district": "Mayiladuthurai",
        "category": "Temple Heritage, Danish Fort & Coastal History",
        "tagline": "The Peacock Sanctuary of Shiva, Danish Fort & Sangam Seashore",
        "lat": 11.1075,
        "lon": 79.6524,
        "overview": "Carved out of Nagapattinam, Mayiladuthurai was historically where Goddess Parvati worshipped Lord Shiva in the form of a peacock (Mayil). It encompasses the Danish colonial fortress of Tarangambadi (Tranquebar), the Sangam-era port of Poompuhar, and great Shaivite and Vaishnavite temples.",
        "ideal_duration": "1 to 2 days",
        "best_season": "October to March (Breezy seaside winter, 21°C - 30°C)",
        "weather_notes": "Comfortable coastal breeze; monsoons bring lush greenery to Cauvery delta.",
        "top_attractions": [
            {
                "name": "Tarangambadi (Tranquebar) & Fort Dansborg",
                "experience": "1620 Danish seaside fortress (Fort Dansborg) overlooking the Bay of Bengal, cobblestone King's Street, and India's first printing press museum.",
                "duration": "2.5 hours",
                "entry_fee": "₹10 per adult; Museum ₹5",
                "highlights": "Yellow Danish fort ramparts, crashing waves, breezy colonial promenade"
            },
            {
                "name": "Poompuhar (Kaveripoompattinam)",
                "experience": "Ancient seaport of the Early Cholas celebrated in the Tamil epic Silappathikaram, featuring the Silappathikara Art Gallery and coastal beach.",
                "duration": "2 hours",
                "entry_fee": "₹10 per adult",
                "highlights": "Carved stone memorials illustrating epic Silappathikaram scenes, delta beach"
            },
            {
                "name": "Mayuranathaswamy Temple",
                "experience": "Massive ancient Dravidian temple with a 9-tier Rajagopuram dedicated to Lord Shiva, celebrated for the annual Thula Snanam sacred river bath.",
                "duration": "1.5 hours",
                "entry_fee": "Free",
                "highlights": "Peacock dance reliefs, Cauvery river ghats"
            },
            {
                "name": "Thirukkadaiyur Amritaghateswarar Abhirami Temple",
                "experience": "Famous temple where Lord Shiva saved Markandeya from Yama; premier pilgrimage site for celebrating 60th (Sashtiapthapoorthi) and 80th birthdays.",
                "duration": "2 hours",
                "entry_fee": "Free",
                "highlights": "Special blessing rituals, sacred temple architecture"
            }
        ],
        "local_food": {
            "specialties": ["Mayiladuthurai pure cow-milk filter coffee", "Freshly fried coastal fish in Tarangambadi", "Traditional Cauvery delta thali meals"],
            "iconic_eateries": ["Bungalo on the Beach (Tranquebar - colonial dining)", "Hotel Million Day (Mayiladuthurai)", "Hotel Sadhabishegam (Thirukkadaiyur)"]
        },
        "transport": {
            "railway": "Mayiladuthurai Junction (MV) - Major mainline railhead connecting Chennai, Trichy, and Rameswaram",
            "road": "Connected to Kumbakonam (35 km), Chidambaram (40 km), and Thanjavur (75 km)"
        },
        "accommodation": {
            "budget": "₹800 - ₹1,500 / night (Mayiladuthurai town)",
            "mid_range": "₹2,500 - ₹5,000 / night (Heritage properties in Tranquebar)",
            "luxury": "₹6,000 - ₹12,000+ / night (The Bungalow on the Beach - Neemrana Tranquebar)"
        },
        "estimated_budget_per_day": "₹1,200 - ₹2,500 per person",
        "travel_tips": ["Stay overnight in Tranquebar to experience the quiet sunrise over the Danish fort and crashing waves."],
        "emergency_contacts": {"police": "100", "ambulance": "108"}
    },

    "nagapattinam": {
        "name": "Nagapattinam",
        "district": "Nagapattinam",
        "category": "Interfaith Coastal Shrines & Maritime Heritage",
        "tagline": "The Coastal Pilgrim Haven of Velankanni, Nagore & Ancient Ports",
        "lat": 10.7656,
        "lon": 79.8424,
        "overview": "Nagapattinam is a prominent coastal pilgrimage center on the Bay of Bengal, world-renowned for the Basilica of Our Lady of Good Health in Velankanni, the historic Nagore Dargah, and coastal fishing culture.",
        "ideal_duration": "1 to 2 days",
        "best_season": "October to March (21°C - 30°C)",
        "weather_notes": "Annual feast of Our Lady of Good Health in late August/early September attracts over 2 million pilgrims.",
        "top_attractions": [
            {
                "name": "Basilica of Our Lady of Good Health, Velankanni",
                "experience": "Renowned as the 'Lourdes of the East', this towering Gothic cathedral overlooks the sea and is visited by millions of pilgrims of all faiths.",
                "duration": "2.5 hours",
                "entry_fee": "Free",
                "highlights": "Gothic spires, miraculous shrine, Holy Path, museum of offerings"
            },
            {
                "name": "Nagore Dargah (Nagore Andavar Shrine)",
                "experience": "500-year-old Islamic shrine of saint Shahul Hameed with five tall minarets (highest 40 m) showcasing Indo-Islamic architecture.",
                "duration": "1.5 hours",
                "entry_fee": "Free",
                "highlights": "Soaring minarets, spiritual harmony, holy tank"
            },
            {
                "name": "Nagapattinam Beach & Lighthouse",
                "experience": "Historic seaport beach with a 45-meter functioning maritime lighthouse guiding ships across the Bay of Bengal.",
                "duration": "1 hour",
                "entry_fee": "Free; Lighthouse ₹10",
                "highlights": "Lighthouse views, seaside breeze"
            }
        ],
        "local_food": {
            "specialties": ["Fresh seashore fried fish & calamari", "Nagore special Halwa (Dumroot Halwa)", "South Indian banana leaf meals"],
            "iconic_eateries": ["Hotel Clinton (Velankanni)", "Nagore sweet stalls", "Hotel TamilNadu TTDC Velankanni"]
        },
        "transport": {
            "railway": "Nagapattinam (NGT) & Velankanni (VLNK) connected with Chennai, Bangalore, and Madurai",
            "road": "Connected via ECR and NH 83 to Thanjavur (85 km) and Trichy (140 km)"
        },
        "accommodation": {
            "budget": "₹800 - ₹1,500 / night (Many pilgrim lodges in Velankanni)",
            "mid_range": "₹2,000 - ₹4,200 / night (MGM Vailankanni Residency, Hotel Golden Sand)"
        },
        "estimated_budget_per_day": "₹1,000 - ₹2,200 per person",
        "travel_tips": ["During the Velankanni annual feast (Aug 29 - Sept 8), book rooms several months in advance due to massive pilgrim turnouts."],
        "emergency_contacts": {"police": "100", "ambulance": "108"}
    },

    "namakkal": {
        "name": "Namakkal",
        "district": "Namakkal",
        "category": "Monolithic Rock Fortress, Anjaneyar & 70 Hairpin Bends",
        "tagline": "The City of 18-Foot Monolithic Anjaneyar & Misty Kolli Hills",
        "lat": 11.2189,
        "lon": 78.1674,
        "overview": "Namakkal is famous for its towering 200-foot single rock fort, the legendary open-sky 18-foot monolithic Hanuman (Anjaneyar) statue, and the pristine, winding Kolli Hills with its thrilling 70 continuous hairpin bends.",
        "ideal_duration": "1 to 2 days",
        "best_season": "October to March (18°C - 28°C)",
        "weather_notes": "Kolli Hills stays pleasantly cool year-round.",
        "top_attractions": [
            {
                "name": "Namakkal Anjaneyar Temple",
                "experience": "Legendary 18-foot monolithic statue of Lord Hanuman standing under the open sky facing the Narasimha temple atop the rock.",
                "duration": "1 hour",
                "entry_fee": "Free",
                "highlights": "18-foot single-stone idol, spiritual vibrations"
            },
            {
                "name": "Namakkal Rock Fort & Narasimha Temple",
                "experience": "Monolithic rock fortress constructed in the 9th century, featuring rock-cut cave temples of Lord Ranganatha and Narasimha.",
                "duration": "1.5 hours",
                "entry_fee": "Free",
                "highlights": "Climbing rock fort steps, ancient cave sculptures"
            },
            {
                "name": "Kolli Hills (Kolli Malai) & Agaya Gangai Falls",
                "experience": "Untouched mountain range accessed via 70 continuous hairpin bends, with the 300-foot Agaya Gangai waterfalls in the deep forest valley.",
                "duration": "Full day",
                "entry_fee": "Free; Falls ₹10",
                "highlights": "70 hairpin bend drive, climbing down 1000 steps to waterfalls, organic pepper farms"
            }
        ],
        "local_food": {
            "specialties": ["Kolli Hills medicinal wild honey & fresh black pepper", "Pure mountain pineapple and jackfruit", "Namakkal egg delicacies & spicy chicken roast"],
            "iconic_eateries": ["Hotel Santhosh", "Nala Hotel", "Kolli Hill resorts dining"]
        },
        "transport": {
            "railway": "Namakkal Railway Station (NMKL) on Karur-Salem line",
            "road": "Connected via NH 44 directly between Salem (50 km) and Karur (45 km)"
        },
        "accommodation": {
            "budget": "₹800 - ₹1,400 / night (Namakkal town)",
            "mid_range": "₹2,200 - ₹4,000 / night (Kolli Hills resorts)"
        },
        "estimated_budget_per_day": "₹1,100 - ₹2,200 per person",
        "travel_tips": ["Driving up the 70 hairpin bends to Kolli Hills requires alert driving; avoid traveling late at night."],
        "emergency_contacts": {"police": "100", "ambulance": "108"}
    },

    "nilgiris": {
        "name": "Nilgiris (Ooty & Coonoor)",
        "district": "Nilgiris",
        "category": "Queen of Hill Stations, Tea & UNESCO Rail",
        "tagline": "The Blue Mountains & UNESCO Mountain Railway",
        "lat": 11.4102,
        "lon": 76.6950,
        "overview": "The Nilgiris ('Blue Mountains') rise up to 2,637 meters at Doddabetta Peak. Encompassing Ooty, Coonoor, Kotagiri, and Mudumalai Tiger Reserve, it is celebrated for rolling tea plantations, eucalyptus forests, cool mountain air, and the UNESCO Toy Train.",
        "ideal_duration": "2 to 3 days",
        "best_season": "October to June (Pleasant summer 15°C - 24°C; crisp winter 5°C - 15°C)",
        "weather_notes": "Winter nights can drop near freezing; carry woollens year-round.",
        "top_attractions": [
            {
                "name": "Nilgiri Mountain Railway (UNESCO Toy Train)",
                "experience": "Historic rack-and-pinion steam locomotive running from Mettupalayam through Coonoor to Ooty over tunnels and deep mountain bridges.",
                "duration": "3-4 hours",
                "entry_fee": "First Class ₹205 - ₹600 (Advance IRCTC booking recommended)",
                "highlights": "UNESCO World Heritage ride, breathtaking tea gorge views"
            },
            {
                "name": "Government Botanical Garden & Rose Garden",
                "experience": "55-acre terraced botanical park established in 1848, and India's largest rose garden featuring 20,000 rose varieties.",
                "duration": "2.5 hours",
                "entry_fee": "Botanical ₹40; Rose Garden ₹40",
                "highlights": "20-million-year-old fossilized tree, Italian lawns"
            },
            {
                "name": "Pykara Lake, Waterfalls & Boating",
                "experience": "Sacred Toda river featuring cascading waterfalls and speed-boating in a serene mountain reservoir.",
                "duration": "2.5 hours",
                "entry_fee": "₹10 entry; Speed boat ₹800",
                "highlights": "Pine tree backdrop, thrilling speed boat ride"
            },
            {
                "name": "Doddabetta Peak & Sim's Park Coonoor",
                "experience": "Highest peak in the Nilgiris (2,637 m) and the Japanese-style botanical park in Coonoor.",
                "duration": "2 hours",
                "entry_fee": "Doddabetta ₹10; Sim's Park ₹30",
                "highlights": "Cloud-level panoramic telescope view"
            }
        ],
        "local_food": {
            "specialties": ["Fresh Nilgiri Homemade Chocolates", "Ooty Varkey (crisp flaky tea biscuit)", "Freshly brewed orthodox Nilgiri tea", "Warm plum cake"],
            "iconic_eateries": ["Moddy's Chocolates (Since 1951)", "Earl's Secret", "Cafe Diem (Coonoor)", "Nahar's Sidewalk Cafe"]
        },
        "transport": {
            "airport": "Coimbatore Airport (88 km) is nearest",
            "railway": "Udagamandalam (Ooty) & Coonoor on toy train line; Mettupalayam (MTP) connects to express trains",
            "road": "Connected via Kotagiri and Coonoor ghat roads with 36 hairpin bends"
        },
        "accommodation": {
            "budget": "₹1,000 - ₹1,800 / night",
            "mid_range": "₹2,500 - ₹5,000 / night (Tea estate homestays)",
            "luxury": "₹6,000 - ₹18,000+ / night (Savoy IHCL, Teanest Coonoor)"
        },
        "estimated_budget_per_day": "₹1,500 - ₹3,000 per person",
        "travel_tips": ["Book the UNESCO Toy Train ticket on IRCTC 2-3 months in advance as tickets sell out quickly."],
        "emergency_contacts": {"police": "100", "ambulance": "108"}
    },

    "perambalur": {
        "name": "Perambalur",
        "district": "Perambalur",
        "category": "Historic Bastion Forts & Sacred Shrines",
        "tagline": "The Historic Fortress Citadel of Ranjankudi",
        "lat": 11.2342,
        "lon": 78.8820,
        "overview": "Perambalur is an agricultural district in central Tamil Nadu, celebrated for the imposing 17th-century Ranjankudi Fort constructed by the Nawab of the Carnatic, ancient rock temples, and sugar mills.",
        "ideal_duration": "1 day",
        "best_season": "October to March (21°C - 30°C)",
        "weather_notes": "Pleasant in winter; convenient stopover on Chennai-Trichy NH 45.",
        "top_attractions": [
            {
                "name": "Ranjankudi Fort",
                "experience": "Imposing 17th-century stone fortress with high battlements, deep moat, palace ruins, and underground chambers, site of the 1751 Battle of Valikondah.",
                "duration": "1.5 hours",
                "entry_fee": "Free",
                "highlights": "Cannons, semi-circular bastions, climbing stone ramparts"
            },
            {
                "name": "Chettikulam Balathandayuthapani Temple",
                "experience": "Hilltop Murugan temple built by King Kulothunga Chola I offering panoramic vistas of the surrounding green countryside.",
                "duration": "1.5 hours",
                "entry_fee": "Free",
                "highlights": "Ancient stone carvings, scenic hill breeze"
            },
            {
                "name": "Siruvachur Madhurakali Amman Temple",
                "experience": "Revered 1,000-year-old temple of Goddess Kali, attracting thousands of devotees on Mondays and Fridays.",
                "duration": "1.5 hours",
                "entry_fee": "Free",
                "highlights": "Sacred spiritual traditions, temple car"
            }
        ],
        "local_food": {
            "specialties": ["Perambalur sugar cane juice and jaggery sweets", "Traditional banana leaf meals", "Highway tiffin stalls"],
            "iconic_eateries": ["Hotel Dhanalakshmi Srinivasan", "Highway Saravana Bhavan (NH 45)"]
        },
        "transport": {
            "road": "Strategically positioned on NH 45 (GST Road) between Chennai (270 km) and Trichy (55 km)",
            "railway": "Ariyalur (30 km) or Trichy Junction (55 km)",
            "airport": "Trichy International Airport (60 km)"
        },
        "accommodation": {
            "budget": "₹800 - ₹1,400 / night (Perambalur town or highway hotels)"
        },
        "estimated_budget_per_day": "₹900 - ₹1,800 per person",
        "travel_tips": ["Ranjankudi Fort is just 2 km off the main Chennai-Trichy highway, making it an easy 1-hour cultural detour."],
        "emergency_contacts": {"police": "100", "ambulance": "108"}
    },

    "pudukkottai": {
        "name": "Pudukkottai",
        "district": "Pudukkottai",
        "category": "Jain Cave Murals, Royal Princely Heritage & Forts",
        "tagline": "The Princely State of Rock-Cut Caves & Sittannavasal Frescoes",
        "lat": 10.3797,
        "lon": 78.8208,
        "overview": "Pudukkottai was the only independent princely state in Tamil Nadu during British rule. It is a treasure trove of archaeology featuring the 2nd-century BCE rock-cut Jain cave paintings at Sittannavasal, the colossal rock fortress of Thirumayam, and Kudumiyanmalai musical inscriptions.",
        "ideal_duration": "1 to 2 days",
        "best_season": "October to March (21°C - 30°C)",
        "weather_notes": "Pleasant winter climate; ideal heritage exploring season.",
        "top_attractions": [
            {
                "name": "Sittannavasal Cave (Arivar Koil) & Eladipattam",
                "experience": "2nd-century BCE rock-cut Jain monastery with world-renowned natural vegetable dye fresco paintings of lotus ponds and dancing apsaras, and megalithic stone beds.",
                "duration": "2.5 hours",
                "entry_fee": "₹25 for ASI",
                "highlights": "Echo chamber inside cave, 2000-year-old fresco murals, Jain rock beds"
            },
            {
                "name": "Thirumayam Fort & Rock-Cut Cave Temples",
                "experience": "Dramatic 17th-century rock bastion fort built by Sethupathi rulers, housing ancient rock-cut cave temples of Shiva and reclining Vishnu.",
                "duration": "1.5 hours",
                "entry_fee": "₹25 for ASI",
                "highlights": "Massive monolithic reclining Vishnu carving, cannon bastion"
            },
            {
                "name": "Kudumiyanmalai Temple & Inscription",
                "experience": "Ancient rock shrine famous for the 7th-century Pallava musical treatise inscribed in granite, and the magnificent 1,000-pillar hall.",
                "duration": "1.5 hours",
                "entry_fee": "Free",
                "highlights": "Musical granite inscriptions, stone carvings"
            }
        ],
        "local_food": {
            "specialties": ["Pudukkottai Muttom Murukku", "Chettinad style chicken & mutton curries", "Kavuni Arisi sweet"],
            "iconic_eateries": ["Hotel Shivalik", "Hotel Saradha", "Chettinad traditional messes"]
        },
        "transport": {
            "railway": "Pudukkottai Railway Station (PDKT) on Trichy-Karaikudi line",
            "airport": "Trichy International Airport (50 km)",
            "road": "Connected to Trichy (50 km), Madurai (100 km), and Thanjavur (60 km)"
        },
        "accommodation": {
            "budget": "₹800 - ₹1,500 / night (Pudukkottai town)",
            "mid_range": "₹2,200 - ₹4,000 / night (Chidambara Vilas nearby in Chettinad border)"
        },
        "estimated_budget_per_day": "₹1,000 - ₹2,000 per person",
        "travel_tips": ["Sittannavasal is a must-visit for lovers of Indian art; carry a flashlight to view the cave ceiling murals."],
        "emergency_contacts": {"police": "100", "ambulance": "108"}
    },

    "ramanathapuram": {
        "name": "Ramanathapuram (Rameswaram)",
        "district": "Ramanathapuram",
        "category": "Pilgrimage Island, Pamban Sea Bridge & Ghost Town",
        "tagline": "The Holy Island of Char Dham, Pamban Sea Bridge & Dhanushkodi Land's End",
        "lat": 9.3639,
        "lon": 78.8395,
        "overview": "Ramanathapuram district encompasses the holy island of Rameswaram (one of India's four Char Dham shrines), the historic 1914 Pamban ocean bridge, the ghost town of Dhanushkodi where the Bay of Bengal meets the Indian Ocean, and the memorial of Dr. A.P.J. Abdul Kalam.",
        "ideal_duration": "2 days",
        "best_season": "October to April (Breezy coastal weather, 22°C - 30°C)",
        "weather_notes": "Comfortable winter breeze; summer is warm and sunny.",
        "top_attractions": [
            {
                "name": "Arulmigu Ramanathaswamy Temple",
                "experience": "Jyotirlinga shrine with the world's third-longest corridor (1,220 m) with 1,212 carved pillars and 22 sacred teertham bathing wells.",
                "duration": "3-4 hours",
                "entry_fee": "Free; 22 Theerthams bath ticket ₹25",
                "highlights": "Bathing in 22 theerthams, magnificent pillared corridor"
            },
            {
                "name": "Pamban Sea Bridge & New Railway Lift Bridge",
                "experience": "India's legendary 2.06 km sea bridge over the Palk Strait, offering panoramic views of the open ocean.",
                "duration": "1 hour",
                "entry_fee": "Free",
                "highlights": "Ocean views, watching trains cross over water"
            },
            {
                "name": "Dhanushkodi & Arichal Munai (Land's End)",
                "experience": "The haunting ghost town destroyed in 1964 and Arichal Munai, where the Bay of Bengal meets the Indian Ocean just 28 km from Sri Lanka.",
                "duration": "3 hours",
                "entry_fee": "Free",
                "highlights": "Church ruins, Ram Setu ocean point, dual-colored waters"
            },
            {
                "name": "Dr. A.P.J. Abdul Kalam National Memorial",
                "experience": "Memorial honoring India's 11th President, with missile replicas and personal memorabilia.",
                "duration": "1.5 hours",
                "entry_fee": "Free",
                "highlights": "Rocket models, Kalam's personal library exhibits"
            }
        ],
        "local_food": {
            "specialties": ["Fresh caught Vanjaram (Seer fish) fry", "Nandu (Crab) masala", "Temple Prasadam Puliyodharai & Laddoo", "Tender coconut water"],
            "iconic_eateries": ["Sri Saravana Bhavan Rameswaram", "Hotel Guru Veg", "Daiwik Hotel Restaurant"]
        },
        "transport": {
            "railway": "Rameswaram (RMM) / Mandapam connected across India",
            "airport": "Madurai Airport (170 km / 3.5 hours)",
            "road": "Smooth NH 49 connects mainland to island across Pamban road bridge"
        },
        "accommodation": {
            "budget": "₹800 - ₹1,500 / night (near temple)",
            "mid_range": "₹2,200 - ₹4,500 / night (Daiwik Hotels, TTDC)",
            "luxury": "₹5,000 - ₹10,000+ / night (Hyatt Place Rameswaram)"
        },
        "estimated_budget_per_day": "₹1,200 - ₹2,500 per person",
        "travel_tips": ["Wear clothes suitable for getting completely wet if bathing in the 22 holy wells of Ramanathaswamy Temple; carry a dry change."],
        "emergency_contacts": {"police": "100", "ambulance": "108"}
    },

    "ranipet": {
        "name": "Ranipet",
        "district": "Ranipet",
        "category": "Nawab Heritage, Delhi Gate & Craft Hub",
        "tagline": "The City of Arcot Nawabs, Historic Delhi Gate & Palar River",
        "lat": 12.9224,
        "lon": 79.3330,
        "overview": "Ranipet district is deeply intertwined with the history of the Carnatic Nawabs. It features the famous town of Arcot, Robert Clive's historic Delhi Gate, the ancient Mahendravadi rock-cut cave, and renowned leather manufacturing.",
        "ideal_duration": "1 day",
        "best_season": "October to March (20°C - 30°C)",
        "weather_notes": "Comfortable in winter; warm in summer.",
        "top_attractions": [
            {
                "name": "Delhi Gate, Arcot",
                "experience": "The lone surviving entrance gate of the historic Arcot Fort where Robert Clive made his famous defense during the 1751 Siege of Arcot.",
                "duration": "1 hour",
                "entry_fee": "Free",
                "highlights": "Mughal arch architecture, Clive's secret upper room"
            },
            {
                "name": "Mahendravadi Rock-Cut Temple",
                "experience": "6th-century rock-cut cave shrine excavated by Pallava King Mahendravarman I dedicated to Lord Vishnu.",
                "duration": "1 hour",
                "entry_fee": "Free",
                "highlights": "Early Pallava monolithic rock architecture"
            },
            {
                "name": "Arcot Nawab Tombs & Palar Riverfront",
                "experience": "Dargahs and tombs of the Carnatic Nawabs dating back to the 18th century along the Palar river basin.",
                "duration": "1 hour",
                "entry_fee": "Free",
                "highlights": "Islamic arches, historic tombs"
            }
        ],
        "local_food": {
            "specialties": ["World-famous Arcot Makkan Peda (deep-fried khoya sweet soaked in sugar syrup)", "Arcot Star Mutton Biryani", "Ambur Biryani nearby"],
            "iconic_eateries": ["Arcot Sweet Stalls (near bus stand)", "Star Biryani (Arcot branch)"]
        },
        "transport": {
            "railway": "Walajah Road Junction (WJR) on Chennai-Bangalore mainline",
            "road": "Connected on NH 48, just 25 km from Vellore and 110 km from Chennai",
            "airport": "Chennai International Airport (100 km)"
        },
        "accommodation": {
            "budget": "₹800 - ₹1,400 / night (Walajapet or stay in Vellore 20 mins away)"
        },
        "estimated_budget_per_day": "₹900 - ₹1,800 per person",
        "travel_tips": ["Do not leave Arcot without tasting authentic freshly made warm Makkan Peda from local sweet shops."],
        "emergency_contacts": {"police": "100", "ambulance": "108"}
    },

    "salem": {
        "name": "Salem",
        "district": "Salem",
        "category": "Steel City, Yercaud Hill Station & Mettur Dam",
        "tagline": "The City of Steel, Sweet Mangoes, Yercaud Hills & Mettur Dam",
        "lat": 11.6643,
        "lon": 78.1460,
        "overview": "Surrounded by hills on all sides, Salem is renowned for the Shevaroy hill station of Yercaud, the monumental Mettur Dam on the Cauvery river, delicious Malgoa mangoes, steel production, and handloom silks.",
        "ideal_duration": "2 days",
        "best_season": "October to March (18°C - 28°C)",
        "weather_notes": "Yercaud hill station stays cool year-round (15°C - 24°C).",
        "top_attractions": [
            {
                "name": "Yercaud Hill Station & Emerald Lake",
                "experience": "Scenic hill station in the Shevaroy Hills reached via 20 hairpin bends, featuring boat rides on Emerald Lake and coffee plantations.",
                "duration": "1-2 days",
                "entry_fee": "Lake free; Boating ₹120 - ₹250",
                "highlights": "Pedal boating, Lady's Seat cliff view, Killiyur waterfalls"
            },
            {
                "name": "Mettur Dam & Stanley Reservoir",
                "experience": "One of India's largest and oldest dams built in 1934 across the Cauvery River, flanked by thermal power plants and parks.",
                "duration": "2 hours",
                "entry_fee": "Park ₹10",
                "highlights": "Massive masonry dam wall, river breeze, fresh fried fish"
            },
            {
                "name": "1008 Shiva Lingam Temple",
                "experience": "Hilltop shrine featuring 1,008 individual Shiva lingams carved in granite surrounding a giant central presiding deity.",
                "duration": "1.5 hours",
                "entry_fee": "Free",
                "highlights": "Panoramic view of Salem city, spiritual architecture"
            }
        ],
        "local_food": {
            "specialties": ["Salem Malgoa & Salem Bengalora mangoes (in season)", "Salem Thattu Vadai Set (crispy street snack with beet and carrot chutney)", "Yercaud fresh brewed coffee"],
            "iconic_eateries": ["Hotel Saravana Bhavan (Salem New Bus Stand)", "Selvi Mess", "Yercaud Lake Cafes"]
        },
        "transport": {
            "railway": "Salem Junction (SA) - Major Southern Railway junction",
            "airport": "Salem Airport (SXV) at Kamalapuram",
            "road": "Connected via NH 44, NH 544, and NH 79"
        },
        "accommodation": {
            "budget": "₹800 - ₹1,500 / night (Salem city)",
            "mid_range": "₹2,200 - ₹4,500 / night (Sterling Yercaud, Grand Palace)"
        },
        "estimated_budget_per_day": "₹1,200 - ₹2,400 per person",
        "travel_tips": ["Try Salem's iconic street food 'Thattu Vadai Set' sold at evening mobile carts across the city."],
        "emergency_contacts": {"police": "100", "ambulance": "108"}
    },

    "sivaganga": {
        "name": "Sivaganga (Chettinad)",
        "district": "Sivaganga",
        "category": "Merchant Mansions, Athangudi Tiles & World Cuisine",
        "tagline": "The Legendary Land of Chettinad Palaces & Culinary Mastery",
        "lat": 9.8433,
        "lon": 78.4809,
        "overview": "Sivaganga is the heart of Chettinad, founded by the prosperous Nagarathar merchant community. Renowned worldwide for 19th-century palatial mansions with Burma teak and Italian marble, handmade Athangudi floor tiles, and the fiery, world-acclaimed Chettinad cuisine.",
        "ideal_duration": "1 to 2 days",
        "best_season": "October to March (21°C - 30°C)",
        "weather_notes": "Summers are warm; pleasant winter breezes.",
        "top_attractions": [
            {
                "name": "Kanadukathan Chettinad Palace",
                "experience": "1912 architectural marvel with over 1,000 windows, carved Burma teak pillars, Bohemian crystal chandeliers, and wide courtyards.",
                "duration": "1.5 hours",
                "entry_fee": "₹100 for exterior viewing/select mansion entry",
                "highlights": "Athangudi tiles, grand courtyards, Flemish glass"
            },
            {
                "name": "Athangudi Handmade Tile Workshops",
                "experience": "Watch master craftsmen handcrafting vibrant, eco-friendly cement tiles using glass molds and floral motifs.",
                "duration": "1 hour",
                "entry_fee": "Free",
                "highlights": "Live tile pouring demonstration, buying souvenir coasters"
            },
            {
                "name": "Pillayarpatti Karpaga Vinayagar Temple",
                "experience": "Ancient 4th-century rock-cut cave temple dedicated to Lord Ganesha carved out of a hillside, featuring a six-foot bas-relief idol.",
                "duration": "1.5 hours",
                "entry_fee": "Free",
                "highlights": "One of the oldest stone Ganesha shrines in Tamil Nadu"
            }
        ],
        "local_food": {
            "specialties": ["Chettinad Chicken Pepper Fry (Milagu Kozhi)", "Kuzhi Paniyaram with Kara Chutney", "Kandarappam & Vellai Paniyaram", "Chettinad Meen Kozhambu"],
            "iconic_eateries": ["The Bangala (Kanadukathan - world renowned feast)", "Visalam CGH Earth", "Friends Restaurant Karaikudi"]
        },
        "transport": {
            "railway": "Karaikudi Junction (KKDI) & Sivaganga (SVGA)",
            "airport": "Madurai Airport (85 km) or Trichy Airport (80 km)"
        },
        "accommodation": {
            "budget": "₹900 - ₹1,600 / night (Karaikudi)",
            "mid_range": "₹3,000 - ₹6,000 / night (Heritage mansion stays)",
            "luxury": "₹7,500 - ₹18,000+ / night (The Bangala, Visalam)"
        },
        "estimated_budget_per_day": "₹1,500 - ₹3,500 per person",
        "travel_tips": ["Book lunch at The Bangala in Kanadukathan in advance for the ultimate traditional 7-course Chettinad banana leaf feast."],
        "emergency_contacts": {"police": "100", "ambulance": "108"}
    },

    "tenkasi": {
        "name": "Tenkasi (Courtallam)",
        "district": "Tenkasi",
        "category": "Spa of South India & Herbal Waterfalls",
        "tagline": "The Natural Herbal Waterfalls Spa & Kasi of the South",
        "lat": 8.9594,
        "lon": 77.3150,
        "overview": "Carved out of Tirunelveli, Tenkasi ('Varanasi of the South') features the historic Kasi Viswanathar Temple and the world-renowned Courtallam waterfalls flowing through medicinal Western Ghats herbal forests.",
        "ideal_duration": "1 to 2 days",
        "best_season": "June to September (Peak Saral drizzle season) & October to February",
        "weather_notes": "Saral season brings cool misty drizzles and rejuvenating waterfall flows.",
        "top_attractions": [
            {
                "name": "Courtallam Main Falls (Peraruvi) & Five Falls",
                "experience": "Therapeutic waterfalls cascading over rocks in herbal forests, safe for outdoor bathing with protective railings.",
                "duration": "2-3 hours",
                "entry_fee": "Free",
                "highlights": "Herbal mineral bath, night lighting during season"
            },
            {
                "name": "Tenkasi Kasi Viswanathar Temple",
                "experience": "Majestic 14th-century temple with a towering 180-foot Rajagopuram built by King Parakkirama Pandian with musical stone pillars.",
                "duration": "1.5 hours",
                "entry_fee": "Free",
                "highlights": "180-foot gopuram, musical pillars, spiritual peace"
            },
            {
                "name": "Gundar Dam & Reservoir",
                "experience": "Tranquil water reservoir surrounded by Western Ghats mountains and green paddy valleys.",
                "duration": "1.5 hours",
                "entry_fee": "Free",
                "highlights": "Scenic nature walks, fresh mountain air"
            }
        ],
        "local_food": {
            "specialties": ["Border Rahmath Parotta (Sengottai - flaky parotta with spicy chicken gravy)", "Hot spicy banana bajjis by the falls", "Herbal mountain spice tea"],
            "iconic_eateries": ["Border Rahmath Parotta", "Hotel Saaral Dining", "Courtallam highway stalls"]
        },
        "transport": {
            "railway": "Tenkasi Junction (TSI) on Chennai-Sengottai line",
            "airport": "Tuticorin Airport (85 km) or Madurai (150 km)"
        },
        "accommodation": {
            "budget": "₹800 - ₹1,500 / night",
            "mid_range": "₹2,200 - ₹4,500 / night (Saaral Resorts)"
        },
        "estimated_budget_per_day": "₹1,200 - ₹2,500 per person",
        "travel_tips": ["Carry an extra change of clothes and waterproof bags for phones and wallets while visiting Courtallam."],
        "emergency_contacts": {"police": "100", "ambulance": "108"}
    },

    "thanjavur": {
        "name": "Thanjavur",
        "district": "Thanjavur",
        "category": "UNESCO Chola Capital & Classical Arts",
        "tagline": "The Rice Bowl of Tamil Nadu & Cradle of Chola Architecture",
        "lat": 10.7870,
        "lon": 79.1378,
        "overview": "Thanjavur was the majestic royal capital of the Great Chola Empire. Renowned for the UNESCO World Heritage Brihadisvara Temple, classical Tanjore gold-leaf paintings, Thanjavur dancing dolls, and Maratha royal palace.",
        "ideal_duration": "1 to 2 days",
        "best_season": "October to March (20°C - 30°C)",
        "weather_notes": "Summers are warm; pleasant winter breeze across Cauvery delta.",
        "top_attractions": [
            {
                "name": "Brihadisvara Temple (Big Temple - UNESCO)",
                "experience": "Architectural wonder built in 1010 CE by Emperor Raja Raja Chola I with a 66-meter high granite Vimana and monolithic Nandi.",
                "duration": "2.5 hours",
                "entry_fee": "Free",
                "highlights": "Granite Vimana shadow marvel, monolithic Nandi, 1,000-year-old frescoes"
            },
            {
                "name": "Thanjavur Maratha Palace & Art Gallery",
                "experience": "Royal complex built by Nayak and Maratha rulers featuring the Bell Tower, Arsenal Tower, and Chola bronze sculptures.",
                "duration": "2 hours",
                "entry_fee": "₹50 for adults",
                "highlights": "Bronze Chola masterpieces, royal durbar hall"
            },
            {
                "name": "Saraswathi Mahal Library",
                "experience": "One of Asia's oldest medieval libraries, established in the 16th century, housing 60,000 rare palm-leaf manuscripts.",
                "duration": "1 hour",
                "entry_fee": "Free",
                "highlights": "Rare illuminated manuscripts, ancient maps"
            }
        ],
        "local_food": {
            "specialties": ["Thanjavur Ashoka Halwa (Thiruvaiyaru pure ghee mung dal halwa)", "Cauvery Delta Banana Leaf Full Meals", "Kavuni Arisi sweet"],
            "iconic_eateries": ["Hotel Gnanam (Diana Veg)", "Sathars Restaurant", "Andavar Halwa Kadai (Thiruvaiyaru)"]
        },
        "transport": {
            "railway": "Thanjavur Junction (TJ)",
            "airport": "Trichy International Airport (55 km / 1 hour)",
            "road": "Smooth 4-lane highway from Trichy and Kumbakonam"
        },
        "accommodation": {
            "budget": "₹800 - ₹1,400 / night",
            "mid_range": "₹2,200 - ₹4,200 / night (Hotel Gnanam, Sangam Hotel)",
            "luxury": "₹5,000 - ₹12,000+ / night (Svatma Heritage Luxury Resort)"
        },
        "estimated_budget_per_day": "₹1,000 - ₹2,200 per person",
        "travel_tips": ["Visit the Big Temple around 4:30 PM to avoid stone floor heat and witness the golden sunset illuminating the granite Vimana."],
        "emergency_contacts": {"police": "100", "ambulance": "108"}
    },

    "theni": {
        "name": "Theni",
        "district": "Theni",
        "category": "Cloud Mountain (Megamalai), Waterfalls & Cardamom",
        "tagline": "The Earth of Western Ghats, Suruli Falls & Misty Megamalai",
        "lat": 10.0104,
        "lon": 77.4768,
        "overview": "Surrounded by the Western Ghats, Theni is an eco-paradise featuring the misty high-altitude tea hills of Megamalai (Highwavys), the thunderous Suruli Falls mentioned in Silappathikaram, the grape vineyards of Cumbum valley, and cardamom plantations of Bodinayakkanur.",
        "ideal_duration": "2 days",
        "best_season": "October to March (18°C - 28°C)",
        "weather_notes": "Megamalai is cool and misty year-round.",
        "top_attractions": [
            {
                "name": "Megamalai (Highwavys Cloud Mountain)",
                "experience": "Secluded hill station at 1,500 meters framed by rolling tea estates, cloud curtains, elephant reserves, and 18 hairpin bends.",
                "duration": "1-2 days",
                "entry_fee": "Free",
                "highlights": "Tea estate vistas, wildlife spotting, peaceful mountain mist"
            },
            {
                "name": "Suruli Falls",
                "experience": "Cascading two-tier waterfall descending from the Meghamalai slopes, surrounded by 18 natural caves.",
                "duration": "2 hours",
                "entry_fee": "₹10 per adult",
                "highlights": "Natural outdoor bathing, ancient rock caves"
            },
            {
                "name": "Kumbakkarai Falls",
                "experience": "Rock waterfall located at the foothills of Kodaikanal hills along the Pambar river.",
                "duration": "1.5 hours",
                "entry_fee": "₹15 per adult",
                "highlights": "Bathing pools, shaded rock picnic spots"
            },
            {
                "name": "Cumbum Valley Grape Vineyards",
                "experience": "Lush green valley producing Muscat Hamburg (Panneer) grapes throughout the year.",
                "duration": "1.5 hours",
                "entry_fee": "Free",
                "highlights": "Walking through grape orchards, buying fresh vine grapes"
            }
        ],
        "local_food": {
            "specialties": ["Theni fresh Panneer Grapes & grape juice", "Bodinayakkanur Cardamom tea", "Kongu & Madurai style non-veg feasts"],
            "iconic_eateries": ["Hotel Western Gatz", "Hotel Theni International", "Local Cumbum mess"]
        },
        "transport": {
            "railway": "Theni & Bodinayakkanur Railway Stations connected to Madurai",
            "airport": "Madurai Airport (80 km)",
            "road": "Connected via NH 85 (Kochi-Dhanushkodi highway)"
        },
        "accommodation": {
            "budget": "₹800 - ₹1,500 / night (Theni town)",
            "mid_range": "₹2,200 - ₹4,500 / night (Megamalai tea estate stays)"
        },
        "estimated_budget_per_day": "₹1,200 - ₹2,400 per person",
        "travel_tips": ["Megamalai requires an SUV or vehicle with good ground clearance due to rough forest road stretches."],
        "emergency_contacts": {"police": "100", "ambulance": "108"}
    },

    "thoothukudi": {
        "name": "Thoothukudi (Tuticorin)",
        "district": "Thoothukudi",
        "category": "Pearl Fishery Coast, Basilica & Macaroons",
        "tagline": "The Pearl City & Port of Freedom Fighters",
        "lat": 8.7642,
        "lon": 78.1348,
        "overview": "Thoothukudi is known as the 'Pearl City' on the Gulf of Mannar. Famous for its historic sea port, the 16th-century Our Lady of Snows Basilica, pearl harvesting heritage, freedom fighter V.O. Chidambaram Pillai memorials, and cashew-based Tuticorin Macaroons.",
        "ideal_duration": "1 to 2 days",
        "best_season": "October to March (Breezy coastal winter, 22°C - 30°C)",
        "weather_notes": "Pleasant in winter; sunny seaside weather.",
        "top_attractions": [
            {
                "name": "Our Lady of Snows Basilica",
                "experience": "16th-century Portuguese Baroque church housing a miraculous statue of Mother Mary brought from Manila in 1555.",
                "duration": "1.5 hours",
                "entry_fee": "Free",
                "highlights": "Baroque architecture, annual August golden chariot festival"
            },
            {
                "name": "Hare Island & Pearl City Beach",
                "experience": "Tranquil coastal island connected by road, popular for sunset walks and sea breezes.",
                "duration": "1.5 hours",
                "entry_fee": "Free",
                "highlights": "Coastal breeze, sea views, lighthouse"
            },
            {
                "name": "Tiruchendur Murugan Temple (40 km)",
                "experience": "Second of the Six Abodes of Lord Murugan, constructed directly on the seashore of the Gulf of Mannar.",
                "duration": "2.5 hours",
                "entry_fee": "Free; Special Darshan ₹100",
                "highlights": "Seashore temple setting, soaring 137-foot Rajagopuram"
            }
        ],
        "local_food": {
            "specialties": ["World-famous Tuticorin Macaroon (crisp egg white, sugar, and cashew confection)", "Poricha Parotta with spicy Salna", "Fresh coastal crab and prawn curry"],
            "iconic_eateries": ["Bell Hotel Restaurant", "Aardvark Cafe", "Famous Tuticorin Macaroon bakeries"]
        },
        "transport": {
            "airport": "Tuticorin Airport (TCR) at Vagaikulam",
            "railway": "Tuticorin (TN) connecting directly to Chennai and Bangalore",
            "road": "Connected via NH 38 from Madurai (140 km) and Tirunelveli (50 km)"
        },
        "accommodation": {
            "budget": "₹800 - ₹1,500 / night",
            "mid_range": "₹2,200 - ₹4,200 / night (Hotel DSF Grand, Regency Tuticorin)"
        },
        "estimated_budget_per_day": "₹1,100 - ₹2,300 per person",
        "travel_tips": ["Buy authentic GI-style Tuticorin macaroons packed in traditional tin boxes to preserve crispness."],
        "emergency_contacts": {"police": "100", "ambulance": "108"}
    },

    "tiruchirappalli": {
        "name": "Tiruchirappalli (Trichy)",
        "district": "Tiruchirappalli",
        "category": "Cauvery Delta Citadel & Grand Temples",
        "tagline": "Fortress Town of the Cholas, Rockfort & World's Largest Temple",
        "lat": 10.7905,
        "lon": 78.7047,
        "overview": "Trichy is a historic city on the banks of the Cauvery. It features the 3.8-billion-year-old Rockfort Ucchi Pillayar temple, Sri Ranganathaswamy Temple (the world's largest functioning temple complex), and the 2nd-century Kallanai Grand Anicut dam.",
        "ideal_duration": "1 to 2 days",
        "best_season": "October to March (21°C - 31°C)",
        "weather_notes": "Summers are warm; central hub connecting all parts of Tamil Nadu.",
        "top_attractions": [
            {
                "name": "Sri Ranganathaswamy Temple, Srirangam",
                "experience": "World's largest functioning temple complex (156 acres) with 21 grand gopurams including the 73-meter Rajagopuram.",
                "duration": "3 hours",
                "entry_fee": "Free; Special Darshan ₹100 - ₹250",
                "highlights": "73-meter Rajagopuram, 1000-pillar hall, Garuda shrine"
            },
            {
                "name": "Rockfort Ucchi Pillayar Temple",
                "experience": "83-meter high monolithic rock older than the Himalayas, climbed via 437 stone steps, with panoramic views of Trichy and Srirangam.",
                "duration": "2 hours",
                "entry_fee": "Free",
                "highlights": "Rock-cut cave shrines, sunset view over the Cauvery"
            },
            {
                "name": "Kallanai Dam (Grand Anicut)",
                "experience": "One of the world's oldest functional water-diversion dams built in the 2nd century CE by Chola King Karikalan across the Cauvery.",
                "duration": "1.5 hours",
                "entry_fee": "Free",
                "highlights": "Ancient engineering wonder, picnic gardens"
            }
        ],
        "local_food": {
            "specialties": ["Trichy Banana Leaf Thali with Mor Kuzhambu", "Srirangam Sweet Pongal & Puliyodharai", "Cauvery Ayirai Fish Curry"],
            "iconic_eateries": ["Sri Sangeethas", "Mani's Cafe (Near Rockfort)", "DiMoRa"]
        },
        "transport": {
            "airport": "Tiruchirappalli International Airport (TRZ)",
            "railway": "Tiruchirappalli Junction (TPJ)",
            "bus": "Central Bus Stand (Cantt)"
        },
        "accommodation": {
            "budget": "₹800 - ₹1,500 / night",
            "mid_range": "₹2,200 - ₹4,200 / night (Courtyard by Marriott, SRM Hotel, Sangam)"
        },
        "estimated_budget_per_day": "₹1,000 - ₹2,200 per person",
        "travel_tips": ["Climb the Rockfort before 8:30 AM to beat midday heat on the bare stone steps."],
        "emergency_contacts": {"police": "100", "ambulance": "108"}
    },

    "tirunelveli": {
        "name": "Tirunelveli",
        "district": "Tirunelveli",
        "category": "Historic Cultural City on Thamirabarani River",
        "tagline": "The City of Musical Pillars, Iruttu Kadai Halwa & Sacred Waters",
        "lat": 8.7139,
        "lon": 77.7567,
        "overview": "Located on the banks of Tamil Nadu's only perennial river, the Thamirabarani, Tirunelveli is celebrated for the 7th-century Nellaiappar Temple with its musical pillars, Western Ghats waterfalls nearby, and world-famous wheat Halwa.",
        "ideal_duration": "1 to 2 days",
        "best_season": "October to March (22°C - 30°C)",
        "weather_notes": "Comfortable winter weather; gateway to Courtallam and Manimuthar.",
        "top_attractions": [
            {
                "name": "Arulmigu Nellaiappar & Kanthimathi Temple",
                "experience": "Ancient 14-acre temple complex with musical stone pillars that emit swaras when tapped, and the Tamra Sabha (Copper Hall of Nataraja).",
                "duration": "2.5 hours",
                "entry_fee": "Free",
                "highlights": "Musical pillars, Copper Nataraja dance stage"
            },
            {
                "name": "Manimuthar Falls & Dam",
                "experience": "Cascading waterfall nestled inside lush Western Ghats reserves 40 km from town, with a scenic reservoir and tea gardens above at Manjolai.",
                "duration": "3 hours",
                "entry_fee": "Forest checkpost fee ₹30",
                "highlights": "Natural forest pool, mountain drive"
            }
        ],
        "local_food": {
            "specialties": ["Tirunelveli Iruttu Kadai Halwa (Pure ghee wheat halwa served hot on lotus leaves)", "Tirunelveli Sodhi Kuzhambu (Coconut milk drumstick stew)", "Ulundhu Kali"],
            "iconic_eateries": ["Iruttu Kadai (Opposite Nellaiappar temple, opens 5:00 PM)", "Shanthi Sweets", "Hotel Aryas"]
        },
        "transport": {
            "railway": "Tirunelveli Junction (TEN) with Vande Bharat and Superfast express trains",
            "airport": "Tuticorin Airport (35 km) or Trivandrum (140 km)",
            "road": "Connected via NH 44 to Madurai and Kanyakumari"
        },
        "accommodation": {
            "budget": "₹800 - ₹1,400 / night",
            "mid_range": "₹2,000 - ₹3,800 / night (Hotel Apple TTree, Aryas)"
        },
        "estimated_budget_per_day": "₹1,000 - ₹2,000 per person",
        "travel_tips": ["Line up at Iruttu Kadai around 4:45 PM before it opens at 5:00 PM; warm halwa sells out quickly."],
        "emergency_contacts": {"police": "100", "ambulance": "108"}
    },

    "tirupathur": {
        "name": "Tirupathur (Yelagiri)",
        "district": "Tirupathur",
        "category": "Hill Station, Trekking & Lake Haven",
        "tagline": "The Poor Man's Ooty, Yelagiri Hills & Swamimalai Trek",
        "lat": 12.4965,
        "lon": 78.5661,
        "overview": "Carved out of Vellore, Tirupathur encompasses the popular, tranquil hill station of Yelagiri (1,110 m) with its 14 hairpin bends, peaceful Punganoor Lake, and thrilling Swamimalai trek.",
        "ideal_duration": "1 to 2 days",
        "best_season": "October to March (18°C - 26°C)",
        "weather_notes": "Pleasantly cool hill station breeze; never freezing cold.",
        "top_attractions": [
            {
                "name": "Punganoor Lake & Nature Park",
                "experience": "Artificial mountain lake surrounded by gardens, musical fountains, and row/pedal boating.",
                "duration": "2 hours",
                "entry_fee": "Park ₹15; Boating ₹100 - ₹200",
                "highlights": "Pedal boating, walking along flower gardens"
            },
            {
                "name": "Swamimalai Hill Trek",
                "experience": "Highest peak in Yelagiri (4,338 ft) shaped like a cake, reached via an invigorating 3 km forest trek with panoramic valley vistas.",
                "duration": "3 hours",
                "entry_fee": "Free",
                "highlights": "Trekking trail, hilltop Shiva shrine, valley views"
            },
            {
                "name": "Jalagamparai Waterfalls",
                "experience": "Waterfall descending from the Yelagiri hills through the Attaru river, surrounded by herbal forests.",
                "duration": "2 hours",
                "entry_fee": "Free",
                "highlights": "Natural forest cascade (best post-monsoon)"
            }
        ],
        "local_food": {
            "specialties": ["Fresh forest honey", "Locally grown jackfruit and hill bananas", "South Indian home-style tiffin"],
            "iconic_eateries": ["Yelagiri lakeside restaurants", "Hotel Landmark", "Sterling Yelagiri"]
        },
        "transport": {
            "railway": "Jolarpettai Junction (JTJ - 20 km from Yelagiri)",
            "road": "Connected via Bangalore-Chennai highway (NH 48), 150 km from Bangalore, 230 km from Chennai"
        },
        "accommodation": {
            "budget": "₹900 - ₹1,600 / night",
            "mid_range": "₹2,200 - ₹4,500 / night (Sterling Yelagiri, Marigold Ridge)"
        },
        "estimated_budget_per_day": "₹1,200 - ₹2,200 per person",
        "travel_tips": ["The 14 hairpin bends of Yelagiri are named after prominent Tamil poets; drive slowly and enjoy the scenic pull-out points."],
        "emergency_contacts": {"police": "100", "ambulance": "108"}
    },

    "tiruppur": {
        "name": "Tiruppur",
        "district": "Tiruppur",
        "category": "Knitwear Capital, Bird Sanctuaries & Hills",
        "tagline": "The Dollar City, Textile Capital & Thirumoorthy Hills",
        "lat": 11.1085,
        "lon": 77.3411,
        "overview": "Tiruppur is known as the knitwear textile capital of India ('Dollar City'). It features the historic Avinashi Lingeswarar Temple, the pristine Thirumoorthy Hills with Amanalingeswarar Temple and dam, and the Nanjarayan Bird Sanctuary.",
        "ideal_duration": "1 to 2 days",
        "best_season": "October to March (20°C - 30°C)",
        "weather_notes": "Comfortable winter weather; agricultural and textile greenery.",
        "top_attractions": [
            {
                "name": "Avinashi Lingeswarar Temple",
                "experience": "Ancient 7th-century temple celebrated by Sundarar for reviving a child swallowed by a crocodile, featuring towering gopurams.",
                "duration": "1.5 hours",
                "entry_fee": "Free",
                "highlights": "Exquisite Dravidian stone carvings, sacred history"
            },
            {
                "name": "Thirumoorthy Hills, Temple & Dam (Udumalpet)",
                "experience": "Scenic mountain foothills featuring the unique Amanalingeswarar Temple honoring the Hindu Trinity (Brahma, Vishnu, Shiva) under one lingam, waterfalls, and dam.",
                "duration": "Half day",
                "entry_fee": "Free",
                "highlights": "Panjalingam waterfalls, boating in reservoir, hill views"
            },
            {
                "name": "Nanjarayan Tank Bird Sanctuary",
                "experience": "Recently notified 125-hectare bird sanctuary hosting over 180 resident and migratory bird species.",
                "duration": "1.5 hours",
                "entry_fee": "Free",
                "highlights": "Winter birdwatching, lakefront walking trails"
            }
        ],
        "local_food": {
            "specialties": ["Kongu style Pallipalayam chicken", "Nattu Kozhi briyani", "Hot filter coffee and crisp vadas"],
            "iconic_eateries": ["Velan Hotel", "Junior Kuppanna Tiruppur", "Gayathri Pure Veg"]
        },
        "transport": {
            "railway": "Tiruppur Railway Station (TUP) on Coimbatore-Erode mainline",
            "airport": "Coimbatore Airport (45 km)",
            "road": "Smooth 6-lane NH 544"
        },
        "accommodation": {
            "budget": "₹800 - ₹1,500 / night",
            "mid_range": "₹2,000 - ₹3,800 / night (Velan Hotel, Poppys Tower)"
        },
        "estimated_budget_per_day": "₹1,000 - ₹2,000 per person",
        "travel_tips": ["Thirumoorthy hills and dam near Udumalpet make an ideal day outing from Tiruppur or Coimbatore."],
        "emergency_contacts": {"police": "100", "ambulance": "108"}
    },

    "tiruvallur": {
        "name": "Tiruvallur",
        "district": "Tiruvallur",
        "category": "Sacred Tanks, Bird Sanctuaries & Lagoons",
        "tagline": "The City of Veeraraghava Perumal & Pulicat Lagoon Haven",
        "lat": 13.1432,
        "lon": 79.9070,
        "overview": "Adjacent to Chennai, Tiruvallur is celebrated for the ancient Sri Veeraraghava Perumal temple, the historic Hritayaleeswarar temple, the Pulicat Lake lagoon bird sanctuary, and the Poondi reservoir.",
        "ideal_duration": "1 day",
        "best_season": "October to March (20°C - 30°C)",
        "weather_notes": "Comfortable winter weather; flamingo season at Pulicat.",
        "top_attractions": [
            {
                "name": "Sri Veeraraghava Perumal Temple",
                "experience": "One of the 108 Divya Desams, featuring Lord Vishnu in a majestic reclining posture on Adishesha, renowned for curing ailments.",
                "duration": "1.5 hours",
                "entry_fee": "Free",
                "highlights": "Hritayaleeswarar healing tank, Dravidian architecture"
            },
            {
                "name": "Pulicat Lake Bird Sanctuary (Pazhaverkadu)",
                "experience": "India's second-largest brackish water lagoon, attracting tens of thousands of pink greater flamingos between November and February.",
                "duration": "2.5 hours",
                "entry_fee": "Free; Boat ride ₹600 - ₹1,000",
                "highlights": "Flamingo watching, Dutch cemetery, lighthouse"
            },
            {
                "name": "Poondi Reservoir (Sathyamurthy Sagar)",
                "experience": "Major drinking water reservoir constructed across the Kosasthalaiyar River with parks and botanical gardens.",
                "duration": "1.5 hours",
                "entry_fee": "Free",
                "highlights": "Water breeze, picnic spot"
            }
        ],
        "local_food": {
            "specialties": ["Pulicat lagoon fresh prawn & crab fry", "Traditional temple prasadam", "South Indian filter coffee"],
            "iconic_eateries": ["Hotel Saravana Bhavan Tiruvallur", "Pulicat seafood stalls"]
        },
        "transport": {
            "railway": "Tiruvallur Railway Station (TRL) connected via Chennai suburban electric trains every 15 minutes",
            "road": "Connected via Chennai-Tirupati highway (NH 716), 45 km from Chennai center"
        },
        "accommodation": {
            "budget": "₹800 - ₹1,400 / night (or stay in Chennai)"
        },
        "estimated_budget_per_day": "₹800 - ₹1,600 per person",
        "travel_tips": ["Visit Pulicat Lake in December or January to witness vast flocks of pink greater flamingos feeding in the shallow waters."],
        "emergency_contacts": {"police": "100", "ambulance": "108"}
    },

    "tiruvannamalai": {
        "name": "Tiruvannamalai",
        "district": "Tiruvannamalai",
        "category": "Spiritual Beacon, Fire Element & Girivalam",
        "tagline": "The Sacred Hill of Arunachala & Seat of Ramana Maharshi",
        "lat": 12.2253,
        "lon": 79.0747,
        "overview": "Tiruvannamalai is one of the most revered spiritual sanctuaries in India, centered on the holy Arunachala Hill and the sprawling Annamalaiyar Temple (Pancha Bhoota Sthalam for the Fire element - Agni). Famous for the 14 km Girivalam barefoot pradakshina around the hill and the Sri Ramana Ashram.",
        "ideal_duration": "1 to 2 days",
        "best_season": "October to March (Cooler weather, 20°C - 30°C)",
        "weather_notes": "Karthigai Deepam (Nov/Dec) lights a giant ghee beacon visible for 30 km.",
        "top_attractions": [
            {
                "name": "Arulmigu Arunachaleswarar (Annamalaiyar) Temple",
                "experience": "One of India's largest temples spanning 25 acres with 4 towering gopurams (Eastern tower 66 m high), 1000-pillar hall, and Agni Shiva Linga.",
                "duration": "2.5 hours",
                "entry_fee": "Free",
                "highlights": "Grand Dravidian gopurams, Thousand Pillar Hall, Pathala Lingam cave"
            },
            {
                "name": "Girivalam (Arunachala Circumambulation)",
                "experience": "14 km sacred barefoot walk circling Mount Arunachala along a forested path punctuated by 8 directional Ashta Lingams.",
                "duration": "3.5 - 4 hours",
                "entry_fee": "Free",
                "highlights": "Spiritual peace, 8 Ashta Lingams, view of Mount Arunachala"
            },
            {
                "name": "Sri Ramana Maharshi Ashram & Virupaksha Cave",
                "experience": "Peaceful ashram where Ramana taught Advaita Vedanta, plus the cave up the hill where he meditated for 17 years.",
                "duration": "2 hours",
                "entry_fee": "Free",
                "highlights": "Meditation hall silence, peacocks, Virupaksha cave climb"
            }
        ],
        "local_food": {
            "specialties": ["Ashram satvik meals", "Hot ghee roast dosas", "South Indian filter coffee", "International sourdough bakeries on Chengam road"],
            "iconic_eateries": ["The Dreaming Tree Restaurant", "Hotel Shakthi Pudhira", "Aakash Veg"]
        },
        "transport": {
            "railway": "Tiruvannamalai Railway Station (TNM)",
            "road": "Connected via state highways to Chennai (185 km), Bangalore (200 km), and Pondicherry (105 km)"
        },
        "accommodation": {
            "budget": "₹700 - ₹1,400 / night (near Ramana Ashram or Temple)",
            "mid_range": "₹2,000 - ₹3,800 / night (Arunai Anantha, Athena Hotel)",
            "luxury": "₹4,500 - ₹8,000 / night (Sparsa Resort)"
        },
        "estimated_budget_per_day": "₹900 - ₹2,000 per person",
        "travel_tips": ["On Pournami (Full Moon) nights, over 500,000 pilgrims perform Girivalam; advance hotel booking is essential."],
        "emergency_contacts": {"police": "100", "ambulance": "108"}
    },

    "tiruvarur": {
        "name": "Tiruvarur",
        "district": "Tiruvarur",
        "category": "Carnatic Musical Trinity & Chariot Wonder",
        "tagline": "The Land of Thyagaraja Temple, Mammoth Chariot & Musical Trinity",
        "lat": 10.7725,
        "lon": 79.6366,
        "overview": "Tiruvarur is a cultural bastion of Tamil Nadu, famous for the colossal Thyagaraja Temple with the largest temple chariot in Tamil Nadu (Aazhi Ther), the expansive Kamalalayam sacred tank, and as the birthplace of all three doyens of Carnatic music: Tyagaraja, Muthuswami Dikshitar, and Syama Sastri.",
        "ideal_duration": "1 day",
        "best_season": "October to March (20°C - 30°C)",
        "weather_notes": "Cauvery delta agriculture brings lush green paddy surroundings.",
        "top_attractions": [
            {
                "name": "Sri Thyagarajaswamy Temple & Kamalalayam Tank",
                "experience": "20-acre ancient temple complex with the famous 33-acre Kamalalayam sacred tank with a central island temple.",
                "duration": "2 hours",
                "entry_fee": "Free",
                "highlights": "Kamalalayam tank, Thyagaraja shrine, historic stone carvings"
            },
            {
                "name": "Aazhi Ther (The Grand Temple Chariot)",
                "experience": "The largest temple chariot in Asia, standing 96 feet high and weighing over 300 tonnes, pulled by thousands of devotees during the Chithirai festival.",
                "duration": "1 hour",
                "entry_fee": "Free",
                "highlights": "Mammoth wooden chariot carvings"
            },
            {
                "name": "Birthplaces of the Carnatic Music Trinity",
                "experience": "The historic homes of Saint Tyagaraja, Muthuswami Dikshitar, and Syama Sastri, all born in the same street in Tiruvarur.",
                "duration": "1 hour",
                "entry_fee": "Free",
                "highlights": "Carnatic musical heritage, museum exhibits"
            }
        ],
        "local_food": {
            "specialties": ["Traditional Cauvery delta full meals", "Tiruvarur special butter murukku", "Filter coffee"],
            "iconic_eateries": ["Hotel Selva", "Hotel Meenakshi", "Sri Krishna Bhavan"]
        },
        "transport": {
            "railway": "Tiruvarur Junction (TVR) connected with Chennai, Trichy, and Nagapattinam",
            "road": "Connected to Thanjavur (60 km), Kumbakonam (40 km), and Nagapattinam (25 km)"
        },
        "accommodation": {
            "budget": "₹800 - ₹1,400 / night"
        },
        "estimated_budget_per_day": "₹900 - ₹1,800 per person",
        "travel_tips": ["Combine Tiruvarur with Thanjavur and Kumbakonam for a rich temple and cultural heritage tour."],
        "emergency_contacts": {"police": "100", "ambulance": "108"}
    },

    "vellore": {
        "name": "Vellore",
        "district": "Vellore",
        "category": "Moated Stone Fort, Golden Temple & Biryani",
        "tagline": "The Fort City, Sripuram Golden Temple & Ambur Biryani",
        "lat": 12.9165,
        "lon": 79.1325,
        "overview": "Vellore is famous for its imposing 16th-century granite fort surrounded by a deep water moat, the historic Jalakandeswarar temple inside, the sparkling Sripuram Golden Temple gilded with 1,500 kg of pure gold, and the world-renowned Ambur Dum Biryani.",
        "ideal_duration": "1 to 2 days",
        "best_season": "October to March (20°C - 30°C)",
        "weather_notes": "Summers are warm; pleasant winter climate.",
        "top_attractions": [
            {
                "name": "Vellore Fort & Moat",
                "experience": "16th-century granite fortress built by Vijayanagara rulers with massive double stone walls and wide crocodile-infested moat, site of the 1806 Vellore Mutiny.",
                "duration": "2 hours",
                "entry_fee": "Free; ASI Museum ₹5",
                "highlights": "Moat walk, rampart cannons, Government Museum"
            },
            {
                "name": "Jalakandeswarar Temple (Inside Fort)",
                "experience": "Exquisite Vijayanagara temple with intricately sculpted stone pillars depicting mythical yalis, celestial dancers, and stone chains.",
                "duration": "1.5 hours",
                "entry_fee": "Free",
                "highlights": "Intricately carved stone pillars, monolithic sculptures"
            },
            {
                "name": "Sripuram Golden Temple (Malaikodi)",
                "experience": "Magnificent spiritual park and star-shaped path leading to a sanctum gilded with 1,500 kilograms of pure gold.",
                "duration": "2.5 hours",
                "entry_fee": "Free; Special Darshan ₹100 - ₹250",
                "highlights": "Pure gold-foil covered temple dome and sanctum, star-shaped path"
            }
        ],
        "local_food": {
            "specialties": ["World-famous Ambur Dum Biryani (Seeraga samba rice cooked with curd and whole spices)", "Vellore Mullu Murukku", "Ennai Kathirikai (Eggplant curry)"],
            "iconic_eateries": ["Star Biryani (Ambur / Vellore)", "Hotel Khanna", "Hotel Saravana Bhavan Vellore"]
        },
        "transport": {
            "railway": "Katpadi Junction (KPD - 6 km) - Major junction on Chennai-Bangalore line",
            "road": "Connected via 6-lane NH 48, 140 km from Chennai and 210 km from Bangalore"
        },
        "accommodation": {
            "budget": "₹800 - ₹1,500 / night",
            "mid_range": "₹2,200 - ₹4,200 / night (Fortune Park Vellore, Regency by GRT)"
        },
        "estimated_budget_per_day": "₹1,100 - ₹2,200 per person",
        "travel_tips": ["Electronic devices and phones are prohibited inside the Sripuram Golden Temple; use the secure cloakroom counters."],
        "emergency_contacts": {"police": "100", "ambulance": "108"}
    },

    "viluppuram": {
        "name": "Viluppuram (Villupuram)",
        "district": "Viluppuram",
        "category": "Troy of the East, Gingee Fort & Koovagam",
        "tagline": "The Troy of the East, Impregnable Gingee Fort & Historical Crossroads",
        "lat": 11.9401,
        "lon": 79.4861,
        "overview": "Viluppuram is home to Gingee Fort (Senji Fort), described by Shivaji as the 'most impregnable fortress in India' and by the British as the 'Troy of the East'. It also serves as the key railway crossroads of Tamil Nadu and gateway to Auroville and Pondicherry.",
        "ideal_duration": "1 to 2 days",
        "best_season": "October to March (20°C - 30°C)",
        "weather_notes": "Comfortable winter weather; avoid midday sun while climbing Gingee fort.",
        "top_attractions": [
            {
                "name": "Gingee Fort (Rajagiri & Krishnagiri)",
                "experience": "Monumental fortress complex spanning three sheer hillcitadels, featuring the 7-story Kalyana Mahal, granaries, and a drawbridge over a chasm.",
                "duration": "3-4 hours (Requires climbing stone stairs)",
                "entry_fee": "₹25 for ASI",
                "highlights": "7-story Kalyana Mahal, natural stone moat, Rajagiri summit views"
            },
            {
                "name": "Mailam Murugan Temple",
                "experience": "Hilltop shrine dedicated to Lord Murugan with ancient traditions, offering views of the surrounding cashew and mango orchards.",
                "duration": "1.5 hours",
                "entry_fee": "Free",
                "highlights": "Hilltop breezes, peacocks, spiritual sanctity"
            },
            {
                "name": "Thirukoilur Ulagalantha Perumal Temple",
                "experience": "Ancient Divya Desam temple dedicated to Lord Vishnu in the Trivikrama (Vamana) form with his foot raised to measure the sky.",
                "duration": "1.5 hours",
                "entry_fee": "Free",
                "highlights": "Giant Trivikrama idol, historical Sangam inscriptions"
            }
        ],
        "local_food": {
            "specialties": ["Gingee special roasted cashews and peanuts", "Village clay-pot country meals", "Crispy Medu Vadas at Viluppuram railway junction"],
            "iconic_eateries": ["Hotel Grand Kubera (Viluppuram)", "Gingee highway restaurants", "Railway Refreshment Room"]
        },
        "transport": {
            "railway": "Viluppuram Junction (VM) - One of Tamil Nadu's busiest railway junctions connecting Chennai to southern routes",
            "road": "Connected via NH 45 (GST Road), 160 km from Chennai and 40 km from Pondicherry"
        },
        "accommodation": {
            "budget": "₹800 - ₹1,400 / night (Viluppuram or Gingee lodges)"
        },
        "estimated_budget_per_day": "₹1,000 - ₹1,800 per person",
        "travel_tips": ["Start your climb of Gingee Fort early morning around 8:00 AM; carry water and wear sports shoes for the steep rock steps."],
        "emergency_contacts": {"police": "100", "ambulance": "108"}
    },

    "virudhunagar": {
        "name": "Virudhunagar",
        "district": "Virudhunagar",
        "category": "Culinary Oil Parotta, Temples & Freedom History",
        "tagline": "The City of Flaky Ennai Parotta, Kamarajar Memorial & Ayyanar Falls",
        "lat": 9.5680,
        "lon": 77.9624,
        "overview": "Virudhunagar is an energetic business and cultural hub in southern Tamil Nadu, celebrated for its legendary crispy shallow-fried Ennai Parotta, the memorial home of Bharat Ratna K. Kamaraj, the ancient Andal Temple in Srivilliputhur (whose gopuram is the official emblem of Tamil Nadu), and the serene Ayyanar Falls in Rajapalayam.",
        "ideal_duration": "1 to 2 days",
        "best_season": "October to March (21°C - 30°C)",
        "weather_notes": "Pleasant in winter; rich cultural festivals in Srivilliputhur.",
        "top_attractions": [
            {
                "name": "Srivilliputhur Andal Temple",
                "experience": "Birthplace of saint-poetess Andal, featuring the magnificent 11-tier 192-foot Rajagopuram that serves as the official state emblem of the Government of Tamil Nadu.",
                "duration": "2 hours",
                "entry_fee": "Free",
                "highlights": "Official emblem Rajagopuram, Andal sanctum, sacred floral garlands"
            },
            {
                "name": "Ayyanar Falls (Rajapalayam)",
                "experience": "Cascading forest waterfall tucked inside the foothills of the Western Ghats, safe for bathing and family picnics.",
                "duration": "2.5 hours",
                "entry_fee": "Free",
                "highlights": "Lush forest setting, clear cool mountain stream, trekking"
            },
            {
                "name": "Kamarajar Memorial House",
                "experience": "The modest ancestral home of Bharat Ratna K. Kamaraj, former Chief Minister of Tamil Nadu and kingmaker of Indian politics.",
                "duration": "1 hour",
                "entry_fee": "Free",
                "highlights": "Rare photographs, personal artifacts of Kamaraj"
            },
            {
                "name": "Kullursandai Dam & Reservoir",
                "experience": "Scenic reservoir with landscaped gardens, home to local and migratory winter waterbirds.",
                "duration": "1.5 hours",
                "entry_fee": "Free",
                "highlights": "Water breeze, birdwatching, sunset strolls"
            }
        ],
        "local_food": {
            "specialties": ["World-famous Virudhunagar Ennai Parotta (flaky shallow-fried parotta served with spicy salna)", "Srivilliputhur Palkova (GI-tagged slow-simmered rich milk sweet)", "Chettinad style mutton chukka"],
            "iconic_eateries": ["Barmas Parotta Stall (Virudhunagar)", "Sri Venkateswara Palkova (Srivilliputhur)", "Hotel Park Gate"]
        },
        "transport": {
            "railway": "Virudhunagar Junction (VPT) - Major junction connecting Madurai, Tenkasi, and Tirunelveli",
            "road": "Strategically located on NH 44, 45 km south of Madurai",
            "airport": "Madurai Airport (45 km)"
        },
        "accommodation": {
            "budget": "₹800 - ₹1,400 / night",
            "mid_range": "₹1,800 - ₹3,500 / night"
        },
        "estimated_budget_per_day": "₹1,000 - ₹2,000 per person",
        "travel_tips": ["Taste genuine GI-tagged Srivilliputhur Palkova made purely with reduced milk and sugar, available right outside the Andal temple."],
        "emergency_contacts": {"police": "100", "ambulance": "108"}
    }
}

# Quick lookup index
DESTINATION_BY_NAME = {k.lower(): v for k, v in DESTINATIONS.items()}

# Aliases and district name mappings
ALIASES = {
    "madras": "chennai",
    "kovai": "coimbatore",
    "udhagai": "nilgiris",
    "udhagamandalam": "nilgiris",
    "ooty": "nilgiris",
    "coonoor": "nilgiris",
    "kotagiri": "nilgiris",
    "kodai": "dindigul",
    "kodaikanal": "dindigul",
    "palani": "dindigul",
    "tanjore": "thanjavur",
    "trichy": "tiruchirappalli",
    "nellai": "tirunelveli",
    "courtallam": "tenkasi",
    "kutralam": "tenkasi",
    "tuticorin": "thoothukudi",
    "dhanushkodi": "ramanathapuram",
    "rameswaram": "ramanathapuram",
    "rameshwaram": "ramanathapuram",
    "yercaud": "salem",
    "yelagiri": "tirupathur",
    "valparai": "coimbatore",
    "pollachi": "coimbatore",
    "mahabalipuram": "chengalpattu",
    "mamallapuram": "chengalpattu",
    "kanchi": "kancheepuram",
    "kanchipuram": "kancheepuram",
    "cape comorin": "kanniyakumari",
    "kanyakumari": "kanniyakumari",
    "karaikudi": "sivaganga",
    "chettinad": "sivaganga",
    "chidambaram": "cuddalore",
    "pichavaram": "cuddalore",
    "hogenakkal": "dharmapuri",
    "velankanni": "nagapattinam",
    "mudumalai": "nilgiris",
    "gangaikonda cholapuram": "ariyalur",
    "tarangambadi": "mayiladuthurai",
    "tranquebar": "mayiladuthurai",
    "poompuhar": "mayiladuthurai",
    "srivilliputhur": "virudhunagar",
    "rajapalayam": "virudhunagar",
    "megamalai": "theni",
    "gingee": "viluppuram",
    "senji": "viluppuram",
    "arcot": "ranipet",
    "kolli hills": "namakkal",
    "bhavani": "erode",
    "kalvarayan": "kallakurichi",
    "sittannavasal": "pudukkottai"
}

for alias, target in ALIASES.items():
    if target in DESTINATIONS:
        DESTINATION_BY_NAME[alias] = DESTINATIONS[target]

def get_destination_data(name: str) -> Optional[Dict[str, Any]]:
    key = name.strip().lower()
    return DESTINATION_BY_NAME.get(key)

def list_all_destinations() -> List[Dict[str, Any]]:
    """Returns catalog of all 38 districts of Tamil Nadu."""
    return [
        {
            "id": k,
            "name": v["name"],
            "district": v["district"],
            "category": v["category"],
            "tagline": v["tagline"],
            "best_season": v["best_season"],
            "ideal_duration": v["ideal_duration"],
            "lat": v["lat"],
            "lon": v["lon"]
        }
        for k, v in DESTINATIONS.items()
    ]
