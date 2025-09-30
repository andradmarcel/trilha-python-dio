


estoque = ["camiseta", "calça", "camiseta", "sapato", "bermuda", "camiseta"]
menu = """
================= ESTOQUE LOJA ================= 
1 - Verificar quantidade do produto digitado
2 - Adicionar novo produto ao estoque
3 - Exibir estoque atualizado
4 - Devolução do item desejado
5 - Sair do programa de estoque
================================================
"""

while True:
    print(menu)
    try:
        escolha = int(input("Escolha uma das opções acima: "))
        if escolha > 5:
            print("Digite um numero entre 1 e 5")
        elif escolha == 5:
            print("Saindo do programa!")
            break            
    except ValueError:
        print("Digite um numero valido")  


    if escolha == 1:
        nome_produto = input("Digite o nome do produto: ")
        print(f"Quantidade do produto {nome_produto}: {estoque.count(nome_produto.lower().strip())}")
        
    elif escolha == 2:
        nome_produto = input("Digite o nome do produto que voce quer adicionar ao estoque: ")
        estoque.append(nome_produto.lower().strip())
        print(f"O produto: {nome_produto.lower().strip()} foi adicionado ao estoque")
        
    elif escolha == 3:
        estoque.sort()
        for item in estoque:
            print(item)
            
    elif escolha == 4:
        nome_produto = input("Qual item voce quer devolver? ")
        estoque.remove(nome_produto.lower().strip())
        print(f"O produto {nome_produto} foi devolvido")
            
        
        
        
        
                
        
    
        
        
            
                  