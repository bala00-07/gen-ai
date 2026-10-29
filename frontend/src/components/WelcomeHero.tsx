import React from 'react'
import {
  Compass,
  MapPin,
  Calendar,
  Utensils,
  Landmark,
  Trees,
  Coins,
  Sparkles
} from 'lucide-react'

interface WelcomeHeroProps {
  onSelectPrompt: (prompt: string) => void
}

export const WelcomeHero: React.FC<WelcomeHeroProps> = ({ onSelectPrompt }) => {
  const suggestedPrompts = [
    {
      title: 'Best Places in Coimbatore',
      subtitle: 'Adiyogi, Marudhamalai & Siruvani',
      icon: MapPin,
      color: 'from-amber-500/20 to-amber-600/10 text-amber-400 border-amber-500/30',
      query: 'What are the best tourist places in Coimbatore?'
    },
    {
      title: 'Plan Trip Within ₹3,000',
      subtitle: 'Personalized 2-Day budget itinerary',
      icon: Coins,
      color: 'from-emerald-500/20 to-teal-600/10 text-emerald-400 border-emerald-500/30',
      query: 'Plan a two-day trip within ₹3,000.'
    },
    {
      title: 'Ooty vs Kodaikanal',
      subtitle: 'Which hill station is better for you?',
      icon: Sparkles,
      color: 'from-blue-500/20 to-indigo-600/10 text-blue-400 border-blue-500/30',
      query: 'Which is better: Ooty or Kodaikanal?'
    },
    {
      title: 'Attractions in Ariyalur',
      subtitle: 'Gangaikonda Cholapuram & Fossils',
      icon: Landmark,
      color: 'from-purple-500/20 to-pink-600/10 text-purple-400 border-purple-500/30',
      query: 'Tell me about tourist attractions in Ariyalur.'
    },
    {
      title: 'Explore Mayiladuthurai',
      subtitle: 'Tarangambadi Danish Fort & Poompuhar',
      icon: Trees,
      color: 'from-emerald-500/20 to-teal-600/10 text-emerald-400 border-emerald-500/30',
      query: 'What can I explore in Mayiladuthurai?'
    },
    {
      title: 'Gems in Virudhunagar',
      subtitle: 'Ayyanar Falls & Ennai Parotta',
      icon: Sparkles,
      color: 'from-pink-500/20 to-rose-600/10 text-pink-400 border-pink-500/30',
      query: 'Suggest hidden gems in Virudhunagar.'
    },
    {
      title: 'Madurai Traditional Food',
      subtitle: 'Jigarthanda, Kari Dosa & Bun Parotta',
      icon: Utensils,
      color: 'from-orange-500/20 to-amber-600/10 text-orange-400 border-orange-500/30',
      query: 'What traditional food should I try in Madurai?'
    },
    {
      title: 'Chennai to Kanyakumari',
      subtitle: 'Train routes, Vande Bharat & road',
      icon: Calendar,
      color: 'from-cyan-500/20 to-sky-600/10 text-cyan-400 border-cyan-500/30',
      query: 'How can I travel from Chennai to Kanyakumari?'
    }
  ]

  return (
    <div className="max-w-4xl mx-auto px-4 py-8 sm:py-12 flex flex-col items-center text-center">
      {/* Visual Badge */}
      <div className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-amber-500/10 border border-amber-500/30 text-amber-300 text-xs font-semibold mb-6 shadow-sm">
        <Compass className="w-4 h-4 text-amber-400" />
        <span>Dedicated Exclusively to Tamil Nadu • Covers All 38 Districts</span>
      </div>

      {/* Main Welcome Title */}
      <h2 className="text-3xl sm:text-4xl font-extrabold tracking-tight mb-4 text-white">
        வணக்கம்! Welcome to <span className="bg-gradient-to-r from-amber-400 to-yellow-300 bg-clip-text text-transparent">Coimbatore & TN Travel Guide Bot</span>
      </h2>

      {/* Structured Welcome Text */}
      <p className="text-slate-300 text-sm sm:text-base max-w-2xl leading-relaxed mb-8">
        I'm your ChatGPT-like guide for Tamil Nadu tourism across all 38 districts. Ask any question in natural language about destinations, local food, routes, budgets, or custom trip itineraries!
      </p>

      <div className="w-16 h-0.5 bg-gradient-to-r from-transparent via-amber-500/50 to-transparent mb-8"></div>

      <p className="text-xs uppercase font-bold tracking-widest text-slate-400 mb-4">
        Where would you like to explore?
      </p>

      {/* 8 Suggested Prompt Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3 w-full text-left">
        {suggestedPrompts.map((item, index) => {
          const Icon = item.icon
          return (
            <button
              key={index}
              onClick={() => onSelectPrompt(item.query)}
              className="group p-3.5 rounded-xl glass-card hover:bg-slate-800/90 border transition-all duration-200 hover:-translate-y-0.5 flex flex-col justify-between hover:border-amber-500/40"
            >
              <div className="flex items-center justify-between mb-2">
                <div className={`p-2 rounded-lg bg-gradient-to-br ${item.color} border`}>
                  <Icon className="w-4 h-4" />
                </div>
                <span className="text-[11px] font-medium text-slate-500 group-hover:text-amber-400 transition">
                  Ask AI &rarr;
                </span>
              </div>
              <div>
                <h3 className="text-sm font-semibold text-slate-100 group-hover:text-amber-300 transition">
                  {item.title}
                </h3>
                <p className="text-xs text-slate-400 line-clamp-2 mt-0.5">
                  {item.subtitle}
                </p>
              </div>
            </button>
          )
        })}
      </div>
    </div>
  )
}
export default WelcomeHero
