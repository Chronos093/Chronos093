# Desafio com 'Sets'

'''
    Criar um programa que gera 3 listas de acordo com a necessidade logo abaixo:
Lista1 = Funcionários que tem carro e trabalha a noite
Lista2 = Funcionários que tem carro e trabalha durante o dia
Lista3 = Fuincionários que não tem carro
'''

funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa']
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turno_noite = ['Pedro', 'Sophia', 'Bruno']
tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']


print(f'Funcionários que tem carro no turno da noite, {set(turno_noite).intersection(set(tem_carro))}')

print(f'Funcionários que tem carro no turno do dia, {set(turno_dia).intersection(set(tem_carro))}')

print(f'Funcionários que não tem carro, {set(funcionarios).difference(set(tem_carro))}')