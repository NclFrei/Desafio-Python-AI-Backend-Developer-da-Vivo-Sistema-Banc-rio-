def depositar(usuario, deposito, /):
    if deposito > 0:
        usuario['saldo'] += deposito
        print(f"\nO valor de R$ {deposito} foi depositado a sua conta! Agora seu saldo é de R$ {usuario['saldo']:.2f}")
        usuario['extrato'] += f"Depósito: R$ {deposito:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")

def sacar(*, usuario, saque, limite, limite_saques):
    excedeu_saldo = saque > usuario['saldo']
    excedeu_limite = saque > limite
    excedeu_saques = usuario['saques_diarios'] >= limite_saques

    if excedeu_saques:
        print("\nErro! Nosso sistema só permite 3 saques diários. Caso deseje fazer um saque de emergência entre em contato com o seu gerente!")
    else:
        while saque <= 0: 
            print("\nErro! Por favor digite um valor positivo")
            saque = float(input("Qual valor você deseja sacar: "))
            excedeu_saldo = saque > usuario['saldo']
            excedeu_limite = saque > limite

        while excedeu_limite: 
            print("\nErro! Nosso sistema só permite saque no valor máximo de R$ 500,00. Caso deseje fazer um saque maior que o limite entre em contato com o seu gerente!")
            saque = float(input("Qual valor você deseja sacar: "))
            excedeu_saldo = saque > usuario['saldo']
            excedeu_limite = saque > limite

        while excedeu_saldo: 
            print(f"\nErro! Você está tentando sacar um valor maior que o saldo presente na sua conta. Saldo atual de R$ {usuario['saldo']:.2f}")
            saque = float(input("Qual valor você deseja sacar: "))
            excedeu_saldo = saque > usuario['saldo']
            excedeu_limite = saque > limite

        usuario['saldo'] -= saque
        print(f"\nO valor de R$ {saque} foi descontado da sua conta! Agora seu saldo é de R$ {usuario['saldo']:.2f}")
        usuario['saques_diarios'] += 1
        usuario['extrato'] += f"Saque: R$ {saque:.2f}\n"

def exibir_extrato(usuario, /):
    print("\n===========Extrato===========")
    print(f"Usuário: {usuario['nome']}")
    print("Não foram realizadas movimentações." if not usuario['extrato'] else usuario['extrato'])
    print(f"\nSaldo: R$ {usuario['saldo']:.2f}")
    print("=============================")

def criar_usuario(usuarios):
    print("================ Criar a conta de Usuário ================")
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe usuário com esse CPF!")
        return None

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    novo_usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco,
        "saldo": 0,
        "extrato": "",
        "saques_diarios": 0
    }
    usuarios.append(novo_usuario)

    print("=== Usuário criado com sucesso! ===")
    return novo_usuario

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não encontrado, impossivel criar a conta!")
    return None

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print((linha))

def menu(usuario):
    menu = f"""\n
    ================ MENU ================
    Usuário: {usuario['nome']}
    Saldo disponível: R$ {usuario['saldo']:.2f}

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [c] Novo Usuário
    [v] Criar Conta Corrente
    [r] Listar Contas
    [w] Acessar Outro Usuário
    [q] Sair

    => """
    return input(menu)

def acessar_usuario(usuarios):
    cpf = input("Informe o CPF do usuário que deseja acessar: ")
    usuario_acessado = filtrar_usuario(cpf, usuarios)
    if usuario_acessado:
        print(f"\nUsuário {usuario_acessado['nome']} acessado com sucesso!")
        return usuario_acessado
    else:
        print("\nUsuário não encontrado!")
        return None

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    usuarios = []
    contas = []

    # Exigir a criação do usuário antes de acessar o menu principal
    usuario = None
    while not usuario:
        usuario = criar_usuario(usuarios)

    while True:
        opcao = menu(usuario)

        if opcao == "d":
            deposito = float(input("Qual valor você deseja depositar: "))
            depositar(usuario, deposito)

        elif opcao == "s":
            saque = float(input("Informe o valor do saque: "))
            sacar(
                usuario=usuario,
                saque=saque,
                limite=500,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(usuario)

        elif opcao == "c":
            novo_usuario = criar_usuario(usuarios)
            if novo_usuario:
                usuario = novo_usuario

        elif opcao == "v":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "r":
            listar_contas(contas)

        elif opcao == "w":
            usuario_acessado = acessar_usuario(usuarios)
            if usuario_acessado:
                usuario = usuario_acessado

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
