if __name__ == '__main__':
    def user(nome, nasc, uf):
        nome2 = nome.split()
        nasc2 = nasc.split('/')
        
        newUSER = uf + nome2[1] + nasc2[2]
        return(newUSER)
        
    nome = str(input('Digite o nome: '))
    nasc = str(input('Digite a data de nascimento (Exm: MM/DD/AAAA): '))
    uf = str(input('Digite o estado (Exm: AA): '))
    
    print(user(nome, nasc, uf))