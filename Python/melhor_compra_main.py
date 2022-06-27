def comp(lista):
  menor = str(min(lista))
  return(menor)

if __name__ == '__main__':
  x = float(input("Digite um valor do produto: "))
  y = float(input("Digite um valor do produto: "))
  z = float(input("Digite um valor do produto: "))

  lista = [x, y, z]

  menor = comp(lista)

  print("Compre o produto com o valor, R$ " + menor)