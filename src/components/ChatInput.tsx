import React, { useState, useRef, useEffect } from 'react'
import { Send, Sparkles, Loader2, DollarSign, Utensils } from 'lucide-react'

interface ChatInputProps {
  onSendMessage: (message: string) => void
  isLoading: boolean
}

export const ChatInput: React.FC<ChatInputProps> = ({ onSendMessage, isLoading }) => {
  const [input, setInput] = useState('')
  const textareaRef = useRef<HTMLTextAreaElement>(null)

  // Auto-resize textarea
  useEffect(() => {
    if (textareaRef.current) {
      textareaRef.current.style.height = 'auto'
      textareaRef.current.style.height = `${Math.min(textareaRef.current.scrollHeight, 140)}px`
    }
  }, [input])

  const handleSend = () => {
    if (input.trim() && !isLoading) {
      onSendMessage(input.trim())
      setInput('')
      if (textareaRef.current) {
        textareaRef.current.style.height = 'auto'
      }
    }
  }

  const handleKeyDown = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      handleSend()
    }
  }

  const quickModifiers = [
    { label: 'Make it cheaper', icon: DollarSign, query: 'Make this itinerary cheaper and suggest budget stays.' },
    { label: 'Add local food', icon: Utensils, query: 'Recommend the best local food spots and regional dishes for this trip.' },
    { label: 'Tanglish la sollunga', icon: Sparkles, query: 'Tanglish la explain pannunga.' },
    { label: 'Remove temples', query: 'Remove temple visits and replace with nature viewpoints or cultural sights.' },
  ]

  return (
    <div className="sticky bottom-0 z-20 glass-panel border-t border-slate-800/80 px-4 py-3 sm:px-6">
      <div className="max-w-4xl mx-auto space-y-2">
        {/* Quick action chips */}
        <div className="flex items-center gap-1.5 overflow-x-auto pb-1 scrollbar-none">
          {quickModifiers.map((chip, idx) => (
            <button
              key={idx}
              onClick={() => onSendMessage(chip.query)}
              disabled={isLoading}
              className="text-[11px] font-medium px-2.5 py-1 rounded-full bg-slate-800/80 hover:bg-slate-700/80 text-slate-300 hover:text-amber-300 border border-slate-700/60 transition whitespace-nowrap flex items-center gap-1 shadow-sm disabled:opacity-50"
            >
              {chip.icon && <chip.icon className="w-3 h-3 text-amber-400" />}
              <span>{chip.label}</span>
            </button>
          ))}
        </div>

        {/* Input Textarea Container */}
        <div className="relative flex items-end gap-2 rounded-2xl glass-input p-2 focus-within:ring-2 focus-within:ring-amber-500/30">
          <textarea
            ref={textareaRef}
            rows={1}
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={handleKeyDown}
            disabled={isLoading}
            placeholder="Ask anything about Tamil Nadu travel, food, routes, or trip plans... (Press Enter to send)"
            className="flex-1 max-h-36 resize-none bg-transparent px-2 py-1 text-sm text-slate-100 placeholder-slate-400 focus:outline-none"
          />

          <button
            onClick={handleSend}
            disabled={!input.trim() || isLoading}
            className={`p-2.5 rounded-xl transition flex items-center justify-center shrink-0 ${
              input.trim() && !isLoading
                ? 'bg-gradient-to-r from-amber-600 to-amber-500 text-slate-950 shadow-md shadow-amber-500/20 hover:from-amber-500 hover:to-amber-400'
                : 'bg-slate-800 text-slate-500 cursor-not-allowed'
            }`}
            title="Send message"
          >
            {isLoading ? (
              <Loader2 className="w-4 h-4 animate-spin text-amber-400" />
            ) : (
              <Send className="w-4 h-4" />
            )}
          </button>
        </div>

        <p className="text-[10px] text-center text-slate-500">
          TamilNadu TravelAI can make mistakes. Verify time-sensitive transport timings and seasonal ghat road alerts before travel.
        </p>
      </div>
    </div>
  )
}
