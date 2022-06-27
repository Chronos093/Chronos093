def pos_neg(x):
  if x == 0:
    print("Você digitou o número zero.")
  elif x > 0:
    print("Você digitou um número positivo.")
  else:
    print("Você digitou um número negativo.")

if __name__ == '__main__':
  x = int(input("Digite um número: "))
  pos_neg(x)