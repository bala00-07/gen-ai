import React, { useState, useEffect } from 'react'
import { X, MapPin, Search, Mountain, Landmark, Trees, Waves } from 'lucide-react'
import type { DestinationSummary } from '../types'

interface DestinationDrawerProps {
  isOpen: boolean
  onClose: () => void
  onSelectDestination: (destName: string) => void
}

export const DestinationDrawer: React.FC<DestinationDrawerProps> = ({
  isOpen,
  onClose,
  onSelectDestination
}) => {
  const [destinations, setDestinations] = useState<DestinationSummary[]>([])
  const [search, setSearch] = useState('')
  const [selectedCategory, setSelectedCategory] = useState<string>('all')
  const [loading, setLoading] = useState(false)

  useEffect(() => {
    if (isOpen && destinations.length === 0) {
      setLoading(true)
      fetch('/api/destinations')
        .then((res) => res.json())
        .then((data) => {
          if (data.destinations) {
            setDestinations(data.destinations)
          }
        })
        .catch((err) => console.error('Failed to load destinations', err))
        .finally(() => setLoading(false))
    }
  }, [isOpen, destinations.length])

  if (!isOpen) return null

  const categories = [
    { id: 'all', label: 'All Destinations', icon: MapPin },
    { id: 'hill', label: 'Hill Stations', icon: Mountain },
    { id: 'temple', label: 'Heritage & Temples', icon: Landmark },
    { id: 'nature', label: 'Nature & Wildlife', icon: Trees },
    { id: 'coastal', label: 'Coastal & Beaches', icon: Waves },
  ]

  const filtered = destinations.filter((dest) => {
    const matchesSearch =
      dest.name.toLowerCase().includes(search.toLowerCase()) ||
      dest.district.toLowerCase().includes(search.toLowerCase()) ||
      dest.tagline.toLowerCase().includes(search.toLowerCase())

    if (!matchesSearch) return false

    if (selectedCategory === 'all') return true
    if (selectedCategory === 'hill') return dest.category.toLowerCase().includes('hill')
    if (selectedCategory === 'temple') return dest.category.toLowerCase().includes('temple') || dest.category.toLowerCase().includes('heritage')
    if (selectedCategory === 'nature') return dest.category.toLowerCase().includes('wildlife') || dest.category.toLowerCase().includes('nature') || dest.category.toLowerCase().includes('ecotourism')
    if (selectedCategory === 'coastal') return dest.category.toLowerCase().includes('coastal') || dest.category.toLowerCase().includes('beach') || dest.category.toLowerCase().includes('island')

    return true
  })

  return (
    <div className="fixed inset-0 z-50 flex justify-end bg-black/60 backdrop-blur-sm transition-opacity">
      <div className="w-full max-w-md h-full bg-slate-900 border-l border-slate-800 flex flex-col shadow-2xl animate-in slide-in-from-right duration-200">
        {/* Drawer Header */}
        <div className="p-4 border-b border-slate-800 flex items-center justify-between">
          <div className="flex items-center gap-2">
            <div className="p-1.5 rounded-lg bg-amber-500/20 text-amber-400">
              <MapPin className="w-5 h-5" />
            </div>
            <div>
              <h3 className="font-bold text-white text-base">Tamil Nadu Travel Hubs</h3>
              <p className="text-xs text-slate-400">All 38 Districts & Verified Tourist Hubs</p>
            </div>
          </div>
          <button
            onClick={onClose}
            className="p-1.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Search Bar */}
        <div className="p-4 border-b border-slate-800 space-y-3">
          <div className="relative">
            <Search className="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-slate-400" />
            <input
              type="text"
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              placeholder="Search destination, district, or style..."
              className="w-full pl-9 pr-3 py-2 text-xs rounded-lg glass-input text-slate-200 placeholder-slate-500 focus:outline-none"
            />
          </div>

          {/* Category Filter Pills */}
          <div className="flex gap-1.5 overflow-x-auto pb-1 scrollbar-none">
            {categories.map((cat) => (
              <button
                key={cat.id}
                onClick={() => setSelectedCategory(cat.id)}
                className={`px-2.5 py-1 text-[11px] font-medium rounded-full whitespace-nowrap transition ${
                  selectedCategory === cat.id
                    ? 'bg-amber-500 text-slate-950 font-bold'
                    : 'bg-slate-800 text-slate-300 hover:bg-slate-700'
                }`}
              >
                {cat.label}
              </button>
            ))}
          </div>
        </div>

        {/* Destination List */}
        <div className="flex-1 overflow-y-auto p-4 space-y-2.5">
          {loading ? (
            <div className="text-center py-12 text-slate-400 text-xs">
              Loading Tamil Nadu destinations...
            </div>
          ) : filtered.length === 0 ? (
            <div className="text-center py-12 text-slate-400 text-xs">
              No destinations matching your search.
            </div>
          ) : (
            filtered.map((dest) => (
              <div
                key={dest.id}
                onClick={() => {
                  onSelectDestination(`What are the top things to do and travel tips for ${dest.name}?`)
                  onClose()
                }}
                className="p-3 rounded-xl glass-card hover:bg-slate-800/80 border border-slate-800 hover:border-amber-500/40 cursor-pointer transition group"
              >
                <div className="flex items-center justify-between">
                  <h4 className="font-bold text-slate-100 group-hover:text-amber-400 transition text-sm">
                    {dest.name}
                  </h4>
                  <span className="text-[10px] uppercase font-bold tracking-wider px-2 py-0.5 rounded-full bg-slate-800 text-amber-300 border border-slate-700">
                    {dest.district}
                  </span>
                </div>
                <p className="text-xs text-slate-400 mt-1 line-clamp-1 italic">
                  {dest.tagline}
                </p>
                <div className="flex items-center justify-between text-[11px] text-slate-400 mt-2 pt-2 border-t border-slate-800/60">
                  <span>Best Time: {dest.best_season.split('(')[0]}</span>
                  <span className="text-amber-400 font-medium">Ask Guide &rarr;</span>
                </div>
              </div>
            ))
          )}
        </div>
      </div>
    </div>
  )
}
