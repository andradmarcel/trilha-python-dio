



def exibir_perfil(nome, **kwargs):
    print(f"Perfil de {nome}")
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")




exibir_perfil("Marcel", idade=28, profissao= "vendedor")
exibir_perfil("Carlos", cidade="Salvador", time="Bahia")