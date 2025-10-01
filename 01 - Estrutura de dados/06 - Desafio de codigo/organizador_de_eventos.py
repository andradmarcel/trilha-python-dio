# Dicionário para agrupar participantes por tema
eventos = {}

# Entrada do número de participantes
n = int(input().strip())

# TODO: Crie um loop para armazenar participantes e seus temas:
for _ in range(n):
    # 1. Lê a linha de entrada, ex: "Lucas, Fotografia"
    entrada = input()
    
    # 2. Separa o nome e o tema usando a vírgula como divisor.
    #    A função .split(',') retorna uma lista com duas partes.
    nome, tema = entrada.split(',')
    
    # 3. Remove espaços em branco extras do tema.
    tema = tema.strip()
    
    # 4. Verifica se o tema já é uma chave no dicionário.
    if tema in eventos:
        # Se o tema já existe, adiciona o nome à lista de participantes.
        eventos[tema].append(nome)
    else:
        # Se o tema não existe, cria a chave e inicia sua lista com o nome atual.
        eventos[tema] = [nome]

# Exibe os grupos organizados (seu código original aqui, já estava perfeito)
for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")