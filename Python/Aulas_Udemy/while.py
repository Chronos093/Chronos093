# Loops While
valor = 40
dia = 1


while valor > 20:
  print(f'No dia {dia} o produto custara R$ {valor}.')
  dia += 1
  valor -= 5


print('\n')
# Publicar um produto com comissão de 10% se for acima de R$ 20
preco = int(input("Digite o valor do produto em R$: "))


while preco > 20:
  preco = (preco * 0.10) + preco
  print(f'O valor final do produto é R$ {preco}')
  break