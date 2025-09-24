def sacar(saldo, valor):
    if saldo >= valor:
        saldo -= valor
        print(f"valor sacado {valor}!")
        print("retire o seu dinheiro na boca do caixa.")
        return saldo
    else:
        print("Saldo insuficiente!")
        return saldo


def depositar(saldo, valor):
    saldo += valor
    print("Depósito realizado com sucesso!")
    return saldo


saldo_conta = 500
print(f"Saldo inicial: R$ {saldo_conta}")

saldo_conta = depositar(saldo_conta, 200)
print(f"Saldo após depósito: R$ {saldo_conta}")

saldo_conta = sacar(saldo_conta, 150)
print(f"Saldo após saque: R$ {saldo_conta}")

print("\nObrigado por ser nosso cliente, tenha um bom dia!")
