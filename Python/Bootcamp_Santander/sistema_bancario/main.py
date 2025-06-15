import datetime

# Variáveis de controle
saldo = 0.0
extrato = []
limite_saque = 500.00
saques_diarios = 0
LIMITE_SAQUES = 3

def formatar_moeda(valor):
    return f"R$ {valor:.2f}"

while True:
    print("\n==== MENU ====")
    print("[d] Depositar")
    print("[s] Sacar")
    print("[e] Extrato")
    print("[q] Sair")

    opcao = input("Escolha uma opção: ").lower()

    if opcao == "d":
        valor = float(input("Informe o valor para depósito: R$ "))
        if valor > 0:
            saldo += valor
            extrato.append(f"Depósito: {formatar_moeda(valor)}")
            print("Depósito realizado com sucesso.")
        else:
            print("Valor inválido. Informe um valor positivo.")

    elif opcao == "s":
        if saques_diarios >= LIMITE_SAQUES:
            print("Limite diário de saques atingido.")
            continue

        valor = float(input("Informe o valor para saque: R$ "))
        if valor <= 0:
            print("Valor inválido. Informe um valor positivo.")
        elif valor > saldo:
            print("Saldo insuficiente.")
        elif valor > limite_saque:
            print(f"Limite de saque por operação é de {formatar_moeda(limite_saque)}.")
        else:
            saldo -= valor
            extrato.append(f"Saque: {formatar_moeda(valor)}")
            saques_diarios += 1
            print("Saque realizado com sucesso.")

    elif opcao == "e":
        print("\n====== EXTRATO ======")
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            for item in extrato:
                print(item)
        print(f"\nSaldo atual: {formatar_moeda(saldo)}")

    elif opcao == "q":
        print("Obrigado por utilizar nosso sistema!")
        break

    else:
        print("Opção inválida. Tente novamente.")
