def calcular_imc(peso, altura):
    # Refinamento: Verificar se a altura é zero para evitar erro de divisão
    if altura == 0:
        return None # Retornamos 'None' para indicar que o cálculo não foi possível
    
    imc = peso / (altura ** 2)
    return imc

# Usando um laço para garantir que recebemos entradas válidas
while True:
    try:
        peso_usuario = float(input("Digite seu peso (em kg): ").replace(',', '.'))
        altura_usuario = float(input("Digite sua altura (em metros): ").replace(',', '.'))
        
        # Chamando a função, como você já fez perfeitamente
        imc_resultado = calcular_imc(peso_usuario, altura_usuario)
        
        if imc_resultado is not None:
            print(f"\nSeu IMC é de: {imc_resultado:.2f}")
            break # Sai do laço, pois o cálculo foi um sucesso
        else:
            print("Erro: A altura não pode ser zero. Tente novamente.")

    except ValueError:
        print("Erro: Por favor, digite apenas números para peso и altura.")
    except ZeroDivisionError:
        # Embora a nossa função agora trate isso, é uma boa prática saber que este erro existe
        print("Erro: A altura não pode ser zero. Impossível calcular.")