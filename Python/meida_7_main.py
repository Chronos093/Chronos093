def media(x, y):
  med = int((x + y) / 2)

  if med == 10:
    print("Aprovado com Distinção")
  else:
    if med >= 7:
      print("Aprovado")
    elif med < 7:
      print("Reprovado")

if __name__ == '__main__':
  x = int(input("Digite a primeira nota: "))
  y = int(input("Digite a segunda nota: "))

  media(x, y)