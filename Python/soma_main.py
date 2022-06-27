def calc(l):
  i = 0
  soma = 0
  num_registros = len(l) - 1
  
  while i <= num_registros:
    soma = l[i] + soma
    i += 1  
  print()
  print("O valor da soma é, ", soma)
  
if __name__ == '__main__':
  c = "s"
  l = []
  while c == "s":
    l.append(int(input("Digite o número: ")))
    c = input("Deseja adicionar um novo número, s (sim)  n (não): ")

  calc(l)