if __name__ == '__main__':
    def media(a, b, c, d, e):
        total = (a + b + c + d + e) / 5
        return (total)

    a = int(input('Digite a primeira nota: '))
    b = int(input('Digite a segunda nota: '))
    c = int(input('Digite a terceira nota: '))
    d = int(input('Digite a quarta nota: '))
    e = int(input('Digite a quinta nota:'))

    if media(a, b, c, d, e) > 6:
        sit = "Aprovado"
    elif media(a, b, c, d, e) > 3:
        sit = "Recuperação"
    elif media(a, b, c, d, e) > 1:
        sit = "Reprovado"
    else :
        sit = "Sai dessa cara"

    print(f'A média desse aluno é {media(a, b, c, d, e)} e a situação é {sit}')

