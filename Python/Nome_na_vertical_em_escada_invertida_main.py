nome = input("Digite o nome: ")

qtd_letras = len(nome)

while qtd_letras >= 0:
    print(nome[0:qtd_letras])

    qtd_letras = qtd_letras - 1
