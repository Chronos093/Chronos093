# Calculadora de IMC - Índice de Massa Corporal

'''
    Qual é a sua Altura em cm:
    Qual é o seu Peso em kg:

    MENOR QUE 18,5 - MAGREZA
    ENTRE 18,5 E 24,9 - NORMAL
    ENTRE 25,0 E 29,9 - SOBREPESO
    ENTRE 30,0 E 39,9 - OBESIDADE
    MAIOR QUE 40,0 - OBESIDADE GRAVE
'''


def imc(peso, altura):
    # IMC = PESO EM KG / (ALTURA EM METROS * ALTURA EM METROS)
    imc = peso / (altura/100)**2 

    if imc < 18.5:
        situacao = 'MAGREZA'
    elif imc >= 18.5 and imc < 24.9:
        situacao = 'NORMAL'
    elif imc >= 25 and imc < 29.9:
        situacao = 'SOBREPESO'
    elif imc >= 30 and imc < 39.9:
        situacao = 'OBESIDADE'
    elif imc > 40:
        situacao = 'OBESIDADE GRAVE'
    else:
        situacao = 'ERRO AO EFETUAR ANÁLISE'

    return situacao


altura = float(input('Qual é a sua Altura em cm: '))
peso = float(input('Qual é o seu Peso em kg: '))

sitIMC = imc(peso, altura)

print(f'A sua situação é, {sitIMC}')