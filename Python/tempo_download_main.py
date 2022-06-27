def convertMin(tempSeg):
  tempMin = round(tempSeg / 60, 2)
  return tempMin
def calcTemp(tam, vel):
  tempSeg = tam / (vel / 8)

  if tempSeg > 60:
    tempMin = str(convertMin(tempSeg))
    temp = tempMin + " minutos"
  else:
    tempSeg = str(tempSeg)
    temp = tempSeg + " segundos"
    
  return temp
if __name__ == '__main__':
  tam = float(input("Digite o tamanho do arquivo em MB: "))
  vel = int(input("Digite a velocidade da conexão em Mbps: "))

  print(f"O tempo médio de donwload é, {calcTemp(tam, vel)}")