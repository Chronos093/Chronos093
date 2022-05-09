def switch(case):
    if case == "1":
        mes = "Janeiro"
        return mes
    elif case == "2":
        mes = "Fevereiro"
        return mes
    elif case == "3":
        mes = "Março"
        return mes
    elif case == "4":
        mes = "Abril"
        return mes
    elif case == "5":
        mes = "Maio"
        return mes
    elif case == "6":
        mes = "Junho"
        return mes
    elif case == "7":
        mes = "Julho"
        return mes
    elif case == "8":
        mes = "Agosto"
        return mes
    elif case == "9":
        mes = "Setembro"
        return mes
    elif case == "10":
        mes = "Outubro"
        return mes
    elif case == "11":
        mes = "Novembro"
        return mes
    elif case == "12":
        mes = "Dezembro"
        return mes


dta_nasc = input("Digite a data de nascimento: ")

dta_corta = dta_nasc.split("/")

print("Você nasceu em ",dta_corta[0],"de",switch(case=dta_corta[1]),"de",dta_corta[2])
#function = switch(case=dta_corta[1])
#function()
