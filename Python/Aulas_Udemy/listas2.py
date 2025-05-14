# CONCATENAR LISTAS

numeros = [2, 3, 4, 5]
letras = ['a', 'b', 'c', 'd']

final = numeros + letras
print(final)
print()

numeros.extend(letras)
print(numeros)
print()

# Lista dentro de lista
itens = [['item1', 'item2'], ['item3', 'item4']]
print(itens[0][1])
print()

# Unpacking Lists
produtos = ['arroz', 'feijão', 'laranja', 'banana']
# item1 = produtos[0]
# item2 = produtos[1]
# item3 = produtos[2]
item1, item2, item3, *outros = produtos

print(f'{item1}, {item2}, {item3}')
print()
