# Definindo as variáveis
saldo = 0
limite_saque = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

# Função de menu
def exibir_menu():
    print("\nEscolha a operação:")
    print("d - Depósito")
    print("s - Saque")
    print("e - Extrato")
    print("q - Sair")

while True:
    exibir_menu()
    opcao = input("Digite a opção desejada: ")

    if opcao == "d":
        valor = float(input("Valor do depósito: R$ "))
        if valor > 0:
            saldo += valor
            extrato.append(f"Depósito: R$ {valor:.2f}")
            print("Depósito realizado com sucesso!")
        else:
            print("O valor do depósito deve ser positivo.")

    elif opcao == "s":
        if numero_saques < LIMITE_SAQUES:
            valor = float(input("Valor do saque: R$ "))
            if valor <= saldo and valor <= limite_saque:
                saldo -= valor
                numero_saques += 1
                extrato.append(f"Saque: R$ {valor:.2f}")
                print("Saque realizado com sucesso!")
            else:
                print("Saque não realizado. Verifique o valor ou o saldo disponível.")
        else:
            print("Limite de saques diários atingido.")

    elif opcao == "e":
        if extrato:
            print("\nExtrato de transações:")
            for transacao in extrato:
                print(transacao)
            print(f"Saldo atual: R$ {saldo:.2f}\n")
        else:
            print("Não foram realizadas movimentações.")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

