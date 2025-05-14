# Desafio com If, Elif, Else

'''
    Criar um programa que dependendo da temperatura (em celsius) do steak ele retorne
o ponto de cozimento em portugues. O usuário deverá fornecer a temperatura.

Temperaturas - Cozimento
120ºF ou 48ºC - Rare (Selada)
130ºF ou 54ºC - Medium Rare (Ao ponto para o mal)
140ºF ou 60ºC - Medium (Ao ponto)
150ºF ou 65ºC - Medium well (Ao ponto para o bem)
160ºF ou 71ºC - Well done (Bem passada)
'''

temperatura = float(input("Digite a temperatura do Steak: "))

if temperatura < 48:
    print("O Steak está crú")

if temperatura in range(48, 53):
    print("O Steak está, Selado (Rare)")

elif temperatura in range(54, 59):
    print("O Steak está, Ao ponto para o mal (Medium Rare)")

elif temperatura in range(60, 64):
    print("O Steak está, Ao ponto (Medium)")

elif temperatura in range(65, 70):
    print("O Steak está, Ao ponto para o bem (Medium well)")

elif temperatura > 71:
    print("O Steak está, Queimado !!! (Carvão)")

else:
    print("Temperatura inválida")
