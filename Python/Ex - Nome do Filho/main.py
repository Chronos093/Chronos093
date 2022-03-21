import random

if __name__ == '__main__':
    nome = ['Levi', 'Lucca', 'Luiz', 'Luan', 'Leon', 'Lúcio', 'Leo']
    nome_meio = ['Davi', 'Raphael', 'Alberto', 'Gustavo', 'Marcos', '']
    sobrenome = ['Reis Gois', 'Reis de Gois', 'de Reis Gois', 'Gois', 'Reis']
    
    new_nome = random.choice(nome)
    new_nome_meio = random.choice(nome_meio)
    new_sobrenome = random.choice(sobrenome)

    print(f'O nome do meu novo filho é {new_nome}  {new_nome_meio} {new_sobrenome}!')