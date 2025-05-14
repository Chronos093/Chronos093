import tkinter as tk
from tkinter import messagebox
import random

TAMANHO = 6
MAX_TROCAS = 3

class JogoTabuleiro:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo de Pares - 6x6")
        self.tabuleiro = []
        self.botoes = []
        self.numero_atual = None
        self.numero_preso = None
        self.trocas = MAX_TROCAS

        self.frame_tabuleiro = tk.Frame(root)
        self.frame_tabuleiro.pack(pady=10)

        self.label_info = tk.Label(root, text="", font=("Helvetica", 14))
        self.label_info.pack()

        self.frame_controle = tk.Frame(root)
        self.frame_controle.pack(pady=10)

        self.botao_trocar = tk.Button(self.frame_controle, text="🔁 Trocar número", command=self.trocar_numero)
        self.botao_trocar.grid(row=0, column=0, padx=5)

        self.botao_novo = tk.Button(self.frame_controle, text="🔄 Novo jogo", command=self.novo_jogo)
        self.botao_novo.grid(row=0, column=1, padx=5)

        self.novo_jogo()

    def novo_jogo(self):
        self.tabuleiro = [[None for _ in range(TAMANHO)] for _ in range(TAMANHO)]
        self.botoes = []
        self.numero_preso = None
        self.trocas = MAX_TROCAS
        self.numero_atual = random.randint(1, 6)

        posicoes = random.sample(range(TAMANHO * TAMANHO), 15)
        for pos in posicoes:
            x, y = divmod(pos, TAMANHO)
            self.tabuleiro[x][y] = random.randint(1, 6)

        for widget in self.frame_tabuleiro.winfo_children():
            widget.destroy()

        for i in range(TAMANHO):
            linha = []
            for j in range(TAMANHO):
                btn = tk.Button(self.frame_tabuleiro, text=" ", width=4, height=2,
                                command=lambda x=i, y=j: self.jogar(x, y))
                btn.grid(row=i, column=j, padx=1, pady=1)
                linha.append(btn)
            self.botoes.append(linha)

        self.atualizar_interface()

    def atualizar_interface(self):
        for i in range(TAMANHO):
            for j in range(TAMANHO):
                val = self.tabuleiro[i][j]
                self.botoes[i][j]["text"] = str(val) if val else " "
                self.botoes[i][j]["bg"] = "SystemButtonFace"

        info = f"🎲 Número atual: {self.numero_atual}    🔁 Trocas: {self.trocas}"
        if self.numero_preso:
            info += f"    🔒 Número preso: {self.numero_preso}"
        self.label_info["text"] = info

    def piscar_botao(self, x, y, cor):
        botao = self.botoes[x][y]
        original = botao["bg"]
        botao["bg"] = cor
        self.root.after(200, lambda: botao.config(bg=original))

    def jogar(self, x, y):
        if self.tabuleiro[x][y] is not None:
            return

        self.tabuleiro[x][y] = self.numero_atual
        if self.remover_par(x, y, self.numero_atual):
            self.piscar_botao(x, y, "lightgreen")
        else:
            self.piscar_botao(x, y, "lightgray")

        self.numero_atual = None
        if self.numero_preso:
            self.numero_atual = self.numero_preso
            self.numero_preso = None
            self.piscar_botao(x, y, "lightblue")
        else:
            self.numero_atual = random.randint(1, 6)

        if all(cell is None for row in self.tabuleiro for cell in row):
            messagebox.showinfo("Parabéns!", "🏆 Você venceu!")
            self.novo_jogo()
            return

        if not any(cell is None for row in self.tabuleiro for cell in row):
            messagebox.showerror("Fim de jogo", "❌ Você perdeu! Sem espaços livres.")
            self.novo_jogo()
            return

        self.atualizar_interface()

    def remover_par(self, x, y, numero):
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < TAMANHO and 0 <= ny < TAMANHO:
                if self.tabuleiro[nx][ny] == numero:
                    self.tabuleiro[nx][ny] = None
                    self.tabuleiro[x][y] = None
                    self.piscar_botao(nx, ny, "lightgreen")
                    return True
        return False

    def trocar_numero(self):
        if self.numero_preso:
            messagebox.showwarning("Troca não permitida", "⚠️ Você já tem um número preso. Jogue ele antes.")
            return

        if self.trocas == 0:
            resp = messagebox.askyesno("Fim de trocas", "🚫 Você usou todas as trocas.\nDeseja iniciar um novo jogo?")
            if resp:
                self.novo_jogo()
            else:
                self.root.quit()
            return

        self.trocas -= 1
        self.numero_preso = random.randint(1, 6)
        self.numero_atual = random.randint(1, 6)
        self.atualizar_interface()

# Executa o jogo
root = tk.Tk()
app = JogoTabuleiro(root)
root.mainloop()
