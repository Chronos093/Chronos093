import random

TAMANHO = 6
MAX_TROCAS = 3

def criar_tabuleiro():
    tabuleiro = [[None for _ in range(TAMANHO)] for _ in range(TAMANHO)]
    posicoes = random.sample(range(TAMANHO * TAMANHO), 15)
    for pos in posicoes:
        x, y = divmod(pos, TAMANHO)
        tabuleiro[x][y] = random.randint(1, 6)
    return tabuleiro

def imprimir_tabuleiro(tabuleiro):
    print("\nTabuleiro:")
    for linha in tabuleiro:
        print(' '.join(str(c) if c else '.' for c in linha))
    print()

def tem_par_adjacente(tabuleiro, x, y, numero):
    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx, ny = x+dx, y+dy
        if 0 <= nx < TAMANHO and 0 <= ny < TAMANHO:
            if tabuleiro[nx][ny] == numero:
                return True
    return False

def pode_jogar(tabuleiro):
    for x in range(TAMANHO):
        for y in range(TAMANHO):
            if tabuleiro[x][y] is None:
                return True
    return False

def remover_par(tabuleiro, x, y, numero):
    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx, ny = x+dx, y+dy
        if 0 <= nx < TAMANHO and 0 <= ny < TAMANHO:
            if tabuleiro[nx][ny] == numero:
                tabuleiro[nx][ny] = None
                tabuleiro[x][y] = None
                print("✅ Par removido!")
                return True
    return False

def jogar():
    tabuleiro = criar_tabuleiro()
    trocas_restantes = MAX_TROCAS
    numero_preso = None

    while True:
        imprimir_tabuleiro(tabuleiro)
        
        if not pode_jogar(tabuleiro):
            print("❌ Você perdeu! Sem espaços restantes.")
            break

        if all(all(cell is None for cell in row) for row in tabuleiro):
            print("🏆 Você venceu! Tabuleiro limpo.")
            break

        if numero_preso:
            print(f"🔒 Número preso com você: {numero_preso}")
        numero = random.randint(1, 6)
        print(f"🎲 Novo número sorteado: {numero}")
        print(f"🔁 Trocas restantes: {trocas_restantes}")

        acao = input("Digite 'j' para jogar, 't' para trocar o número: ").lower()

        if acao == 't':
            if trocas_restantes == 0:
                print("⚠️ Você não tem mais trocas disponíveis.")
                continue
            trocas_restantes -= 1
            if numero_preso:
                print(f"⚠️ Você já tem um número preso ({numero_preso}), jogue ele antes de pedir outra troca.")
                continue
            numero_preso = random.randint(1, 6)
            print(f"🔁 Número trocado! Novo número: {random.randint(1,6)}, número preso: {numero_preso}")
            continue  # Vai sortear outro número no próximo loop

        try:
            x = int(input("Linha (0-5): "))
            y = int(input("Coluna (0-5): "))
            if not (0 <= x < TAMANHO and 0 <= y < TAMANHO):
                print("⚠️ Coordenadas fora do tabuleiro.")
                continue
            if tabuleiro[x][y] is not None:
                print("⚠️ Espaço já ocupado.")
                continue

            tabuleiro[x][y] = numero
            if not remover_par(tabuleiro, x, y, numero):
                print("🔹 Sem par. Número fixado no tabuleiro.")

            # Depois da jogada com o número atual, se houver número preso, o jogador deve jogá-lo
            while numero_preso:
                imprimir_tabuleiro(tabuleiro)
                print(f"🔒 Você ainda tem o número preso: {numero_preso}")
                try:
                    x = int(input("Linha para o número preso (0-5): "))
                    y = int(input("Coluna para o número preso (0-5): "))
                    if not (0 <= x < TAMANHO and 0 <= y < TAMANHO):
                        print("⚠️ Coordenadas fora do tabuleiro.")
                        continue
                    if tabuleiro[x][y] is not None:
                        print("⚠️ Espaço já ocupado.")
                        continue

                    tabuleiro[x][y] = numero_preso
                    if not remover_par(tabuleiro, x, y, numero_preso):
                        print("🔹 Número preso fixado no tabuleiro.")
                    else:
                        print("✅ Número preso removido com par.")
                    numero_preso = None
                except ValueError:
                    print("⚠️ Entrada inválida.")
        except ValueError:
            print("⚠️ Entrada inválida.")

jogar()
