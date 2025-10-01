
def iterar_dicionario(dicionario):
    for chave, valor in dicionario.items():
        print(chave.title(), f"R${valor:.2f}")



catalogo = {"caderno": 15.50, "caneta": 3.00, "camisa": 70.80, "chinelo": 42.90, "estojo": 9.99}



while True:
    
    nome_produto = input("Digite o nome de um produto: ").lower().strip()
    if nome_produto in catalogo:
        print(f"O preço do(a) '{nome_produto}' é de R${catalogo[nome_produto]:.2f}")
        sair = input("Deseja sair do programa? [s/n]").lower().strip()
    else: 
        preco_produto = float(input(f"Produto '{nome_produto}' nao encontrado, digite seu preço para aciona-lo ao catalogo: "))
        catalogo[nome_produto] = preco_produto
        iterar_dicionario(catalogo)
        sair = input("Deseja sair do programa? [s/n] ").lower().strip()
    if sair == "s" or sair == "sim":
        break
    else:
        continue    