import React, { useState } from 'react'
import ReactMarkdown from 'react-markdown'
import remarkGfm from 'remark-gfm'
import {
  Compass,
  Calendar,
  CloudSun,
  Coins,
  ShieldCheck,
  Clock,
  ArrowRight,
  AlertTriangle,
  ChevronDown,
  ChevronUp
} from 'lucide-react'
import type { Message } from '../types'

interface ChatMessageProps {
  message: Message
  onSelectFollowUp: (prompt: string) => void
}

export const ChatMessage: React.FC<ChatMessageProps> = ({ message, onSelectFollowUp }) => {
  const isUser = message.role === 'user'
  const [selectedDay, setSelectedDay] = useState<number>(1)
  const [showTips, setShowTips] = useState<boolean>(false)

  if (isUser) {
    return (
      <div className="flex justify-end mb-5">
        <div className="max-w-[85%] sm:max-w-[70%] rounded-2xl rounded-tr-sm bg-gradient-to-r from-amber-600 to-amber-500 text-slate-950 font-medium px-4 py-3 shadow-md shadow-amber-500/10">
          <p className="whitespace-pre-wrap text-sm leading-relaxed">{message.content}</p>
          <span className="block text-[10px] text-amber-950/70 text-right mt-1 font-semibold">
            {message.timestamp}
          </span>
        </div>
      </div>
    )
  }

  // Assistant Message
  const destCard = message.destination_card
  const itinCard = message.itinerary_card
  const budgetCard = message.budget_card
  const weather = message.live_weather

  return (
    <div className="flex gap-3 mb-6 max-w-4xl">
      {/* Bot Avatar */}
      <div className="w-8 h-8 rounded-lg bg-gradient-to-br from-amber-500 to-yellow-400 flex items-center justify-center shrink-0 shadow-md shadow-amber-500/20 text-slate-950">
        <Compass className="w-4 h-4" />
      </div>

      <div className="flex-1 space-y-4 overflow-hidden">
        {/* Out of scope alert banner */}
        {message.is_out_of_scope && (
          <div className="flex items-start gap-2.5 p-3 rounded-xl bg-amber-500/10 border border-amber-500/20 text-amber-200 text-xs">
            <AlertTriangle className="w-4 h-4 text-amber-400 shrink-0 mt-0.5" />
            <div>
              <p className="font-semibold text-amber-300">Dedicated Scope: Tamil Nadu Tourism</p>
              <p className="text-slate-300 mt-0.5 leading-relaxed">
                I am specialized exclusively in Tamil Nadu travel, destinations, culture, and trip planning.
              </p>
            </div>
          </div>
        )}

        {/* Live Weather Widget Badge */}
        {weather && (
          <div className="p-3.5 rounded-xl glass-card border border-sky-500/30 bg-gradient-to-r from-sky-950/40 via-slate-900/60 to-slate-900/40 flex flex-wrap items-center justify-between gap-3 text-xs">
            <div className="flex items-center gap-2.5">
              <div className="p-2 rounded-lg bg-sky-500/20 text-sky-300">
                <CloudSun className="w-5 h-5 text-sky-400" />
              </div>
              <div>
                <div className="flex items-center gap-2">
                  <span className="font-bold text-sky-200 text-sm">
                    {weather.destination} Weather: {weather.temperature_c}°C
                  </span>
                  <span className="text-[11px] px-2 py-0.5 rounded-full bg-sky-500/20 text-sky-300 font-medium">
                    {weather.condition}
                  </span>
                </div>
                <p className="text-slate-400 text-[11px] mt-0.5">
                  Rain likelihood: {weather.rain_probability_pct}% | Expected: {weather.forecast_min_c}°C to {weather.forecast_max_c}°C
                </p>
              </div>
            </div>
            {weather.travel_advice && (
              <div className="text-[11px] text-sky-200/90 italic bg-sky-950/60 px-2.5 py-1 rounded-md border border-sky-500/20 max-w-sm">
                💡 {weather.travel_advice}
              </div>
            )}
          </div>
        )}

        {/* Destination Card Summary */}
        {destCard && (
          <div className="p-4 rounded-xl glass-card border border-amber-500/30 bg-gradient-to-br from-slate-900/80 via-slate-900/60 to-amber-950/20">
            <div className="flex items-start justify-between gap-2">
              <div>
                <div className="flex items-center gap-2">
                  <span className="text-xs uppercase font-bold tracking-wider text-amber-400">
                    {destCard.category}
                  </span>
                  <span className="text-slate-500">•</span>
                  <span className="text-xs text-slate-400">{destCard.district} District</span>
                </div>
                <h3 className="text-lg font-bold text-white mt-0.5">{destCard.name}</h3>
                <p className="text-xs text-amber-300/80 italic mt-0.5">{destCard.tagline}</p>
              </div>
              <div className="text-right shrink-0">
                <span className="text-[11px] block text-slate-400">Best Season</span>
                <span className="text-xs font-semibold text-emerald-400">{destCard.best_season.split('(')[0]}</span>
              </div>
            </div>

            <p className="text-xs text-slate-300 mt-2.5 leading-relaxed line-clamp-3">
              {destCard.overview}
            </p>

            <div className="grid grid-cols-2 sm:grid-cols-3 gap-2 mt-3 pt-3 border-t border-white/5 text-[11px]">
              <div>
                <span className="text-slate-400 block">Ideal Duration:</span>
                <span className="font-medium text-slate-200">{destCard.ideal_duration}</span>
              </div>
              <div>
                <span className="text-slate-400 block">Est. Daily Budget:</span>
                <span className="font-medium text-amber-300">{destCard.estimated_budget_per_day}</span>
              </div>
              <div className="col-span-2 sm:col-span-1">
                <span className="text-slate-400 block">Key Attractions:</span>
                <span className="font-medium text-slate-200">{destCard.attractions_count || 'Top'} Verified spots</span>
              </div>
            </div>
          </div>
        )}

        {/* Structured Itinerary Day-by-Day Card */}
        {itinCard && itinCard.days && itinCard.days.length > 0 && (
          <div className="rounded-xl glass-card border border-amber-500/20 overflow-hidden">
            {/* Header */}
            <div className="p-3.5 bg-slate-800/80 border-b border-white/5 flex flex-wrap items-center justify-between gap-2">
              <div className="flex items-center gap-2">
                <Calendar className="w-4 h-4 text-amber-400" />
                <h4 className="text-sm font-bold text-white">
                  {itinCard.destination} — {itinCard.days_count} Day Detailed Itinerary
                </h4>
              </div>

              {/* Day Switcher Tabs */}
              <div className="flex items-center gap-1 bg-slate-900/80 p-0.5 rounded-lg border border-slate-700/50">
                {itinCard.days.map((d) => (
                  <button
                    key={d.day}
                    onClick={() => setSelectedDay(d.day)}
                    className={`px-2.5 py-1 text-xs font-semibold rounded-md transition ${
                      selectedDay === d.day
                        ? 'bg-amber-500 text-slate-950 shadow-sm'
                        : 'text-slate-400 hover:text-slate-200'
                    }`}
                  >
                    Day {d.day}
                  </button>
                ))}
              </div>
            </div>

            {/* Active Day Activities */}
            {(() => {
              const activeDayData = itinCard.days.find((d) => d.day === selectedDay) || itinCard.days[0]
              return (
                <div className="p-4 space-y-3.5">
                  <div className="text-xs font-semibold text-amber-300 border-l-2 border-amber-500 pl-2">
                    {activeDayData.theme}
                  </div>

                  {/* Morning */}
                  <div className="p-3 rounded-lg bg-slate-900/50 border border-slate-800/80 flex flex-col gap-1 text-xs">
                    <div className="flex items-center justify-between">
                      <span className="font-bold text-amber-400 flex items-center gap-1.5">
                        <Clock className="w-3.5 h-3.5" />
                        Morning (காலை): {activeDayData.morning.time}
                      </span>
                      <span className="text-[11px] text-slate-400 font-medium">
                        {activeDayData.morning.duration}
                      </span>
                    </div>
                    <div className="font-semibold text-slate-100 text-sm mt-0.5">
                      {activeDayData.morning.title}
                    </div>
                    <p className="text-slate-300 leading-relaxed">
                      {activeDayData.morning.activity}
                    </p>
                    <div className="flex flex-wrap items-center gap-3 text-[11px] text-slate-400 mt-1 pt-1 border-t border-slate-800">
                      <span>🎟️ Entry: <strong className="text-slate-200">{activeDayData.morning.entry_fee}</strong></span>
                      <span>🚗 Transit: {activeDayData.morning.travel_transit}</span>
                    </div>
                  </div>

                  {/* Afternoon */}
                  <div className="p-3 rounded-lg bg-slate-900/50 border border-slate-800/80 flex flex-col gap-1 text-xs">
                    <div className="flex items-center justify-between">
                      <span className="font-bold text-sky-400 flex items-center gap-1.5">
                        <Clock className="w-3.5 h-3.5" />
                        Afternoon (மதியம்): {activeDayData.afternoon.time}
                      </span>
                      <span className="text-[11px] text-slate-400 font-medium">
                        {activeDayData.afternoon.duration}
                      </span>
                    </div>
                    <div className="font-semibold text-slate-100 text-sm mt-0.5">
                      {activeDayData.afternoon.title}
                    </div>
                    <p className="text-slate-300 leading-relaxed">
                      {activeDayData.afternoon.activity}
                    </p>
                    <div className="flex flex-wrap items-center gap-3 text-[11px] text-slate-400 mt-1 pt-1 border-t border-slate-800">
                      <span>🎟️ Entry: <strong className="text-slate-200">{activeDayData.afternoon.entry_fee}</strong></span>
                      <span>🚗 Transit: {activeDayData.afternoon.travel_transit}</span>
                    </div>
                  </div>

                  {/* Evening */}
                  <div className="p-3 rounded-lg bg-slate-900/50 border border-slate-800/80 flex flex-col gap-1 text-xs">
                    <div className="flex items-center justify-between">
                      <span className="font-bold text-purple-400 flex items-center gap-1.5">
                        <Clock className="w-3.5 h-3.5" />
                        Evening (மாலை): {activeDayData.evening.time}
                      </span>
                      <span className="text-[11px] text-slate-400 font-medium">
                        {activeDayData.evening.duration}
                      </span>
                    </div>
                    <div className="font-semibold text-slate-100 text-sm mt-0.5">
                      {activeDayData.evening.title}
                    </div>
                    <p className="text-slate-300 leading-relaxed">
                      {activeDayData.evening.activity}
                    </p>
                  </div>

                  {/* Dining Recommendation */}
                  <div className="p-2.5 rounded-lg bg-amber-500/10 border border-amber-500/20 text-xs">
                    <span className="font-bold text-amber-300 block mb-1">
                      🍛 Curated Meal Recommendations:
                    </span>
                    <ul className="text-slate-300 space-y-0.5">
                      <li>• <strong>Breakfast:</strong> {activeDayData.meals.breakfast}</li>
                      <li>• <strong>Lunch:</strong> {activeDayData.meals.lunch}</li>
                      <li>• <strong>Dinner:</strong> {activeDayData.meals.dinner}</li>
                    </ul>
                  </div>

                  {/* Practical Notes Toggle */}
                  {activeDayData.practical_notes && activeDayData.practical_notes.length > 0 && (
                    <div className="text-xs">
                      <button
                        onClick={() => setShowTips(!showTips)}
                        className="text-slate-400 hover:text-amber-400 font-medium flex items-center gap-1 transition"
                      >
                        <span>{showTips ? 'Hide' : 'View'} Day {selectedDay} practical tips</span>
                        {showTips ? <ChevronUp className="w-3.5 h-3.5" /> : <ChevronDown className="w-3.5 h-3.5" />}
                      </button>
                      {showTips && (
                        <ul className="mt-2 pl-4 list-disc text-slate-300 space-y-1">
                          {activeDayData.practical_notes.map((tip, idx) => (
                            <li key={idx}>{tip}</li>
                          ))}
                        </ul>
                      )}
                    </div>
                  )}
                </div>
              )
            })()}
          </div>
        )}

        {/* Deterministic Budget Breakdown Card */}
        {budgetCard && budgetCard.breakdown && (
          <div className="p-4 rounded-xl glass-card border border-emerald-500/30 bg-gradient-to-br from-slate-900/90 via-slate-900/70 to-emerald-950/20 text-xs">
            <div className="flex items-center justify-between pb-2.5 border-b border-white/5 mb-3">
              <div className="flex items-center gap-2">
                <Coins className="w-4 h-4 text-emerald-400" />
                <h4 className="font-bold text-white text-sm">
                  Estimated Travel Budget ({budgetCard.destination})
                </h4>
              </div>
              <span className="text-[11px] font-semibold px-2 py-0.5 rounded-full bg-emerald-500/20 text-emerald-300">
                {budgetCard.travellers} Travellers • {budgetCard.days} Days
              </span>
            </div>

            {/* Breakdown Table */}
            <div className="overflow-x-auto">
              <table className="w-full text-left">
                <thead>
                  <tr className="border-b border-white/10 text-slate-400 text-[11px]">
                    <th className="py-1">Expense Category</th>
                    <th className="py-1">Estimate</th>
                    <th className="py-1 hidden sm:table-cell">Basis / Notes</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-white/5 text-slate-200">
                  {Object.entries(budgetCard.breakdown).map(([key, item]) => (
                    <tr key={key}>
                      <td className="py-1.5 font-medium text-slate-300 capitalize">
                        {key.replace('_', ' ')}
                      </td>
                      <td className="py-1.5 font-bold text-emerald-400">
                        ₹{item.amount.toLocaleString()}
                      </td>
                      <td className="py-1.5 text-slate-400 text-[11px] hidden sm:table-cell">
                        {item.notes}
                      </td>
                    </tr>
                  ))}
                  <tr className="border-t-2 border-emerald-500/40 text-sm font-bold">
                    <td className="py-2 text-white">Total Estimated Cost</td>
                    <td className="py-2 text-emerald-300">₹{budgetCard.total_estimated.toLocaleString()}</td>
                    <td className="py-2 text-slate-400 text-[11px] hidden sm:table-cell">
                      Approx ₹{budgetCard.cost_per_person.toLocaleString()} per person
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>

            {/* Budget limit status if specified */}
            {budgetCard.user_budget_limit && (
              <div className={`mt-3 p-2 rounded-lg font-medium flex items-center justify-between ${
                budgetCard.is_within_budget
                  ? 'bg-emerald-500/10 text-emerald-300 border border-emerald-500/30'
                  : 'bg-rose-500/10 text-rose-300 border border-rose-500/30'
              }`}>
                <span>Your Budget: ₹{budgetCard.user_budget_limit.toLocaleString()}</span>
                <span>
                  {budgetCard.is_within_budget
                    ? `✓ Within Budget (Surplus: ₹${budgetCard.remaining_budget?.toLocaleString()})`
                    : `⚠️ Exceeds Budget by ₹${Math.abs(budgetCard.remaining_budget || 0).toLocaleString()}`}
                </span>
              </div>
            )}
          </div>
        )}

        {/* Formatted Markdown Content */}
        <div className="p-4 rounded-2xl rounded-tl-sm glass-panel text-slate-200 prose-custom text-sm leading-relaxed shadow-sm">
          <ReactMarkdown remarkPlugins={[remarkGfm]}>
            {message.content}
          </ReactMarkdown>

          {/* Source footer */}
          <div className="mt-3 pt-3 border-t border-white/5 flex items-center justify-between text-[11px] text-slate-400">
            <span className="flex items-center gap-1 text-slate-400">
              <ShieldCheck className="w-3.5 h-3.5 text-amber-400" />
              Verified Tamil Nadu Tourism Data
            </span>
            <span>{message.timestamp}</span>
          </div>
        </div>

        {/* Dynamic Follow-up Suggestions */}
        {message.follow_up_suggestions && message.follow_up_suggestions.length > 0 && (
          <div className="flex flex-wrap gap-1.5 pt-1">
            {message.follow_up_suggestions.map((suggestion, index) => (
              <button
                key={index}
                onClick={() => onSelectFollowUp(suggestion)}
                className="text-xs px-3 py-1.5 rounded-full glass-card hover:bg-amber-500/20 text-slate-300 hover:text-amber-300 border border-slate-700 hover:border-amber-500/40 transition shadow-sm flex items-center gap-1.5"
              >
                <span>{suggestion}</span>
                <ArrowRight className="w-3 h-3 text-amber-400/80" />
              </button>
            ))}
          </div>
        )}
      </div>
    </div>
  )
}
