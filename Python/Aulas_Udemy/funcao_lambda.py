# Lambda Function
#    É uma função (pequena) sem nome
#    Pode ter vários argumentos mas somente 1 expressão
#    Muito utilizada dentro de outras funções
#    Código mais 'clean', limpo

somar10 = lambda x: x + 10

print(somar10(2))

# Exemplo de uso

def somar(x):
  func2 = lambda x: x + 10
  return func2(x) * 4

print(somar(2))