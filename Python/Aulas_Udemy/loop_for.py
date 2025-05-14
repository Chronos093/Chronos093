# Loops

# Números
for number in range(5):
  print(number)


print("\n")
# Letras/ Palavras
palavra = 'Google'

for letra in palavra:
  print(f'A letra {letra} está na palavra {palavra}.')


print("\n")
# Colocar espaços entre as letras
for spaco in palavra:
  print(f' {spaco}', end='')


print("\n")
# loop and if
compra_confirmada = True
dados_compra = 'Compra no valor de 12,50 e entrega confirmada.'

for enviar in range(3):
  if compra_confirmada:
    print(dados_compra)
    print('Detalhes enviados por e-mail.')
    break
  else:
    print('Falha na compra.')
    break


print('\n')
# Inner Loops
for numero1 in range(6):
  print(f'Produto {numero1}: ')
  
  for numero2 in range(6):
    print(f'    {numero1} - {numero2}')

  print('\n')