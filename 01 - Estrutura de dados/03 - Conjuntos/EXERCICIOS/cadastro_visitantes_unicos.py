registros_entrada = ["Ana", "Carlos", "Beatriz", "Ana", "Daniel", "Carlos", "Fernanda", "Ana"]

registros_unicos = set(registros_entrada)

print("--- Relatório do Evento ---")
print(f"Lista original de entradas: {registros_entrada}")
print(f"\nVisitantes únicos que compareceram: {registros_unicos}")
print(f"Total de visitantes únicos: {len(registros_unicos)}")