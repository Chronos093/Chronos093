from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from random import randint, sample

TAMANHO = 6
MAX_TROCAS = 3

class Tabuleiro(GridLayout):
    def __init__(self, jogo, **kwargs):
        super().__init__(**kwargs)
        self.jogo = jogo
        self.cols = TAMANHO
        self.rows = TAMANHO
        self.botões = []
        self.atualizar_tabuleiro()

    def atualizar_tabuleiro(self):
        self.clear_widgets()
        self.botões.clear()
        for i in range(TAMANHO):
            for j in range(TAMANHO):
                valor = self.jogo.tabuleiro[i][j]
                texto = str(valor) if valor else ""
                btn = Button(text=texto)
                btn.bind(on_release=lambda btn, x=i, y=j: self.jogo.jogar(x, y))
                self.add_widget(btn)
                self.botões.append((btn, i, j))

    def atualizar_botoes(self):
        for btn, i, j in self.botões:
            valor = self.jogo.tabuleiro[i][j]
            btn.text = str(valor) if valor else ""
            btn.background_color = [1, 1, 1, 1]  # Branco normal

    def piscar_botao(self, x, y, cor):
        for btn, i, j in self.botões:
            if i == x and j == y:
                original = btn.background_color[:]
                btn.background_color = cor
                Clock.schedule_once(lambda dt: self.reset_cor(btn, original), 0.2)
                break

    def reset_cor(self, btn, cor):
        btn.background_color = cor


class Jogo:
    def __init__(self, root):
        self.root = root
        self.tabuleiro = [[None for _ in range(TAMANHO)] for _ in range(TAMANHO)]
        self.numero_atual = randint(1, 6)
        self.numero_preso = None
        self.trocas = MAX_TROCAS
        self.tabuleiro_ui = Tabuleiro(self)
        self.label_info = Label(text="", size_hint=(1, 0.1), font_size='18sp')
        self.atualizar_info()

        posicoes = sample(range(TAMANHO * TAMANHO), 15)
        for pos in posicoes:
            x, y = divmod(pos, TAMANHO)
            self.tabuleiro[x][y] = randint(1, 6)

    def atualizar_info(self):
        info = f"[Número atual: {self.numero_atual}]  [Trocas: {self.trocas}]"
        if self.numero_preso:
            info += f"  [Preso: {self.numero_preso}]"
        self.label_info.text = info

    def jogar(self, x, y):
        if self.tabuleiro[x][y] is not None:
            return

        self.tabuleiro[x][y] = self.numero_atual
        if self.remover_par(x, y, self.numero_atual):
            self.tabuleiro_ui.piscar_botao(x, y, [0.5, 1, 0.5, 1])  # verde claro
        else:
            self.tabuleiro_ui.piscar_botao(x, y, [0.8, 0.8, 0.8, 1])  # cinza claro

        if self.numero_preso:
            self.numero_atual = self.numero_preso
            self.numero_preso = None
            self.tabuleiro_ui.piscar_botao(x, y, [0.6, 0.8, 1, 1])  # azul claro
        else:
            self.numero_atual = randint(1, 6)

        if all(cell is None for row in self.tabuleiro for cell in row):
            self.label_info.text = "🏆 Você venceu!"
            return

        if not any(cell is None for row in self.tabuleiro for cell in row):
            self.label_info.text = "❌ Você perdeu!"
            return

        self.atualizar_info()
        self.tabuleiro_ui.atualizar_botoes()

    def remover_par(self, x, y, numero):
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < TAMANHO and 0 <= ny < TAMANHO:
                if self.tabuleiro[nx][ny] == numero:
                    self.tabuleiro[nx][ny] = None
                    self.tabuleiro[x][y] = None
                    self.tabuleiro_ui.piscar_botao(nx, ny, [0.5, 1, 0.5, 1])
                    return True
        return False

    def trocar_numero(self, btn):
        if self.numero_preso:
            self.label_info.text = "⚠️ Jogue o número preso primeiro!"
            return

        if self.trocas == 0:
            self.label_info.text = "🚫 Fim das trocas. Reinicie o jogo."
            return

        self.trocas -= 1
        self.numero_preso = randint(1, 6)
        self.numero_atual = randint(1, 6)
        self.atualizar_info()


class JogoApp(App):
    def build(self):
        self.jogo = Jogo(self)

        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        layout.add_widget(self.jogo.label_info)
        layout.add_widget(self.jogo.tabuleiro_ui)

        controle = BoxLayout(size_hint=(1, 0.15), spacing=10)
        botao_trocar = Button(text="🔁 Trocar número", on_release=self.jogo.trocar_numero)
        botao_reiniciar = Button(text="🔄 Novo jogo", on_release=lambda x: self.reiniciar_jogo())
        controle.add_widget(botao_trocar)
        controle.add_widget(botao_reiniciar)

        layout.add_widget(controle)
        return layout

    def reiniciar_jogo(self):
        self.stop()
        self.run()

if __name__ == "__main__":
    JogoApp().run()
