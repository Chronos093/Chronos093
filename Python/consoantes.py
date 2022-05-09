con = ["B", "C", "D", "F", "G", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Z"]

x = input("Digite uma palavra: ").upper()

num_letras = len(x)
i = 0
n = 0
letra = []

while i < num_letras:
  if x[i] in con:
    n = n + 1
    letra.append(x[i])
  i = i + 1

print("Foi digitado {} consoantes, são elas {}".format(n, letra))