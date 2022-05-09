def ord(list):
  list.sort(reverse=True)
  print(list)

if __name__ == '__main__':
  x = int(input("Digite um número: "))
  y = int(input("Digite um número: "))
  z = int(input("Digite um número: "))

  list = [x, y, z]
  ord(list)