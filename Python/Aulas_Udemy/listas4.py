from array import array
# Array (Matriz)
'''
letras = ['a', 'b', 'c', 'd']
numeros_i = [10, 20, 30, 40]
numeros_f = [1.2, 2.2, 3.2]

print(letras)
print(numeros_i)
print(numeros_f)
print()
'''
letras = array('u', ['a', 'b', 'c', 'd'])
numeros_i = array('i', [10, 20, 30, 40])
numeros_f = array('f', [1.2, 2.2, 3.2])

#print(letras)
#print(numeros_i)
#print(numeros_f)

print()
#=========================================================================
# SET (LISTAS)
    # Similar a listas
    # Evita itens duplicados
    # Não utiliza index

list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 60, 70]

num1 = set(list1)
num2 = set(list2)

print(f'Primeira lista: {list1}')
print(f'Segunda lista: {list2}')
# | = União (Union)
print(f'União entre as listas: {num1 | num2}')

# - = Diferença (Difference)
print(f'A diferença da lista1 para a lista2: {num1 - num2}')
print(f'A diferença da lista2 para a lista1: {num2 - num1}')

# ^ = Não mostra os Dublicados (Symmetric Difference)
print(f'Não exibe os valores duplicados nas listas: {num1 ^ num2}')

# & = Mostra oque tem Dublicado nas duas listas
print(f'Mostra os valores duplicados nas duas listas: {num1 & num2}')
print()
#=========================================================================
# Outra forma de declarar o set
list_num = {1, 2, 3, 4, 5}
print(type(list_num))

# Adiciona itens ao set
list_num.add(6)

# Adicionar mais de um item, se repetir valor que já existe ele ignora
list_num.update([7, 8, 9, 10])

# Remover item, remove=Caso não existe retorna erro, discard=Caso não existe NÃO retorna erro
list_num.remove(10)
list_num.discard(12)

print(list_num)