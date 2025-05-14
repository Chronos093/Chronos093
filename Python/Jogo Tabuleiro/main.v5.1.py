import tkinter as tk
import random
from tkinter import messagebox

class PairMatchingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo de Pares 6x6")
        self.board = [[0]*6 for _ in range(6)]
        self.buttons = [[None]*6 for _ in range(6)]
        self.current_number = 0
        self.held_number = None
        self.swap_count = 3
        self.max_moves = 50
        self.moves_made = 0
        self.started = False

        self.info_label = tk.Label(root, text="Clique para começar o jogo", font=("Arial", 14))
        self.info_label.grid(row=0, column=0, columnspan=6, pady=5)

        # Container para o tabuleiro
        self.board_frame = tk.Frame(root)
        self.board_frame.grid(row=1, column=0, columnspan=6, pady=5)

        for i in range(6):
            for j in range(6):
                btn = tk.Button(self.board_frame, text="", width=3, height=1, 
                                font=("Arial", 12),
                                command=lambda i=i, j=j: self.place_number(i, j))
                btn.grid(row=i, column=j, padx=1, pady=1)
                self.buttons[i][j] = btn

        self.swap_button = tk.Button(root, text="Trocar Número (3)", command=self.swap_number)
        self.swap_button.grid(row=2, column=0, columnspan=3, sticky="we", pady=5)

        self.score_label = tk.Label(root, text="Pontuação: 0", font=("Arial", 12))
        self.score_label.grid(row=2, column=3, columnspan=3, sticky="we", pady=5)

    def start_game(self):
        self.started = True
        self.score = 0
        self.moves_made = 0
        self.swap_count = 3
        self.held_number = None
        self.board = [[0]*6 for _ in range(6)]

        # Preenche 15 posições com números aleatórios
        filled = 0
        while filled < 15:
            i, j = random.randint(0,5), random.randint(0,5)
            if self.board[i][j] == 0:
                self.board[i][j] = random.randint(1,6)
                filled += 1

        self.current_number = random.randint(1,6)
        self.update_board()

    def update_board(self):
        for i in range(6):
            for j in range(6):
                num = self.board[i][j]
                self.buttons[i][j]['text'] = str(num) if num != 0 else ""
        held = f"Preso: {self.held_number}" if self.held_number else ""
        self.info_label['text'] = f"Número atual: {self.current_number}  {held}  Movimentos restantes: {self.max_moves - self.moves_made}"
        self.swap_button['text'] = f"Trocar Número ({self.swap_count})"
        self.score_label['text'] = f"Pontuação: {self.score}"

    def has_adjacent_pair(self, i, j):
        val = self.board[i][j]
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni, nj = i+dx, j+dy
            if 0 <= ni < 6 and 0 <= nj < 6 and self.board[ni][nj] == val:
                return True
        return False

    def remove_adjacent_pairs(self, i, j):
        val = self.board[i][j]
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            ni, nj = i+dx, j+dy
            if 0 <= ni < 6 and 0 <= nj < 6 and self.board[ni][nj] == val:
                self.board[ni][nj] = 0
                self.board[i][j] = 0
                self.score += 10
                return

    def place_number(self, i, j):
        if self.board[i][j] != 0:
            return

        if not self.started:
            self.start_game()
            return

        if self.moves_made >= self.max_moves:
            messagebox.showinfo("Fim de Jogo", "Você excedeu o número máximo de jogadas!")
            self.root.quit()
            return

        self.moves_made += 1
        placed = False

        # Coloca o número atual
        self.board[i][j] = self.current_number
        if self.has_adjacent_pair(i, j):
            self.remove_adjacent_pairs(i, j)
            # Se tiver número preso, ele entra no lugar
            if self.held_number:
                self.board[i][j] = self.held_number
                self.held_number = None
        else:
            placed = True
            # Se tiver número preso, ele continua preso

        if placed or not self.held_number:
            self.current_number = random.randint(1,6)

        self.update_board()
        self.check_game_state()

    def swap_number(self):
        if not self.started:
            return
        if self.swap_count <= 0:
            messagebox.showinfo("Sem Trocas", "Você usou todas as trocas! Fim de jogo.")
            self.root.quit()
            return

        self.swap_count -= 1
        self.held_number = random.randint(1,6)
        self.current_number = random.randint(1,6)
        self.update_board()

    def check_game_state(self):
        for row in self.board:
            if 0 in row:
                return
        messagebox.showinfo("Fim de Jogo", "Você venceu! Tabuleiro limpo!")
        self.root.quit()

if __name__ == '__main__':
    root = tk.Tk()
    game = PairMatchingGame(root)
    root.mainloop()
