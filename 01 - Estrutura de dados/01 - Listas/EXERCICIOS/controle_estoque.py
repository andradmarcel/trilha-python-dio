


estoque = ["camiseta", "calça", "camiseta", "sapato", "bermuda", "camiseta"]
menu = """
================= ESTOQUE LOJA ================= 
1 - Verificar quantidade de um produto
2 - Adicionar novo produto ao estoque
3 - Exibir estoque atual (em ordem)
4 - Devolver último produto adicionado
5 - Sair do programa de estoque
================================================
"""

while True:
    print(menu)
    try:
        escolha = int(input("Escolha uma das opções acima: "))
        
        # --- Refinamento 1: Toda a lógica de menu vai para dentro do 'try' ---
        
        if escolha == 1:
            nome_produto = input("Digite o nome do produto: ").lower().strip()
            quantidade = estoque.count(nome_produto)
            print(f"\nTemos {quantidade} unidade(s) de '{nome_produto}' no estoque.\n")
            
        elif escolha == 2:
            nome_produto = input("Digite o nome do produto que você quer adicionar: ").lower().strip()
            estoque.append(nome_produto)
            print(f"\nO produto '{nome_produto}' foi adicionado ao estoque!\n")
            
        elif escolha == 3:
            # É uma boa prática não modificar a lista original se o objetivo é apenas exibir.
            # Usamos sorted() para criar uma CÓPIA ordenada para exibição.
            print("\n--- Estoque Atual (Ordenado) ---")
            for item in sorted(estoque):
                print(f"- {item.title()}")
            print("-" * 32 + "\n")
            
        elif escolha == 4:
            # --- Refinamento 2: Usando a ferramenta correta para o problema ---
            # O .pop() remove e RETORNA o último item da lista.
            if len(estoque) > 0: # Boa prática: verificar se a lista não está vazia
                item_removido = estoque.pop()
                print(f"\nO último item, '{item_removido}', foi devolvido.\n")
            else:
                print("\nO estoque já está vazio!\n")

        elif escolha == 5:
            print("\nSaindo do programa de estoque. Até logo!")
            break
            
        else: # Trata números fora do intervalo, como 6, 7, 0, -1...
            print("\nOpção inválida. Por favor, digite um número entre 1 e 5.\n")
            
    except ValueError:
        print("\nErro! Por favor, digite um número válido para a opção do menu.\n")