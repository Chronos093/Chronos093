def media(x, y):
  media = (x + y) / 2
  if media >= 9:
    print("Sua nota foi A, Situação: Aprovado")
  elif media >= 7.5:
    print("Sua nota foi B, Situação: Aprovado")
  elif media >= 6:
    print("Sua nota foi C, Situação: Aprovado")
  elif media >= 4:
    print("Sua nota foi D, Situação: Reprovado")
  elif media >= 0:
    print("Sua nota foi E, Situação: Reprovado")

if __name__ == '__main__':
  x = float(input("Digite a primeira nota: "))
  y = float(input("Digite a segunda nota: "))

  media(x, y)