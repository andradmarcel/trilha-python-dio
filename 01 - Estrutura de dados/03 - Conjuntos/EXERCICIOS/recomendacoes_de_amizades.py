


amigos_ana = {"Bia", "Carlos", "Daniel", "Fernanda"}
amigos_bruno = {"Carlos", "Daniel", "Gustavo", "Helena"}


amigos_em_comum = amigos_ana.intersection(amigos_bruno)
todos_os_amigos = amigos_ana.union(amigos_bruno)

amigos_em_comum_operador = amigos_ana & amigos_bruno
todos_os_amigos_operador = amigos_ana | amigos_bruno

print("--- Análise de Amizades da Rede Social ---")
print(f"\nAmigos em comum (usando .intersection()): {amigos_em_comum}")
print(f"Amigos em comum (usando o operador '&'): {amigos_em_comum_operador}")

print(f"\nTodos os amigos (usando .union()): {todos_os_amigos}")
print(f"Todos os amigos (usando o operador '|'): {todos_os_amigos_operador}")