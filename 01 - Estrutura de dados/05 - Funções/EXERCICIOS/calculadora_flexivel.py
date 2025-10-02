def somar_numeros(*args):
    return sum(args)

# --- Coletando os números do usuário ---
numeros_do_usuario = []
print("--- Calculadora de Soma Flexível ---")
print("Digite os números que deseja somar. Para calcular, digite 'fim'.")

while True:
    entrada = input("Digite um número (ou 'fim'): ").strip().lower()

    if entrada == 'fim':
        break  

    try:
        numero = float(entrada.replace(',', '.'))  # Permite que o usuário use vírgula
        numeros_do_usuario.append(numero)
    except ValueError:
        print("Entrada inválida. Por favor, digite apenas números ou 'fim'.")

# Usamos o operador '*' para desempacotar a lista como argumentos para a função
soma_final = somar_numeros(*numeros_do_usuario)
print(f"\nA soma de todos os números digitados é: {soma_final}")