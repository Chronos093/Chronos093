# Dicionários
#    Utiliza index no formato de keys e values
#    Aceita strings, Integer, Float, Boolean ...
aluno = {'nome': 'Ana', 'idade': 16, 'nota_final': 'A', 'aprovacao': True}

for x in aluno.values():
  print(x)


print()

for keys, values in aluno.items():
  print(keys, values)

print()
##################################################################################
aluno = {
  'nome': 'Ana', 
  'idade': 16, 
  'nota_final': 'A', 
  'aprovacao': True, 
  'materias': ['Fisica', 'Matematica', 'Ingles']
}

print(aluno)
##################################################################################