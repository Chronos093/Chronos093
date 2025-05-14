# Laços dentro de listas

valores = [50, 80, 110, 150, 170]

for x in valores:
  print(f'O valor final do produto é de R$ {x}.')


print()
#==========================================================================
cores = ['AMARELO', 'VERDE', 'AZUL', 'VERMELHO']
cor_cliente = input('Digite a cor desejada: ').upper()

if cor_cliente in cores:
  print('Sim')
else:
  print('Não')

print()
#==========================================================================
# Juntar duas listas
valores = [10, 20, 30, 40]

duas_listas = zip(cores, valores)
print(list(duas_listas))
print()
#==========================================================================
frutas = input('Digite o nome das frutas separados por vírgula: ')

frutas_lista = frutas.split(', ')
print(frutas_lista)
print()
