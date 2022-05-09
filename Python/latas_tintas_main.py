def latas(m):
    m2_lata = 54
    list = [0]
    i = 1
    ult = 0

    while ult < m:
        list.append(m2_lata * i)
        ult = list[len(list) - 1]
        i += 1

    qtd_latas = len(list) - 1
    preco_final = qtd_latas * 80

    return (qtd_latas, preco_final)


if __name__ == '__main__':
    m = int(input("Digite o M² da parede: "))
    qtd_latas, preco = latas(m)
    print("A quantidade de latas é, ", qtd_latas)
    print("O valor a pagar é, R$", preco)
