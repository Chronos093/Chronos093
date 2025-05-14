# ERROS:
#       Não realiza o 'stop' no programa
#       Mensagens customizadas quando encontrar um erro.

try:
    letras = ['a', 'b', 'c']
    print(letras[3])

except IndexError:
    print('Index não existe.')

print()

#########################################################
# Se precisar executar um pedaço de código depois do try seja ele positivo ou negativo, usar o
# (finally).
# Se precisa tratar o try se a saída for negativa ou positiva, usar então (else).

try:
    valor = int(input('Digite o valor do seu produto: '))
    print(valor)

except ValueError:
    print('Favor digitar um valor em números.')

else:
    print('Usuário digitou um valor correto')
    resultado = valor * 2
    print(resultado)

print()

#########################################################
