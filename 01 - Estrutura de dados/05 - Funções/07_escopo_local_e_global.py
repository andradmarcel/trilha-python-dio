salario = 2000


def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario


salario_bonus(500)  # 2500


# A função agora recebe o salário atual como um argumento
# e não modifica mais a variável global. Ela é mais previsível.
def calcular_salario_com_bonus(salario_atual, bonus):
    return salario_atual + bonus


# Para ver o resultado, precisamos usar o print()
novo_salario = calcular_salario_com_bonus(salario, 500)

print(f"O salário original era: R$ {salario}")
print(f"O novo salário com bônus é: R$ {novo_salario}")

