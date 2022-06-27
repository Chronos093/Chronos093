def comp(z):
  maior = max(z)
  return(maior)

if __name__ == '__main__':
  x = int(input("Digite um valor: "))
  y = int(input("Digite um valor: "))

  z = [x, y]

  print(f"O maior valor é, {comp(z)}")