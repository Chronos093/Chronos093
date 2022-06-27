def comp(lista):
  maior = str(max(lista))
  menor = str(min(lista))
  return(maior, menor)

if __name__ == '__main__':
  x = int(input("Digite um valor: "))
  y = int(input("Digite um valor: "))
  z = int(input("Digite um valor: "))

  lista = [x, y, z]

  maior, menor = comp(lista)

  print("O maior valor é, " + maior + " e o menor, " + menor)