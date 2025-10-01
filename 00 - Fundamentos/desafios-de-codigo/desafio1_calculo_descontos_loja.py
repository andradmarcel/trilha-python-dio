# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20
}

# Entrada do usuário
preco = float(input().strip())
cupom = input().strip().upper() # Converte para maiúsculas para corresponder às chaves

# Busca o fator de desconto no dicionário. Se não encontrar, o padrão é 0.0.
fator_desconto = descontos.get(cupom, 0.0)

# Calcula o preço final de forma direta
preco_final = preco * (1 - fator_desconto)
    
print(f"{preco_final:.2f}")