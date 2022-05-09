def inverter(nome):
    nome_inverso = nome[::-1].upper()
    print(nome_inverso)


if __name__ == "__main__":
    nome = input("Digite o nome: ")
    qtd_letras = len(nome) - 1

    inverter(nome)