# Dicionários
#    Utiliza index no formato de keys e values
#    Aceita strings, Integer, Float, Boolean ...
aluno = {'nome': 'Ana', 'idade': 16, 'nota_final': 'A', 'aprovacao': True}

print(aluno['nome'])
print()
##########################################################################
# Alterar valor dentro do dicionário
aluno['nome'] = 'Jose'

print(aluno['nome'])
#    Altera mais de um campo ao mesmo tempo
aluno.update({'nome': 'Osvaldo', 'nota_final': 'B'})

print(aluno)
print()
##########################################################################
# Adicionar campo ao dicionário, no fim
aluno.update({'endereco': 'Rua A'})

print(aluno)
print(aluno.get('cidade', 'Campo(s) não encontrado ou não existe.'))

aluno.update({'cidade': 'Campinas'})
print(aluno.get('cidade', 'Campo(s) não encontrado ou não existe.'))
print()
##########################################################################
# Remover itens
del aluno['idade']

print(aluno)