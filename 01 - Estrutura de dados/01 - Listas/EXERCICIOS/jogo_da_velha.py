# A função para verificar o vencedor é a grande novidade aqui.
def verificar_vencedor(tabuleiro):
    # Verificar linhas
    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2] and linha[0] != ' ':
            return linha[0]  # Retorna 'X' ou 'O'

    # Verificar colunas
    for col in range(3):
        if tabuleiro[0][col] == tabuleiro[1][col] == tabuleiro[2][col] and tabuleiro[0][col] != ' ':
            return tabuleiro[0][col]

    # Verificar diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][0] != ' ':
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[0][2] != ' ':
        return tabuleiro[0][2]

    # Se nenhuma das condições acima for atendida, não há vencedor.
    return None

# Função de exibição que já tínhamos, com uma pequena melhoria.
def exibir_tabuleiro(tabuleiro_atual):
    print("\n   0   1   2")
    print("  -----------")
    for indice, linha in enumerate(tabuleiro_atual):
        print(f"{indice} | {' | '.join(linha)} |")
        print("  -----------")

# --- LAÇO PRINCIPAL DO PROGRAMA (CONTROLA SE JOGAMOS DE NOVO) ---
while True:
    # Reinicia o tabuleiro e as variáveis para cada nova partida
    tabuleiro = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    jogador_atual = "X"
    total_jogadas = 0
    vencedor = None

    # --- LAÇO DA PARTIDA ---
    while total_jogadas < 9:
        exibir_tabuleiro(tabuleiro)
        
        while True:
            try:
                print(f"\nVez do Jogador '{jogador_atual}'")
                linha = int(input("Digite a linha (0, 1 ou 2): "))
                coluna = int(input("Digite a coluna (0, 1 ou 2): "))

                if not (0 <= linha <= 2 and 0 <= coluna <= 2):
                    print("Posição inválida! Jogue dentro do tabuleiro (0 a 2).")
                elif tabuleiro[linha][coluna] != ' ':
                    print("Esta casa já está ocupada! Escolha outra.")
                else:
                    break
            except ValueError:
                print("Entrada inválida! Por favor, digite um número.")

        tabuleiro[linha][coluna] = jogador_atual
        total_jogadas += 1

        # Após cada jogada, verificamos se há um vencedor
        vencedor = verificar_vencedor(tabuleiro)
        if vencedor:
            exibir_tabuleiro(tabuleiro)
            print(f"\n--- FIM DE JOGO ---")
            print(f"O Jogador '{vencedor}' venceu a partida!")
            break # Quebra o laço da partida

        # Alterna o jogador
        jogador_atual = "O" if jogador_atual == "X" else "X"

    # Se o laço da partida terminou sem vencedor, foi empate.
    if not vencedor:
        exibir_tabuleiro(tabuleiro)
        print("\n--- FIM DE JOGO ---")
        print("Deu velha! (Empate)")

    # --- LÓGICA PARA JOGAR NOVAMENTE ---
    while True:
        jogar_novamente = input("\nDeseja jogar novamente? [s/n]: ").lower().strip()
        if jogar_novamente in ["s", "sim", "n", "nao", "não"]:
            break
        else:
            print("Resposta inválida. Por favor, digite 's' ou 'n'.")

    if jogar_novamente in ["n", "nao", "não"]:
        print("\nObrigado por jogar! Até a próxima!")
        break # Quebra o laço principal e encerra o programa