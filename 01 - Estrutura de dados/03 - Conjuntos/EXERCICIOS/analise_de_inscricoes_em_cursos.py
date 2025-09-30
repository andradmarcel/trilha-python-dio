alunos_python = {101, 102, 103, 104, 105}
alunos_java = {103, 104, 106, 107, 108}

print("--- Análise de Inscrições em Cursos ---")

# ===================================================================
# 1. Alunos que estão matriculados em Python, mas NÃO em Java
# ===================================================================
print("\n--> Relatório: Alunos exclusivos do curso de Python")

# Usando o método .difference()
apenas_python_metodo = alunos_python.difference(alunos_java)
print(f"Com método: {apenas_python_metodo}")

# Usando o operador de diferença '-'
apenas_python_operador = alunos_python - alunos_java
print(f"Com operador '-': {apenas_python_operador}")


# ===================================================================
# 2. Alunos que estão matriculados em Java, mas NÃO em Python
# ===================================================================
print("\n--> Relatório: Alunos exclusivos do curso de Java")

# Usando o método .difference()
apenas_java_metodo = alunos_java.difference(alunos_python)
print(f"Com método: {apenas_java_metodo}")

# Usando o operador de diferença '-'
apenas_java_operador = alunos_java - alunos_python
print(f"Com operador '-': {apenas_java_operador}")


# ===================================================================
# 3. Alunos que estão em APENAS UM dos cursos (não em ambos)
# ===================================================================
print("\n--> Relatório: Alunos em apenas um dos dois cursos")

# Usando o método .symmetric_difference()
alunos_exclusivos_metodo = alunos_python.symmetric_difference(alunos_java)
print(f"Com método: {alunos_exclusivos_metodo}")

# Usando o operador de diferença simétrica '^' (XOR)
alunos_exclusivos_operador = alunos_python ^ alunos_java
print(f"Com operador '^': {alunos_exclusivos_operador}")