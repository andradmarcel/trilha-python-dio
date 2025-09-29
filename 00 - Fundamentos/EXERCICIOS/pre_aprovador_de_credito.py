


while True:
    try:
        nome = input("Digite seu nome: ")
        salario = float(input("Digite seu salario: R$ "))
        valor_emprestimo = float(input("Digite o valor do emprestimo: R$ "))
        parcelas = int(input("Em quantas parcelas voce deseja pagar? "))
        
        porcentagem_salario = salario * 0.30
        parcela_mensal = valor_emprestimo / parcelas
        
        if parcela_mensal >= porcentagem_salario:
            print("Empréstimo Recusado. O valor da parcela excede 30% do seu salário.")
        elif valor_emprestimo >= salario * 5:
            print("Empréstimo Recusado. O valor total solicitado excede 5 vezes o seu salário.")
        else:
            print("Empréstimo Aprovado!")
            print(f"Sua parcela ficou no valor de R$ {parcela_mensal:.2f}")
        
        sair = input("Sair? [s/n]: ")
        if sair.lower() == "s":
            break
        
    except ValueError:
        print("ERRO: Por favor, insira um valor numérico válido para salário, empréstimo ou parcelas. Tente novamente.")
    except Exception as e:
        print(f"\nOcorreu um erro inesperado: {e}\n")
        break