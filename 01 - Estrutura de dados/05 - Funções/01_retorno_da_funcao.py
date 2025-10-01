def calcular_total(numeros):
    return sum(numeros)


def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor

# def analisar_numero(numero):
#     antecessor = numero - 1
#     sucessor = numero + 1
#     print(f"Analisando o número {numero}: seu antecessor é {antecessor} e seu sucessor é {sucessor}.")
    
def analisar_numero(numero):
    # Aqui está a mágica: chamamos a primeira função
    # e desempacotamos o resultado (a tupla) em duas variáveis.
    antecessor, sucessor = retorna_antecessor_e_sucessor(numero)

    # Agora a função se preocupa apenas em exibir os dados.
    print(f"Analisando o número {numero}: seu antecessor é {antecessor} e seu sucessor é {sucessor}.")

print(calcular_total([10, 20, 34]))  # 64
print(retorna_antecessor_e_sucessor(10))  # (9, 11)
analisar_numero(10)
