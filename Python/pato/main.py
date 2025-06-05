import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import threading
import time
import pyautogui
import random
import pygame  # 🎵 Para tocar o som

class PatoAnimado:
    def __init__(self):
        pygame.mixer.init()
        self.quack = pygame.mixer.Sound("quack.mp3")  # Carrega o som

        self.root = tk.Tk()
        self.root.overrideredirect(True)
        self.root.wm_attributes("-topmost", True)
        self.root.wm_attributes("-transparentcolor", "white")

        gif = Image.open("pato.gif")
        self.frames = []
        for frame in ImageSequence.Iterator(gif):
            frame = frame.convert("RGBA").resize((100, 100))
            self.frames.append(ImageTk.PhotoImage(frame))
        self.atual = 0
        self.pato_tk = self.frames[self.atual]

        self.canvas = tk.Canvas(self.root, width=150, height=250, bg='white', highlightthickness=0)
        self.canvas.pack()
        self.image_on_canvas = self.canvas.create_image(0, 130, anchor=tk.NW, image=self.pato_tk)

        self.canvas.bind('<Button-1>', self.on_click)
        self.canvas.bind('<Motion>', self.on_hover)

        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        self.x = random.randint(0, self.screen_width - 100)
        self.y = random.randint(0, self.screen_height - 250)
        self.dx = random.choice([-5, 5])
        self.dy = random.choice([-5, 5])

        threading.Thread(target=self.loop_mover, daemon=True).start()
        threading.Thread(target=self.animar_sprite, daemon=True).start()

        self.root.mainloop()

    def animar_sprite(self):
        while True:
            self.atual = (self.atual + 1) % len(self.frames)
            self.pato_tk = self.frames[self.atual]
            self.canvas.itemconfig(self.image_on_canvas, image=self.pato_tk)
            time.sleep(0.1)

    def loop_mover(self):
        while True:
            mouse_x, mouse_y = pyautogui.position()
            pato_real_x = self.x
            pato_real_y = self.y + 130
            distancia = ((mouse_x - pato_real_x)**2 + (mouse_y - pato_real_y)**2)**0.5

            if distancia < 100:
                self.dx = random.choice([-10, 10])
                self.dy = random.choice([-10, 10])
            else:
                if random.random() < 0.05:
                    self.dx = random.choice([-5, 5])
                    self.dy = random.choice([-5, 5])

            self.x += self.dx
            self.y += self.dy

            self.x = max(0, min(self.x, self.screen_width - 100))
            self.y = max(0, min(self.y, self.screen_height - 250))

            self.root.geometry(f"+{self.x}+{self.y}")
            time.sleep(0.05)

    def dentro_do_pato(self, event):
        return 0 <= event.x <= 100 and 130 <= event.y <= 230

    def on_click(self, event):
        if self.dentro_do_pato(event):
            self.quack.play()

    def on_hover(self, event):
        if self.dentro_do_pato(event):
            self.quack.play()

if __name__ == "__main__":
    PatoAnimado()
