import pyautogui
import time

# Obtem as dimensões da tela
largura, altura = pyautogui.size()

# Calcula o centro
centro_x = largura // 2
centro_y = altura // 2

try:
    print("Iniciando cliques no centro da tela. Pressione Ctrl+C para parar.")
    while True:
        pyautogui.click(x=centro_x, y=centro_y)
        time.sleep(1)
except KeyboardInterrupt:
    print("\nScript interrompido pelo usuário.")
