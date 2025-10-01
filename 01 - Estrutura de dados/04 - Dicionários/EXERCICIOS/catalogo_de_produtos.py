def iterar_dicionario(dicionario):
    print("\n--- Catálogo Atualizado ---")
    for chave, valor in dicionario.items():
        # A formatação que você criou ficou ótima!
        print(f"{chave.title()}: R${valor:.2f}")
    print("--------------------------")

catalogo = {"caderno": 15.50, "caneta": 3.00, "camisa": 70.80, "chinelo": 42.90, "estojo": 9.99}

print("--- Bem-vindo ao Catálogo da Loja! ---")

while True:
    nome_produto = input("\nDigite o nome de um produto para consultar ou 'sair' para encerrar: ").lower().strip()
    
    # Uma forma mais direta de sair, sem precisar de uma segunda pergunta.
    if nome_produto == 'sair':
        print("Obrigado por utilizar nosso catálogo. Volte sempre!")
        break

    if nome_produto in catalogo:
        print(f"O preço do(a) '{nome_produto}' é de R${catalogo[nome_produto]:.2f}")
    else: 
        try:
            preco_produto_str = input(f"Produto '{nome_produto}' não encontrado. Digite seu preço para adicioná-lo ao catálogo: R$").replace(',', '.')
            preco_produto = float(preco_produto_str)
            
            catalogo[nome_produto] = preco_produto
            print(f"Produto '{nome_produto}' adicionado com sucesso!")
            
            # Opcional: Mostrar o catálogo apenas quando for atualizado
            iterar_dicionario(catalogo)
            
        except ValueError:
            print("Erro: Preço inválido. O produto não foi adicionado.")

    # A pergunta de "sair" foi substituída por uma instrução mais clara no início.
    # Isso deixa o fluxo mais limpo, sem interrupções a cada consulta.