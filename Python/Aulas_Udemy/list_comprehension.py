# List Comprehension
#    Mais simples de se escrever
#    Utilizado quando você precisa criar uma nova lista a partir de uma existente
#    [expressao dor item in itens]

frutas1 = ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']
'''
frutas2 = []

for item in frutas1:
  if 'b' in item:
    frutas2.append(item)

print(frutas2)
'''

frutas2 = [item for item in frutas1 if 'n' in item]

print(frutas2)
print()
##############################################################
'''
valores = []

for x in range(6):
  valores.append(x * 10)

print(valores)
'''

valores = [x * 10 for x in range(6)]
print(valores)