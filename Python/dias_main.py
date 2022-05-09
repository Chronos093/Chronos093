def segunda():
  print("2 - Segunda")
def terca():
  print("3 - Terça-Feira")
def quarta():
  print("4- Quarta-Feira")
def quinta():
  print("5 - Quinta-Feira")
def sexta():
  print("6 - Sexta-Feira")
def sabado():
  print("7 - Sábado")
def domingo():
  print("1 - Domingo")
def default():
  print("Valor Inválido")

def switch(case):
  if case == "1":
    return domingo
  elif case == "2":
    return segunda
  elif case == "3":
    return terca
  elif case == "4":
    return quarta
  elif case == "5":
    return quinta
  elif case == "6":
    return sexta
  elif case == "7":
    return sabado
  else:
    return default

if __name__ == "__main__":
  case = input("Digite o número do dia: ")
  
  function = switch(case)
  function()  