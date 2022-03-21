import random

if __name__ == '__main__':
    
    def add_nomes():
        nomes = input("Digite os nomes escolhidos separados por espaço (Exem: Nome1 Nome2): ")
        list_Nomes = nomes.split()
        new_Nome = random.choice(list_Nomes)
        return(new_Nome)  
    def add_nome_meio():
        meio = input("Digite os nomes do meio separados por espaço: ")
        list_Meio = meio.split()
        new_Meio = random.choice(list_Meio)
        return(new_Meio)
    def add_sobrenome():
        sobrenome = input("Digite os SobreNomes separador por espaço: ")
        list_Sobrenome = sobrenome.split()
        new_Sobrenome = random.choice(list_Sobrenome)
        return(new_Sobrenome)
    def add_sobrenome2():
        sobrenome = input("Digite o segundo SobreNomes separador por espaço, caso não tenha deixe em branco: ")
        list_Sobrenome = sobrenome.split()
        if len(list_Sobrenome) == 0:
            new_Sobrenome = " "
        else:
            new_Sobrenome = random.choice(list_Sobrenome)
        return(new_Sobrenome)
    
    print(f"O nome do bebe é: {add_nomes()} {add_nome_meio()} {add_sobrenome()} {add_sobrenome2()}")