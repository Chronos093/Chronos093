#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

def saud(t):
  if t == "m":
    print("Bom Dia!")
  elif t == "v":
    print("Boa Tarde!")
  elif t == "n":
    print("Boa Noite!")
  else:
    print("Valor Inválido!")

if __name__ == '__main__':
  print("Em qual turno você estuda.")
  print("M-Matutino")
  print("V-Vespertino")
  print("N-Noturno")
  t = input()

  saud(t)