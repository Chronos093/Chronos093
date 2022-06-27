def sexo(a):
  if a == 'm':
    print("M - Masculino")
  elif a == 'f':
    print("F - Feminino")
  else:
    print("Sexo inválido")

if __name__ == '__main__':
  a = input("Digite M para Masculino e F para Feminino: ")
  sexo(a)