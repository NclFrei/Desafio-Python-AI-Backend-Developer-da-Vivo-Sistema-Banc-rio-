#Desafio
"Fomos contratador por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python. Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato"

#Operação de Depósito 
"Deve ser possível depositar valores positivos para a conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em indentificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato"

#Operação de saque
"O sistema deve permitir realizar 3 saque diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saque devem ser armazenados em uma variável e exibidos na operação de extrato."

#Operação de extrato 
"Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo: 1500.45 = R$ 1500.45"

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES = 3
deposito = 0
saques_diarios = 0

while True: 

    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("Qual valor você deseja depositar: "))

        while deposito <= 0: 
            print("\nErro! Por favor digite um valor positivo")
            deposito = float(input("Qual valor você deseja depositar: "))

        saldo += deposito
        print(f"\nO valor de R$ {deposito} foi adicionado a sua conta! Agora seu saldo é de R$ {saldo}")
        extrato += f"Depósito: R$ {deposito:2f}\n"
    
    elif opcao == "s": 
        if saques_diarios == LIMITE_SAQUES:
            print("\nErro! Nosso sistema só permite 3 saques diários. Caso deseje fazer um saque de emergência entre em contato com o seu gerente!")
        else:
            saque = float(input("Qual valor você deseja sacar: "))

            while saque <= 0: 
                print("\nErro! Por favor digite um valor positivo")
                saque = float(input("\nQual valor você deseja sacar: "))

            while saque >= 500.00: 
                print("\nErro! Nosso sistema só permite saque no valor máximo de R$ 500,00. Caso deseje fazer um saque maior que o limite entre em contato com o seu gerente!")
                saque = float(input("\nQual valor você deseja sacar: "))

            while saque >= saldo: 
                print(f"\nErro! Você está tentando sacar um valor maior que o saldo presente na sua conta. Saldo atual de R$ {saldo}")
                saque = float(input("\nQual valor você deseja sacar: "))

            saldo -= saque
            print(f"\nO valor de R$ {saque} foi descontado da sua conta! Agora seu saldo é de R$ {saldo}")
            saques_diarios += 1
            extrato += f"Saque: R$ {saque:2f}\n"


    elif opcao == "e": 
        print("\n===========Extrato===========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=============================")

    elif opcao == "q":
        break

    else: 
        print("\nOperação inválida, por favor selecione novamente a operação desejada.")