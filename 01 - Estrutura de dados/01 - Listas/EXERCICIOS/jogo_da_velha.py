


tabuleiro = [
    [' ', ' ', ' '],  
    [' ', ' ', ' '],  
    [' ', ' ', ' ']   
]

def exibir_tabuleiro(tabuleiro_atual):
    print("---------")
    for linha in tabuleiro_atual:
        print(" | ".join(linha))
        print("---------")
    
    
exibir_tabuleiro(tabuleiro)    
    
print("Vez do Jogador 1 (X)")
linha_x = int(input("Digite a linha (0, 1 ou 2): "))
coluna_x = int(input("Digite a coluna (0, 1 ou 2): "))

tabuleiro[linha_x][coluna_x] = 'X'
exibir_tabuleiro(tabuleiro)

print("Vez do Jogador 2 (O)")
linha_o = int(input("Digite a linha (0, 1 ou 2): "))
coluna_o = int(input("Digite a coluna (0, 1 ou 2): "))

tabuleiro[linha_o][coluna_o] = 'O'
exibir_tabuleiro(tabuleiro)

        
            
