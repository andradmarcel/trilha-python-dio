

temperaturas = []

for dia in range(1,8):
    registro_temperatura = float(input(f"Digite a temperatura do {dia}° dia em Celsius: "))
    temperaturas.append(registro_temperatura)
    print(f"A temperatura de {registro_temperatura}°C foi adicionada!")

media_temperaturas = sum(temperaturas) / len(temperaturas)

print(f"Lista completa de temperaturas: {temperaturas}\nMedia das temperaturas: {media_temperaturas:.2f}")