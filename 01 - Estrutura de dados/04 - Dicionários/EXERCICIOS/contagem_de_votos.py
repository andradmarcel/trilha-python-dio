votos = ["Candidato A", "Candidato B", "Candidato A", "Candidato C", "Candidato A", "Candidato B"]
contagem_votos = {}

for candidato in votos:
    # Passo 1: Pergunte ao .get() qual a contagem atual.
    # Se o candidato não existir, ele nos devolve 0.
    contagem_atual = contagem_votos.get(candidato, 0)
    
    # Passo 2: Some 1 à contagem que recebemos.
    nova_contagem = contagem_atual + 1
    
    # Passo 3: Agora sim, ATUALIZE o dicionário com a nova contagem.
    # É aqui que a "mágica" acontece.
    contagem_votos[candidato] = nova_contagem

# Agora o dicionário está completo. Vamos exibi-lo como pedia o exercício.
print("--- Resultado da Votação ---")
for candidato, total_votos in contagem_votos.items():
    print(f"{candidato}: {total_votos} voto(s)")





votos = ["Candidato A", "Candidato B", "Candidato A", "Candidato C", "Candidato A", "Candidato B"]
contagem_votos = {}

for candidato in votos:
    contagem_votos[candidato] = contagem_votos.get(candidato, 0) + 1

print("\n--- Resultado da Votação (versão curta) ---")
for candidato, total_votos in contagem_votos.items():
    print(f"{candidato}: {total_votos} voto(s)")