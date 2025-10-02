

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc


peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc_usario = calcular_imc(peso, altura)

print(f"Seu IMC é de: {imc_usario:.2f}")