num = 1
list = []
par = []
impar = []
while num:
  num = input("Insira um número: ")   
  if num == "":
    break
  else:
    list.append(num)
    num = int(num)
    if (num % 2) == 0:
      par.append(num)
    else:
      impar.append(num)

print("Os números digitados foram, {}".format(list))
print("Os números pares, {}".format(par))
print("Os números ímpares, {}".format(impar))