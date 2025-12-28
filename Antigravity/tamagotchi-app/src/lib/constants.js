export const CONSTANTS = {
    TICK_RATE: 10000, // 10 seconds per tick
    MAX_STAT: 100,
    MIN_STAT: 0,
    DECAY: {
        // Base decay per tick (10s)
        // 0.05 per tick ~= 0.3 per min ~= 18 per hour (lasts ~5.5 hours)
        // Adjusted to 0.03 ~= 10 per hour (lasts ~10 hours)
        HUNGER: 0.03,
        HAPPINESS: 0.03,
        ENERGY: 0.02, // Energy lasts longer
        HYGIENE: 0.02,
    },
    MULTIPLIERS: {
        NIGHT_ENERGY: 2.5, // Tires faster at night
        MEAL_HUNGER: 2.0,  // Hungrier at meal times
        SLEEP_RECOVERY: 1.0, // Per tick
    },
    RECOVERY: {
        FEED: 20,
        PLAY: 15,
        CLEAN: 100,
    },
    THRESHOLDS: {
        SICK: 30,
        TIRED: 20,
        HUNGRY: 20,
        SAD: 20,
    },
    TIME: {
        NIGHT_START: 22, // 10 PM
        NIGHT_END: 7,    // 7 AM
        MEALS: [
            { start: 7, end: 9 },   // Breakfast
            { start: 12, end: 14 }, // Lunch
            { start: 19, end: 21 }, // Dinner
        ]
    },
    FOODS: ['DRUMSTICK', 'PIZZA', 'BURGER', 'DRINK', 'COOKIE'],
    DEATH_TIMEOUTS: {
        SICK: 24 * 60 * 60 * 1000,      // 24 Hours to die from sickness
        CRITICAL: 12 * 60 * 60 * 1000   // 12 Hours to die from 0 stats
    }
};

export const STATES = {
    IDLE: 'IDLE',
    EATING: 'EATING',
    SLEEPING: 'SLEEPING',
    PLAYING: 'PLAYING',
    SICK: 'SICK',
    DEAD: 'DEAD',
};
