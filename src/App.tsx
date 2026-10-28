import { useState, useEffect, useRef } from 'react'
import { Header } from './components/Header'
import { WelcomeHero } from './components/WelcomeHero'
import { ChatMessage } from './components/ChatMessage'
import { ChatInput } from './components/ChatInput'
import { DestinationDrawer } from './components/DestinationDrawer'
import { SettingsModal } from './components/SettingsModal'
import type { Message, Language } from './types'
import { Loader2, AlertCircle, RefreshCw } from 'lucide-react'

export function App() {
  const [messages, setMessages] = useState<Message[]>([])
  const [sessionId, setSessionId] = useState<string>(() => {
    return 'session_' + Math.random().toString(36).substring(2, 11)
  })
  const [language, setLanguage] = useState<Language>('auto')
  const [isLoading, setIsLoading] = useState<boolean>(false)
  const [networkError, setNetworkError] = useState<string | null>(null)
  const [lastQuery, setLastQuery] = useState<string>('')
  const [engineMode, setEngineMode] = useState<string>('TN Tourism Expert')
  const [isDrawerOpen, setIsDrawerOpen] = useState<boolean>(false)
  const [isSettingsOpen, setIsSettingsOpen] = useState<boolean>(false)

  const messagesEndRef = useRef<HTMLDivElement>(null)

  // Auto-scroll to bottom of messages
  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }

  useEffect(() => {
    scrollToBottom()
  }, [messages, isLoading])

  // Check backend health on mount
  const checkHealth = () => {
    fetch('/api/health')
      .then((res) => res.json())
      .then((data) => {
        if (data.engine_mode) {
          setEngineMode(data.gemini_api_configured ? 'Gemini 2.0 AI' : 'Verified TN Engine')
        }
      })
      .catch((err) => {
        console.warn('Backend not currently reachable', err)
      })
  }

  useEffect(() => {
    checkHealth()
  }, [])

  const handleSendMessage = async (userText: string) => {
    if (!userText.trim()) return

    setNetworkError(null)
    setLastQuery(userText)

    const now = new Date()
    const timeStr = now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })

    const userMsg: Message = {
      id: 'msg_' + Date.now(),
      role: 'user',
      content: userText,
      timestamp: timeStr
    }

    setMessages((prev) => [...prev, userMsg])
    setIsLoading(true)

    try {
      const response = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          session_id: sessionId,
          message: userText,
          language: language
        })
      })

      if (!response.ok) {
        throw new Error(`Server returned HTTP ${response.status}`)
      }

      const data = await response.json()

      const assistantMsg: Message = {
        id: 'msg_' + (Date.now() + 1),
        role: 'assistant',
        content: data.response,
        language: data.language,
        is_out_of_scope: data.is_out_of_scope,
        destination_card: data.destination_card,
        itinerary_card: data.itinerary_card,
        budget_card: data.budget_card,
        live_weather: data.live_weather,
        follow_up_suggestions: data.follow_up_suggestions,
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
      }

      setMessages((prev) => [...prev, assistantMsg])
    } catch (error: any) {
      console.error('Chat error:', error)
      setNetworkError(
        'Unable to connect to the TamilNadu TravelAI backend server. Please ensure the backend is running at http://127.0.0.1:8000.'
      )
    } finally {
      setIsLoading(false)
    }
  }

  const handleNewChat = async () => {
    const newId = 'session_' + Math.random().toString(36).substring(2, 11)
    setSessionId(newId)
    setMessages([])
    setNetworkError(null)

    // Notify backend
    try {
      await fetch('/api/session/reset', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ session_id: sessionId })
      })
    } catch (e) {
      // ignore
    }
  }

  return (
    <div className="flex flex-col min-h-screen bg-[#090d16] text-slate-100 selection:bg-amber-500/30 selection:text-amber-200">
      {/* App Header */}
      <Header
        language={language}
        onLanguageChange={setLanguage}
        onNewChat={handleNewChat}
        onOpenDestinations={() => setIsDrawerOpen(true)}
        onOpenSettings={() => setIsSettingsOpen(true)}
        engineMode={engineMode}
      />

      {/* Main Conversation Container */}
      <main className="flex-1 max-w-4xl w-full mx-auto px-4 py-6 flex flex-col justify-between">
        {messages.length === 0 ? (
          <WelcomeHero onSelectPrompt={handleSendMessage} />
        ) : (
          <div className="space-y-4 pb-6">
            {messages.map((msg) => (
              <ChatMessage
                key={msg.id}
                message={msg}
                onSelectFollowUp={handleSendMessage}
              />
            ))}

            {/* Loading Indicator */}
            {isLoading && (
              <div className="flex items-center gap-3 p-4 rounded-xl glass-card max-w-sm text-xs text-amber-300 animate-pulse">
                <div className="w-7 h-7 rounded-lg bg-amber-500/20 flex items-center justify-center text-amber-400">
                  <Loader2 className="w-4 h-4 animate-spin" />
                </div>
                <span>TamilNadu TravelAI is planning your journey...</span>
              </div>
            )}

            {/* Network Error Banner with Retry */}
            {networkError && (
              <div className="p-4 rounded-xl bg-rose-500/10 border border-rose-500/30 text-rose-300 text-xs flex items-start justify-between gap-3 shadow-lg">
                <div className="flex items-start gap-2.5">
                  <AlertCircle className="w-4 h-4 text-rose-400 shrink-0 mt-0.5" />
                  <div>
                    <p className="font-semibold text-rose-200">Connection Issue</p>
                    <p className="mt-0.5 text-slate-300">{networkError}</p>
                  </div>
                </div>
                {lastQuery && (
                  <button
                    onClick={() => handleSendMessage(lastQuery)}
                    className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-rose-500/20 hover:bg-rose-500/30 text-rose-200 text-xs font-semibold shrink-0 transition"
                  >
                    <RefreshCw className="w-3.5 h-3.5" />
                    <span>Retry</span>
                  </button>
                )}
              </div>
            )}

            <div ref={messagesEndRef} />
          </div>
        )}
      </main>

      {/* Message Input Bar */}
      <ChatInput onSendMessage={handleSendMessage} isLoading={isLoading} />

      {/* Destination Hubs Side Drawer */}
      <DestinationDrawer
        isOpen={isDrawerOpen}
        onClose={() => setIsDrawerOpen(false)}
        onSelectDestination={handleSendMessage}
      />

      {/* Engine & API Key Settings Modal */}
      <SettingsModal
        isOpen={isSettingsOpen}
        onClose={() => setIsSettingsOpen(false)}
        engineMode={engineMode}
        onEngineUpdate={checkHealth}
      />
    </div>
  )
}
export default App
