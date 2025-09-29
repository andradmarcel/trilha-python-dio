


preco_original_str = input("Digite o preço do produto: R$ ")
percentual_desconto_str = input("Digite o percentual de desconto (ex: 10 para 10%): ")

preco_original = float(preco_original_str.replace(",", "."))
percentual_desconto = float(percentual_desconto_str.replace(",", "."))

valor_desconto = preco_original * (percentual_desconto / 100)
preco_final = preco_original - valor_desconto

print(f"O valor do desconto é: R$ {valor_desconto:.2f}")
print(f"O preço final com desconto é: R$ {preco_final:.2f}")