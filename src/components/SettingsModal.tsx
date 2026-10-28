import React, { useState } from 'react'
import { X, Key, ShieldCheck, Cpu, Check, AlertCircle } from 'lucide-react'

interface SettingsModalProps {
  isOpen: boolean
  onClose: () => void
  engineMode: string
  onEngineUpdate?: () => void
}

export const SettingsModal: React.FC<SettingsModalProps> = ({
  isOpen,
  onClose,
  engineMode,
  onEngineUpdate
}) => {
  const [apiKey, setApiKey] = useState('')
  const [status, setStatus] = useState<'idle' | 'saving' | 'saved' | 'error'>('idle')
  const [statusMsg, setStatusMsg] = useState('')

  if (!isOpen) return null

  const handleSaveKey = async () => {
    setStatus('saving')
    try {
      const res = await fetch('/api/settings/key', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ api_key: apiKey })
      })
      const data = await res.json()
      if (res.ok) {
        setStatus('saved')
        setStatusMsg(data.message || 'Key updated successfully.')
        if (onEngineUpdate) onEngineUpdate()
        setTimeout(() => {
          setStatus('idle')
        }, 2000)
      } else {
        setStatus('error')
        setStatusMsg(data.detail || 'Failed to update key.')
      }
    } catch (err) {
      setStatus('error')
      setStatusMsg('Could not reach backend.')
    }
  }

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm">
      <div className="w-full max-w-md rounded-2xl bg-slate-900 border border-slate-800 p-6 shadow-2xl relative">
        <button
          onClick={onClose}
          className="absolute top-4 right-4 p-1.5 text-slate-400 hover:text-white rounded-lg hover:bg-slate-800 transition"
        >
          <X className="w-5 h-5" />
        </button>

        <div className="flex items-center gap-3 mb-4">
          <div className="p-2.5 rounded-xl bg-amber-500/20 text-amber-400">
            <Cpu className="w-6 h-6" />
          </div>
          <div>
            <h3 className="text-lg font-bold text-white">Assistant Engine Settings</h3>
            <p className="text-xs text-slate-400">Configure AI Model & Knowledge Integration</p>
          </div>
        </div>

        {/* Current Engine Badge */}
        <div className="p-3.5 rounded-xl bg-slate-800/80 border border-slate-700/60 mb-5">
          <div className="flex items-center justify-between text-xs">
            <span className="text-slate-400">Active Engine:</span>
            <span className="font-semibold text-amber-400 flex items-center gap-1.5">
              <ShieldCheck className="w-4 h-4 text-emerald-400" />
              {engineMode}
            </span>
          </div>
          <p className="text-[11px] text-slate-400 mt-2 leading-relaxed">
            The assistant has a built-in expert Tamil Nadu tourism engine with 32+ verified destinations, live Open-Meteo weather, and deterministic trip budget calculation.
          </p>
        </div>

        {/* Optional Gemini API Key */}
        <div className="space-y-3">
          <label className="block text-xs font-semibold text-slate-200">
            Google Gemini API Key (Optional)
          </label>
          <div className="relative">
            <Key className="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-slate-400" />
            <input
              type="password"
              value={apiKey}
              onChange={(e) => setApiKey(e.target.value)}
              placeholder="Enter AIzaSy... (Leave empty to use built-in engine)"
              className="w-full pl-9 pr-3 py-2 text-xs rounded-lg glass-input text-slate-200 placeholder-slate-500 focus:outline-none"
            />
          </div>
          <p className="text-[11px] text-slate-400">
            Keys are kept in your private local session only and never sent to external third parties.
          </p>

          {status === 'saved' && (
            <div className="p-2 rounded-lg bg-emerald-500/10 border border-emerald-500/30 text-emerald-300 text-xs flex items-center gap-2">
              <Check className="w-4 h-4 text-emerald-400" />
              <span>{statusMsg}</span>
            </div>
          )}

          {status === 'error' && (
            <div className="p-2 rounded-lg bg-rose-500/10 border border-rose-500/30 text-rose-300 text-xs flex items-center gap-2">
              <AlertCircle className="w-4 h-4 text-rose-400" />
              <span>{statusMsg}</span>
            </div>
          )}

          <div className="flex justify-end gap-2 pt-2">
            <button
              onClick={onClose}
              className="px-4 py-2 text-xs font-semibold text-slate-300 hover:text-white rounded-lg hover:bg-slate-800 transition"
            >
              Close
            </button>
            <button
              onClick={handleSaveKey}
              disabled={status === 'saving'}
              className="px-4 py-2 text-xs font-semibold rounded-lg bg-amber-500 hover:bg-amber-400 text-slate-950 transition shadow-sm"
            >
              {status === 'saving' ? 'Updating...' : 'Save & Update'}
            </button>
          </div>
        </div>
      </div>
    </div>
  )
}
