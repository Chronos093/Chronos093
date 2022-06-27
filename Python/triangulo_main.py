def confLados(x, y, z):
  som = x + y
  if som > z:
    print("Este é um triângulo")
  else:
    print("Este não é um triângulo")

if __name__ == '__main__':
  x = float(input("Digite o primeiro lado: "))
  y = float(input("Digite o segundo lado: "))
  z = float(input("Digite o terceiro lado:"))

  confLados(x, y, z)