def menu():
    return """
[d] Depositar
[s] Sacar
[e] Extrato
[u] Criar Usuário
[c] Criar Conta
[q] Sair
=> """


def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! Valor inválido.")
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("Operação falhou! Saldo insuficiente.")
    elif valor > limite:
        print("Operação falhou! Valor excede o limite.")
    elif numero_saques >= limite_saques:
        print("Operação falhou! Limite de saques diários excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("Operação falhou! Valor inválido.")
    return saldo, extrato, numero_saques


def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Sem movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=========================================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe usuário com este CPF.")
        return

    nome = input("Nome completo: ")
    data_nasc = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço (logradouro, nº - bairro - cidade/UF): ")

    usuarios.append({
        "nome": nome,
        "data_nasc": data_nasc,
        "cpf": cpf,
        "endereco": endereco
    })

    print("Usuário criado com sucesso!")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [u for u in usuarios if u["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, contas, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print("Usuário não encontrado! Cadastre primeiro.")
        return

    numero_conta = len(contas) + 1
    contas.append({
        "agencia": agencia,
        "numero": numero_conta,
        "usuario": usuario
    })
    print(f"Conta criada com sucesso! Agência: {agencia}, Número: {numero_conta}")


# ===== Programa Principal =====

AGENCIA = "0001"
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
contas = []

while True:
    opcao = input(menu())

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES
        )

    elif opcao == "e":
        exibir_extrato(saldo, extrato)

    elif opcao == "u":
        criar_usuario(usuarios)

    elif opcao == "c":
        criar_conta(AGENCIA, contas, usuarios)

    elif opcao == "q":
        print("Saindo... até logo!")
        break

    else:
        print("Operação inválida, tente novamente.")
