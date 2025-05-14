# Desafio com Funções

'''
    Criar um programa que calcula a quantidade de tinta necessária para pintar uma parede.
O usuário deverá fornecer as seguintes informações:
    - Rendimento;
    - Largura;
    - Altura;
O programa deve mostrar na tela a mensagem "Você necessita de 'x' latas de tinta"

Quantidade de latas =     A área da parede
                     ---------------------------
                     Rendimento da lata de tinta
'''

def calcRendimento(rendimento, altura, largura):
    calcArea = altura * largura
    calLatas = calcArea / rendimento

    return f'Você necessita de {calLatas} latas de tinta'


rendimento = float(input('Digite o rendimento da lata de tinta: '))
altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))

print(calcRendimento(rendimento, altura, largura))