export type Language = 'auto' | 'english' | 'tamil' | 'tanglish'

export interface DestinationCardData {
  id: string
  name: string
  district: string
  category: string
  tagline: string
  overview: string
  best_season: string
  ideal_duration: string
  attractions_count?: number
  estimated_budget_per_day?: string
}

export interface DayActivity {
  time: string
  title: string
  activity: string
  duration: string
  entry_fee: string
  travel_transit: string
  highlights?: string
}

export interface ItineraryDay {
  day: number
  theme: string
  morning: DayActivity
  afternoon: DayActivity
  evening: DayActivity
  meals: {
    breakfast: string
    lunch: string
    dinner: string
  }
  practical_notes: string[]
}

export interface BudgetBreakdownItem {
  amount: number
  notes: string
}

export interface BudgetSummary {
  destination: string
  days: number
  nights: number
  travellers: number
  rooms: number
  travel_style: string
  breakdown: Record<string, BudgetBreakdownItem>
  total_estimated: number
  cost_per_person: number
  user_budget_limit?: number | null
  remaining_budget?: number | null
  is_within_budget?: boolean | null
  assumptions: string[]
}

export interface ItineraryCardData {
  destination: string
  district: string
  days_count: number
  preferences_applied: Record<string, boolean>
  days: ItineraryDay[]
  budget_summary?: BudgetSummary
  travel_tips?: string[]
  emergency_contacts?: Record<string, string>
}

export interface LiveWeatherData {
  destination: string
  district: string
  temperature_c: number
  feels_like_c?: number
  condition: string
  humidity_pct?: number
  wind_speed_kmh?: number
  forecast_max_c?: number
  forecast_min_c?: number
  rain_probability_pct?: number
  travel_advice?: string
  source?: string
}

export interface Message {
  id: string
  role: 'user' | 'assistant'
  content: string
  language?: string
  is_out_of_scope?: boolean
  destination_card?: DestinationCardData | null
  itinerary_card?: ItineraryCardData | null
  budget_card?: BudgetSummary | null
  live_weather?: LiveWeatherData | null
  follow_up_suggestions?: string[]
  timestamp: string
}

export interface DestinationSummary {
  id: string
  name: string
  district: string
  category: string
  tagline: string
  best_season: string
  ideal_duration: string
  lat: number
  lon: number
}
