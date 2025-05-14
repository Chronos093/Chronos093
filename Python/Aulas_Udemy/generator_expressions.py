from sys import getsizeof

# Generator Expressions
    # Uma forma mais rápida para listas, dicionários e etc.
    # Menos memória alocada
    # Valores em bytes

numeros1 = [x * 10 for x in range(5)]
print(numeros1)
print(getsizeof(numeros1))

print()

numeros2 = (x * 10 for x in range(5))
print(list(numeros2))
print(getsizeof(numeros2))