from datetime import datetime

# Classes:
#         Utilizadas para criar Objetos (instances)
#         Objetos são partes dentro de uma Class (instancias)
#         Classes são utilizadas para agrupar dados e funções, podendo reutilizar.


class Funcionario:

    nome = 'Elena'
    sobrenome = 'Cabral'
    data_nascimento = '2022-10-31'


colaborador = Funcionario()

print(colaborador.nome)

print()

####################################################


# criar a classe
class Funcionarios:

    def __init__(self, nome, sobrenome, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = ano_nascimento

    def nome_completo(self):
        return (f'{self.sobrenome}, {self.nome}')

    def idade_funcionario(self):
        ano_atual = datetime.now().year
        self.ano_nascimento = int(ano_atual - self.ano_nascimento)
        return self.ano_nascimento


# criar o objeto
usuario1 = Funcionarios('Elena', 'Cabral', 1983)
usuario2 = Funcionarios('Carol', 'Silva', 2003)

print(usuario1.nome_completo())
# Obs:. Faz mais sentido usar essa forma.
print(Funcionarios.nome_completo(usuario1))
print(Funcionarios.idade_funcionario(usuario1))

####################################################
