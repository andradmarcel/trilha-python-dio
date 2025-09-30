

# Sua lógica perfeita
numeros = list(range(1, 21))
quadrado_dos_pares = [numero**2 for numero in numeros if numero % 2 == 0]

print("--- Análise de Dados Numéricos ---")
print(f"\nLista Original (1 a 20):\n{numeros}")
print(f"\nLista com o Quadrado dos Números Pares:\n{quadrado_dos_pares}")