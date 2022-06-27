def calc(x):
  if x < 280:
    ajus = 0.2
    acres = x * ajus
    novo = x + acres
    por = "20%"
    return(acres, novo, por)
  elif x < 700:
    ajus = 0.15
    acres = x * ajus
    novo = x + acres
    por = "15%"
    return(acres, novo, por)
  elif x < 1500:
    ajus = 0.1
    acres = x * ajus
    novo = x + acres
    por = "10%"
    return(acres, novo, por)
  elif x >= 1500:
    ajus = 0.05
    acres = x * ajus
    novo = x + acres
    por = "5%"
    return(acres, novo, por)
if __name__ == '__main__':
  x = float(input("Digite o salário atual: "))

  acres, novo, por = calc(x)
  acres = str(acres)
  novo = str(novo)
  atual = str(x)
  
  print("O salário atual é, " + atual)
  print("Valor do reajuste, " + por)
  print("Aumento de, " + acres)
  print("Novo salário, " + novo)