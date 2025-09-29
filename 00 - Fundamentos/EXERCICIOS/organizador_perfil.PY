


nome_str = input("Digite seu nome: ")
idade_str = input("Digite sua idade: ")
altura_str = input("Digite sua altura: ")
gosta_programar_str = input ("Voce gosta de programar? ")

idade = int(idade_str)
altura = float(altura_str.replace(",", "."))
gosta_programar_formatada = gosta_programar_str.lower().strip()

if gosta_programar_formatada == "sim" or "s":
    gosta_programar = True
else:
    gosta_programar = False
    
print(f"Perfil de {nome_str.title()}: {idade} anos, {altura:.2f}m de altura. Gosta de programar? {gosta_programar}")