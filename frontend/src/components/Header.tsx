import React from 'react'
import { Compass, Globe, RotateCcw, MapPin, Settings, Sparkles } from 'lucide-react'
import type { Language } from '../types'

interface HeaderProps {
  language: Language
  onLanguageChange: (lang: Language) => void
  onNewChat: () => void
  onOpenDestinations: () => void
  onOpenSettings: () => void
  engineMode?: string
}

export const Header: React.FC<HeaderProps> = ({
  language,
  onLanguageChange,
  onNewChat,
  onOpenDestinations,
  onOpenSettings,
  engineMode
}) => {
  return (
    <header className="sticky top-0 z-30 glass-panel border-b border-amber-500/20 px-4 py-3 sm:px-6">
      <div className="max-w-6xl mx-auto flex items-center justify-between gap-3">
        {/* Logo and Branding */}
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-amber-600 via-amber-500 to-yellow-400 flex items-center justify-center shadow-lg shadow-amber-500/20 text-slate-950 font-black">
            <Compass className="w-6 h-6 animate-spin-slow text-slate-950" />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <h1 className="text-lg sm:text-xl font-bold tracking-tight bg-gradient-to-r from-amber-200 via-amber-400 to-yellow-200 bg-clip-text text-transparent">
                Coimbatore & TN Travel Bot
              </h1>
              <span className="hidden sm:inline-flex items-center gap-1 text-[11px] font-semibold uppercase tracking-wider px-2 py-0.5 rounded-full bg-amber-500/10 text-amber-300 border border-amber-500/20">
                <Sparkles className="w-3 h-3 text-amber-400" />
                {engineMode || 'TN Tourism Expert'}
              </span>
            </div>
            <p className="text-xs text-slate-400 hidden xs:block">
              Coimbatore & Tamil Nadu Travel Guide (ChatGPT-like AI)
            </p>
          </div>
        </div>

        {/* Action Controls */}
        <div className="flex items-center gap-2 sm:gap-3">
          {/* Explore Hubs Drawer Button */}
          <button
            onClick={onOpenDestinations}
            className="flex items-center gap-1.5 px-3 py-1.5 text-xs font-medium rounded-lg bg-slate-800/80 hover:bg-slate-700/80 text-slate-200 border border-slate-700/60 transition shadow-sm"
            title="Browse Tamil Nadu Destinations"
          >
            <MapPin className="w-3.5 h-3.5 text-amber-400" />
            <span className="hidden sm:inline">Explore Hubs</span>
          </button>

          {/* Language Selector */}
          <div className="flex items-center bg-slate-800/80 rounded-lg p-0.5 border border-slate-700/60">
            <Globe className="w-3.5 h-3.5 text-slate-400 ml-2 hidden sm:block" />
            <select
              value={language}
              onChange={(e) => onLanguageChange(e.target.value as Language)}
              className="bg-transparent text-xs font-medium text-slate-200 py-1 px-2 focus:outline-none cursor-pointer"
            >
              <option value="auto" className="bg-slate-900 text-slate-200">Auto (தானியங்கி)</option>
              <option value="english" className="bg-slate-900 text-slate-200">English</option>
              <option value="tamil" className="bg-slate-900 text-slate-200">தமிழ் (Tamil)</option>
              <option value="tanglish" className="bg-slate-900 text-slate-200">Tanglish (தமிழ்)</option>
            </select>
          </div>

          {/* Settings Modal Button */}
          <button
            onClick={onOpenSettings}
            className="p-2 text-slate-300 hover:text-amber-400 rounded-lg hover:bg-slate-800/60 transition"
            title="Settings & API Key"
          >
            <Settings className="w-4 h-4" />
          </button>

          {/* New Chat Button */}
          <button
            onClick={onNewChat}
            className="flex items-center gap-1.5 px-3 py-1.5 text-xs font-semibold rounded-lg bg-gradient-to-r from-amber-600 to-amber-500 hover:from-amber-500 hover:to-amber-400 text-slate-950 transition shadow-md shadow-amber-500/10"
            title="Start a fresh conversation"
          >
            <RotateCcw className="w-3.5 h-3.5" />
            <span className="hidden xs:inline">New Chat</span>
          </button>
        </div>
      </div>
    </header>
  )
}
