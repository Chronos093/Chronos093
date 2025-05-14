# Map Function
#    Muito utilizado com listas
#    Aplicar uma função a um Iterable, por item, (list, tuple, dicetc.)

lista1 = [1, 2, 3, 4]

lista2 = map(lambda x: x * 2, lista1)

print(list(map(lambda x: x * 2, lista1)))
print()
########################################################################
valores = [10, 12, 34, 44, 57]

def remover20(x):
  return x > 20

print(list(filter(remover20, valores)))

print(list(filter(lambda x: x > 20, valores)))
print()
########################################################################