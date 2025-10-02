


def saudacao(nome, titulo= "Sr(a)."):
    mensagem = f"Olá, {titulo} {nome}"
    return mensagem




usario = input("Digite seu nome: ")

print(saudacao(usario.title()))