

texto = "o python é uma linguagem de programação poderosa e versátil o python é ótimo para iniciantes"

texto_fatiado = texto.split(" ")

frequencia = {}


for palavra in texto_fatiado:
    frequencia[palavra] = frequencia.get(palavra, 0) + 1

for palavra, total_palavras in frequencia.items():
    print(f"{palavra}: {total_palavras}")

    
