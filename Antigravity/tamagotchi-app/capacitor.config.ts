import { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
    appId: 'com.pixels.tamagotchi',
    appName: 'Pixel Tamagotchi',
    webDir: 'dist',
    server: {
        androidScheme: 'https'
    }
};

export default config;
