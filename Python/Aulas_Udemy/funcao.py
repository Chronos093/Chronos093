# Funções

def saudacao():
  print("Olá, tudo bem?")
  print("Eu sou uma função.")


def somar_dois_numeros():
    numero1 = 10
    numero2 = 5
    resultado = numero1 + numero2
    print(resultado)


def somar_dois_numeros1(numero1, numero2):
    resultado = numero1 + numero2
    print(resultado)


def boas_vindas(nome, quantidade):
    print(f'Olá, {nome}.')
    print(f'Temos {str(quantidade)} laptops em estoque.')


''' 
Parametro Default, Non-Default. 
    Default: Aquele que você define o valor no parametro.
    Non-Default: Aquele que você não define o valor no parametro. 
Ordem correta.
    def nome_funcao(Non-Default, Default):
'''
def funcDefaultOrNot(nome, idade=28):
    print(f'O seu nome é {nome}, e você tem {idade} anos.')


''' 
Função para somar n valores
'''
def soma(*numeros):
    resultado = 0
    for num in numeros:
        resultado += num
        
    return resultado


'''
Função com n argumentos e identificando os parametros.
'''
def agencia(**carro):
    return carro


print(agencia(marca='Gol', cor='Vermelho', motor=1.0))
print(agencia(marca='Gol', cor='Azul', motor=1.0, placa=123456))
print(agencia(marca='Gol', cor='Amarelo', motor=1.6, placa=15156))
#print(soma(2,3,4,7))
#funcDefaultOrNot('Carlos')
#boas_vindas('Marcos', 5)
#boas_vindas('Carlos', 10)
#boas_vindas('Nat', 15)
#somar_dois_numeros1(10, 10)