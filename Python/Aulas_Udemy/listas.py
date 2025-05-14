# LISTAS
    # Armezenar mais de uma informação em variáveis
    # Manter a sequencia dos dados em uma variável

cidade1 = 'Campinas'
cidade2 = 'São Paulo'
cidade3 = 'Santos'

# Índex         0          -2          -1
cidades = ['Campinas', 'São Paulo', 'Santos']
# Índex         0           1           2

print(f'{cidades[0]}, {cidades[2]}, {cidades[-1]}, {cidades[-2]}')

# Alterar valor dentro da lista
cidades[0] = 'Valinhos' 
print(cidades)

# Adiciona valor ao final da lista
cidades.append('Rio de Janeiro')
print(cidades)

# Remove valor da lista
cidades.remove('Rio de Janeiro')
print(cidades)

# Insere com base o índex
cidades.insert(1, 'Campinas')
print(cidades)

# Retira com base o índex
cidades.pop(0)
print(cidades)

# Organizar em ordem alfabética
cidades.sort()
print(cidades)