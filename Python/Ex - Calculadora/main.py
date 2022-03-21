def soma(a, b):
    total = a + b
    return(total)

def sub(a, b):
    total = a - b
    return(total)
    
def mul(a, b):
    total = a * b
    return(total)
    
def div(a, b):
    total = a / b
    return(total)
    
def switch(case):
    if case == "soma":
       return(soma(a, b))
    elif case == "subtração":
       return(sub(a, b))
    elif case == "multiplicação":
       return(mul(a, b))
    elif case == "divição":
       return(div(a, b))
    else:
       return("404")
           

if __name__ == '__main__':
    a = int(input('Digite o número: '))
    b = int(input('Digite o número: '))
    op = input(f'Qual a operação, soma, subtração, multiplicação, ou divição.')
    
    if switch(case = op) == "404":
        print("ERRO: Opção invalida.")
    else:
        print(f'O resultado é, {switch(case = op)}')
