carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")


def iterar_set(conjunto):
    for i in conjunto:
        print(i)
    
    
iterar_set(carros) 
    