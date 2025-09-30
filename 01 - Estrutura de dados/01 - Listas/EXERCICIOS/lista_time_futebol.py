



jogadores = ["Neymar", "Vinícius Jr", "Alisson", "Casemiro", "Marquinhos", "Thiago Silva", "Paquetá", "Richarlison"]

# Sua lógica, que já estava perfeita
jogadores_ordenados = sorted(jogadores)
titulares = jogadores_ordenados[:5]
reservas = jogadores_ordenados[5:]

# Apenas uma forma mais organizada de apresentar os resultados
print("--- CONVOCAÇÃO OFICIAL ---")
print(f"\nLista de Observação Original: {jogadores}")

print("\nTime Titular (5 convocados):")
for titular in titulares:
    print(f"- {titular}")

print("\nBanco de Reservas:")
for reserva in reservas:
    print(f"- {reserva}")

print("\n--- Convocação finalizada! ---")