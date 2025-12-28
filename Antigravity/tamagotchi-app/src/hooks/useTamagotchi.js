import { useState, useEffect, useCallback, useRef } from 'react';
import { CONSTANTS, STATES } from '../lib/constants';
import { LocalNotifications } from '@capacitor/local-notifications';

export const useTamagotchi = () => {
    // Initialize stats and last numeric update time
    const [stats, setStats] = useState(() => {
        try {
            const saved = localStorage.getItem('tamagotchi_stats');
            const parsed = saved ? JSON.parse(saved) : null;
            // Validate minimal structure
            if (parsed && typeof parsed.hunger === 'number') {
                return parsed;
            }
        } catch (e) {
            console.error("Failed to load save", e);
        }
        return {
            hunger: 100,
            happiness: 100,
            energy: 100,
            hygiene: 100,
            sicknessStart: null,
            criticalStart: null,
            lastSaveTime: Date.now()
        };
    });

    const [gameState, setGameState] = useState(STATES.IDLE);

    // Refs to prevent notification spam
    const hasNotifiedHunger = useRef(false);
    const hasNotifiedSleep = useRef(false);
    const hasNotifiedGrim = useRef(false);

    // Helpers
    const clamp = (val, min, max) => Math.min(Math.max(val, min), max);


    // Save to localStorage
    useEffect(() => {
        const dataToSave = { ...stats, lastSaveTime: Date.now() };
        localStorage.setItem('tamagotchi_stats', JSON.stringify(dataToSave));
    }, [stats]);

    // Request Notification Permissions on Mount
    useEffect(() => {
        const reqPerms = async () => {
            try {
                const result = await LocalNotifications.requestPermissions();
                if (result.display === 'granted') {
                    console.log("Notification permissions granted");
                }
            } catch (e) {
                console.error("Error requesting notifications", e);
            }
        };
        reqPerms();
    }, []);

    // --- LOGIC ENGINE ---

    // Calculate multipliers based on current time
    const getMultipliers = useCallback(() => {
        const hour = new Date().getHours();
        let hungerMult = 1;
        let energyMult = 1;

        // Meal Times
        const isMealTime = CONSTANTS.TIME.MEALS.some(m => hour >= m.start && hour < m.end);
        if (isMealTime) hungerMult = CONSTANTS.MULTIPLIERS.MEAL_HUNGER;

        // Night Time (Calc for wrapping hours e.g. 22 to 7)
        const isNight = hour >= CONSTANTS.TIME.NIGHT_START || hour < CONSTANTS.TIME.NIGHT_END;
        if (isNight) energyMult = CONSTANTS.MULTIPLIERS.NIGHT_ENERGY;

        return { hungerMult, energyMult };
    }, []);


    // Decrease Stats function (Single Tick)
    const applyTick = useCallback((currentStats, ticksPassed = 1, isSleeping = false) => {
        const { hungerMult, energyMult } = getMultipliers();

        // If many ticks (offline), we estimate average, but for simplicity we use current time multipliers
        // A more complex version would integrate over the time gap, but this is sufficient for casual play.

        let newStats = { ...currentStats };

        if (!isSleeping && currentStats.hunger > 0 && currentStats.hygiene > 0 && currentStats.energy > 0) {
            newStats.hunger -= CONSTANTS.DECAY.HUNGER * hungerMult * ticksPassed;
            newStats.happiness -= CONSTANTS.DECAY.HAPPINESS * ticksPassed;
            newStats.energy -= CONSTANTS.DECAY.ENERGY * energyMult * ticksPassed;
            newStats.hygiene -= CONSTANTS.DECAY.HYGIENE * ticksPassed;
        } else if (isSleeping) {
            // While sleeping
            newStats.energy += CONSTANTS.MULTIPLIERS.SLEEP_RECOVERY * ticksPassed;
            newStats.hunger -= (CONSTANTS.DECAY.HUNGER * 0.5) * ticksPassed; // Slower hunger in sleep
        }

        // Clamp everyone
        Object.keys(newStats).forEach(key => {
            if (typeof newStats[key] === 'number') {
                newStats[key] = clamp(newStats[key], CONSTANTS.MIN_STAT, CONSTANTS.MAX_STAT);
            }
        });

        return newStats;
    }, [getMultipliers]);


    // Offline Catch-up (Run once on mount)
    useEffect(() => {
        const now = Date.now();
        const lastSave = stats.lastSaveTime || now;
        const diffMs = now - lastSave;

        if (diffMs > 1000) { // If more than 1 second passed
            const ticksMissed = Math.floor(diffMs / CONSTANTS.TICK_RATE);
            if (ticksMissed > 0) {
                console.log(`Catching up: ${ticksMissed} ticks missed.`);
                setStats(prev => {
                    // Assume constant state for the offline period (e.g. if was sleeping, stayed sleeping)
                    // Limitation: Doesn't wake up automatically if energy full offline.
                    const wasSleeping = gameState === STATES.SLEEPING;
                    return applyTick(prev, ticksMissed, wasSleeping);
                });
            }
        }
    }, []); // Run ONCE on mount


    // Notifications helper
    const checkNotifications = async (newStats) => {
        // HUNGER CHECK
        if (newStats.hunger < 20 && !hasNotifiedHunger.current) {
            hasNotifiedHunger.current = true;
            await LocalNotifications.schedule({
                notifications: [{
                    title: "I'm Hungry!",
                    body: "Please feed me! 🍗",
                    id: 1,
                    schedule: { at: new Date(Date.now() + 500) }
                }]
            }).catch(e => console.error(e));
        } else if (newStats.hunger >= 30) {
            hasNotifiedHunger.current = false;
        }

        // ENERGY CHECK
        if (newStats.energy < 20 && !hasNotifiedSleep.current) {
            hasNotifiedSleep.current = true;
            await LocalNotifications.schedule({
                notifications: [{
                    title: "So tired...",
                    body: "I need to sleep! 💤",
                    id: 2,
                    schedule: { at: new Date(Date.now() + 500) }
                }]
            }).catch(e => console.error(e));
        } else if (newStats.energy >= 30) {
            hasNotifiedSleep.current = false;
        }
    };

    // Live Game Loop
    useEffect(() => {
        const interval = setInterval(() => {
            if (gameState === STATES.DEAD) return;

            setStats(prev => {
                const now = Date.now();
                let { sicknessStart, criticalStart } = prev;
                let shouldDie = false;

                // 1. Sickness Logic
                let isSick = gameState === STATES.SICK;

                // If not sick, check chance to become sick
                if (!isSick && (prev.hunger < 20 || prev.hygiene < 20 || prev.energy < 20)) {
                    if (Math.random() < 0.1) {
                        setGameState(STATES.SICK);
                        isSick = true;
                    }
                }

                // Track Sickness Time
                if (isSick) {
                    if (!sicknessStart) sicknessStart = now;
                    else if (now - sicknessStart > CONSTANTS.DEATH_TIMEOUTS.SICK) shouldDie = true;
                } else {
                    sicknessStart = null;
                }

                // 2. Critical Stats Logic (Any stat <= 0)
                const isCritical = prev.hunger <= 0 || prev.hygiene <= 0 || prev.energy <= 0;

                if (isCritical) {
                    if (!criticalStart) criticalStart = now;
                    else if (now - criticalStart > CONSTANTS.DEATH_TIMEOUTS.CRITICAL) shouldDie = true;
                } else {
                    criticalStart = null;
                }

                // 3. Death Trigger
                if (shouldDie) {
                    setGameState(STATES.DEAD);
                    if (!hasNotifiedGrim.current) {
                        hasNotifiedGrim.current = true;
                        LocalNotifications.schedule({
                            notifications: [{
                                title: "R.I.P.",
                                body: "Your pet has passed away... 🪦",
                                id: 99,
                                schedule: { at: new Date(Date.now() + 500) }
                            }]
                        }).catch(console.error);
                    }
                    return prev; // Stop updates if dead
                }

                // 4. Apply Ticks
                const isSleeping = gameState === STATES.SLEEPING;
                const newStats = applyTick(prev, 1, isSleeping);
                checkNotifications(newStats);

                return {
                    ...newStats,
                    sicknessStart,
                    criticalStart
                };
            });

        }, CONSTANTS.TICK_RATE);

        return () => clearInterval(interval);
    }, [gameState, applyTick]); // Removed 'stats' from dependency to avoid loop, using functional update


    // Actions
    const feed = () => {
        if (gameState === STATES.DEAD || gameState === STATES.SLEEPING || gameState === STATES.SICK) return; // Can't eat if sick
        setGameState(STATES.EATING);
        setStats(prev => ({ ...prev, hunger: clamp(prev.hunger + CONSTANTS.RECOVERY.FEED, 0, 100) }));
        setTimeout(() => setGameState(STATES.IDLE), 2000);
    };

    const play = () => {
        if (gameState === STATES.DEAD || gameState === STATES.SLEEPING || gameState === STATES.SICK) return;
        setGameState(STATES.PLAYING);
        setStats(prev => ({
            ...prev,
            happiness: clamp(prev.happiness + CONSTANTS.RECOVERY.PLAY, 0, 100),
            energy: clamp(prev.energy - 10, 0, 100)
        }));
        setTimeout(() => setGameState(STATES.IDLE), 2000);
    };

    const sleep = () => {
        if (gameState === STATES.DEAD || gameState === STATES.SICK) return;
        setGameState(prev => prev === STATES.SLEEPING ? STATES.IDLE : STATES.SLEEPING);
    };

    const clean = () => {
        if (gameState === STATES.DEAD || gameState === STATES.SLEEPING) return;
        setStats(prev => ({ ...prev, hygiene: 100 }));
    };

    const giveMedicine = () => {
        if (gameState !== STATES.SICK) return;
        setGameState(STATES.IDLE);
        setStats(prev => ({ ...prev, health: 100, happiness: prev.happiness - 10 })); // Medicine tastes bad
    };

    const revive = () => {
        setStats({
            hunger: 100, happiness: 100, energy: 100, hygiene: 100,
            sicknessStart: null, criticalStart: null,
            lastSaveTime: Date.now()
        });
        setGameState(STATES.IDLE);
    }

    return {
        stats,
        gameState,
        actions: { feed, play, sleep, clean, giveMedicine, revive }
    };
};
