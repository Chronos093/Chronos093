import React, { useEffect, useState, useMemo } from 'react';
import { useTamagotchi } from './hooks/useTamagotchi';
import { STATES, CONSTANTS } from './lib/constants';
import { Utensils, Zap, Moon, Sparkles, RefreshCcw, Heart, Droplets, Pill, Drumstick, Pizza, Sandwich, Coffee, Cookie } from 'lucide-react';

// Use Emojis for full color support as requested
const FOOD_EMOJIS = ['🍗', '🍕', '🍔', '🥤', '🍪', '🍎', '🥪'];

function App() {
  const { stats, gameState, actions } = useTamagotchi();
  const [isNight, setIsNight] = useState(false);
  const [speech, setSpeech] = useState(null);
  const [currentFoodIndex, setCurrentFoodIndex] = useState(0);
  const [isEatingAnim, setIsEatingAnim] = useState(false);

  const CurrentFood = FOOD_EMOJIS[currentFoodIndex];

  // Randomize food after eating
  const handleEat = () => {
    actions.feed();
    setIsEatingAnim(true);
    setTimeout(() => {
      setIsEatingAnim(false);
      // Switch food type after eating
      setCurrentFoodIndex(prev => (prev + 1) % FOOD_EMOJIS.length);
    }, 1500); // Match CSS animation duration
  };

  // Check for night time
  useEffect(() => {
    const checkTime = () => {
      const h = new Date().getHours();
      setIsNight(h >= CONSTANTS.TIME.NIGHT_START || h < CONSTANTS.TIME.NIGHT_END);
    };
    checkTime();
    const interval = setInterval(checkTime, 60000);
    return () => clearInterval(interval);
  }, []);

  // Speech Bubble Logic
  useEffect(() => {
    if (gameState === STATES.DEAD) { setSpeech(null); return; }

    let msg = null;
    if (gameState === STATES.SICK) msg = "I'm sick... Help! 🤢";
    else if (stats.hunger < 20) msg = "I'm hungry! 🍔";
    else if (stats.energy < 20) msg = "So tired... 😴";
    else if (stats.happiness < 20) msg = "Bored... 😑";
    else if (stats.hygiene < 20) msg = "Eww... 💩";

    setSpeech(msg);
  }, [stats, gameState]);


  // Clouds Generator
  const clouds = useMemo(() => {
    return Array.from({ length: 5 }).map((_, i) => ({
      id: i,
      top: Math.random() * 40 + '%',
      left: Math.random() * 100 + '%',
      scale: 0.5 + Math.random(),
      duration: 20 + Math.random() * 20 + 's',
      delay: -Math.random() * 20 + 's'
    }));
  }, []);

  const getEmoji = () => {
    if (gameState === STATES.DEAD) return '💀';
    if (gameState === STATES.SICK) return '🤢';
    if (gameState === STATES.SLEEPING) return '💤';
    if (gameState === STATES.EATING) return '😋';
    if (gameState === STATES.PLAYING) return '😆';
    if (stats.happiness < 40) return '😢';
    return '👾';
  };

  const getBgColor = () => {
    if (gameState === STATES.DEAD) return 'bg-gray-900';
    if (isNight) return 'bg-indigo-950';
    if (stats.happiness < 30) return 'bg-blue-100';
    return 'bg-amber-50';
  };

  const StatBar = ({ icon: Icon, value, color }) => (
    <div className="flex items-center gap-2 w-full mb-1">
      <Icon size={20} className="text-black/80 drop-shadow-sm" />
      <div className="stat-bar-container flex-grow box-border border-2 border-black">
        <div
          className="stat-bar-fill border-r-2 border-black/20"
          style={{ width: `${value}%`, backgroundColor: color || '#4ade80' }}
        />
      </div>
    </div>
  );

  return (
    <div className="w-full h-screen bg-neutral-100 flex flex-col relative overflow-hidden select-none">

      {/* --- TOP BAR (Stats) --- */}
      {/* Moved outside and before the game stage so it sits on top naturally, solid background */}
      <div className="w-full p-4 bg-white border-b-4 border-black/10 z-20 flex flex-col gap-2 shadow-sm shrink-0">
        <StatBar icon={Utensils} value={stats.hunger} color={stats.hunger < 20 ? '#ef4444' : '#facc15'} />
        <StatBar icon={Heart} value={stats.happiness} color={stats.happiness < 20 ? '#ef4444' : '#60a5fa'} />
        <StatBar icon={Zap} value={stats.energy} color={stats.energy < 20 ? '#ef4444' : '#a855f7'} />
        <StatBar icon={Droplets} value={stats.hygiene} color={stats.hygiene < 20 ? '#ef4444' : '#22d3ee'} />
      </div>

      {/* --- MAIN STAGE (Pet & Background) --- */}
      {/* Background color is applied HERE now, so it doesn't go behind the header */}
      <div className={`flex-grow relative flex flex-col items-center justify-center overflow-hidden transition-colors duration-1000 ${getBgColor()}`}>

        {/* --- CLOUDS LAYER (Inside Stage) --- */}
        {!isNight && gameState !== STATES.DEAD && (
          <div className="absolute inset-0 pointer-events-none overflow-hidden">
            {clouds.map(c => (
              <div
                key={c.id}
                className="absolute text-white/40 animate-cloud"
                style={{
                  top: c.top,
                  left: c.left, // Start pos, animation moves it
                  fontSize: `${c.scale * 4}rem`,
                  animationDuration: c.duration,
                  animationDelay: c.delay
                }}
              >☁️</div>
            ))}
          </div>
        )}

        {/* Night Decor */}
        {isNight && (
          <>
            <div className="absolute top-10 right-10 text-4xl opacity-80 animate-pulse text-yellow-100">🌙</div>
            <div className="absolute top-24 left-8 text-xl text-yellow-100 opacity-60 animate-pulse">✨</div>
            <div className="absolute bottom-40 right-12 text-sm text-yellow-100 opacity-40 animate-pulse">✨</div>
          </>
        )}

        {/* Speech Bubble */}
        {speech && !isEatingAnim && (
          <div className="speech-bubble animate-bounce z-20">
            {speech}
          </div>
        )}

        {/* RENDER EITHER EATING ANIMATION OR PET FACE */}
        {isEatingAnim ? (
          <div className="absolute z-30 flex items-center justify-center animate-eat">
            {/* Huge Food Emoji */}
            <div className="text-[180px] filter drop-shadow-2xl">{CurrentFood}</div>
          </div>
        ) : (
          <div className={`
                  text-[150px] sm:text-[200px] leading-none 
                  filter drop-shadow-2xl 
                  transition-all duration-500
                  cursor-pointer
                  ${gameState === STATES.IDLE ? 'animate-breathe' : ''}
                  ${gameState === STATES.PLAYING ? 'animate-bounce' : ''}
                  ${gameState === STATES.SICK ? 'animate-shake grayscale' : ''}
            `}
            onClick={() => { if (gameState === STATES.IDLE) actions.play(); }}
          >
            {getEmoji()}
          </div>
        )}
      </div>

      {/* --- BOTTOM CONTROLS --- */}
      <div className="w-full p-4 pb-8 bg-white/30 backdrop-blur-md border-t-4 border-black/10 z-10 shadow-[0_-4px_10px_rgba(0,0,0,0.05)] shrink-0">
        <div className="grid grid-cols-4 gap-3 max-w-md mx-auto relative">

          {gameState === STATES.SICK ? (
            <div className="col-span-4 flex justify-center animate-bounce">
              <button onClick={actions.giveMedicine} className="pixel-btn bg-pink-500 text-white w-full max-w-[200px] border-pink-700 shadow-lg">
                <Pill size={32} className="animate-pulse" />
                <span className="text-sm mt-2">GIVE MEDICINE</span>
              </button>
            </div>
          ) : (
            <>
              <button onClick={handleEat} disabled={gameState === STATES.SLEEPING || gameState === STATES.DEAD} className="pixel-btn active:bg-yellow-100 group">
                <div className="group-active:animate-bounce-icon group-hover:scale-110 transition-transform text-2xl">
                  {CurrentFood}
                </div>
                <span className="mt-1">EAT</span>
              </button>
              <button onClick={actions.play} disabled={gameState === STATES.SLEEPING || gameState === STATES.DEAD} className="pixel-btn active:bg-blue-100 group">
                <div className="group-active:animate-spin-slow group-hover:rotate-12 transition-transform text-2xl">
                  ⚽
                </div>
                <span className="mt-1">PLAY</span>
              </button>
              <button onClick={actions.sleep} disabled={gameState === STATES.DEAD} className={`pixel-btn ${gameState === STATES.SLEEPING ? 'bg-indigo-300' : 'active:bg-indigo-100'} group`}>
                <div className="animate-pulse">
                  <Moon size={24} className="text-indigo-600" />
                </div>
                <span>{gameState === STATES.SLEEPING ? 'WAKE' : 'SLEEP'}</span>
              </button>
              <button onClick={actions.clean} disabled={gameState === STATES.SLEEPING || gameState === STATES.DEAD} className="pixel-btn active:bg-cyan-100 group">
                <div className="animate-drip">
                  <Sparkles size={24} className="text-cyan-600" />
                </div>
                <span>CLEAN</span>
              </button>
            </>
          )}

        </div>
      </div>

      {/* --- GAME OVER OVERLAY --- */}
      {gameState === STATES.DEAD && (
        <div className="absolute inset-0 bg-black/95 flex flex-col items-center justify-center z-50 animate-fade-in p-8 text-center">
          <div className="text-8xl mb-6 grayscale opacity-80">🪦</div>
          <h1 className="text-red-600 text-4xl mb-2 font-bold tracking-widest font-[Press_Start_2P]">R.I.P.</h1>
          <p className="text-gray-400 mb-8 text-sm max-w-[200px]">Your pixel friend has pixelated away.</p>

          <button onClick={actions.revive} className="pixel-btn bg-white border-4 border-gray-500 hover:bg-gray-200 scale-125">
            <RefreshCcw className="mr-2 inline animate-spin-slow" /> TRY AGAIN
          </button>
        </div>
      )}

    </div>
  );
}

export default App;
