string_1 = input("Digite a primeira string: ")
string_2 = input("Digite a segunda string: ")

qtd_string_1 = len(string_1)
qtd_string_2 = len(string_2)

if qtd_string_1 == qtd_string_2:
  result_1 = "As duas strings tem o mesmo tamanho."
else:
  result_1 = "As duas strings são de tamanhos diferentes."

if string_1 == string_2:
  result_2 = "As duas strings possuem o mesmo conteúdo."
else:
  result_2 = "As duas strings possuem conteúdo diferente."

print("A string é, ",string_1,", e a segunda",string_2)
print(result_1)
print(result_2)