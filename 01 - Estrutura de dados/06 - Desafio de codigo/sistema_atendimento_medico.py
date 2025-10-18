def prioridade_paciente(lista_pacientes):
    # Suas variáveis para os grupos de triagem
    urgente = []
    idosos = []
    normal = []
    
    # 1. FAZENDO A TRIAGEM SIMPLES
    # Este laço separa os pacientes nos três grupos corretos.
    for paciente in lista_pacientes:
        if paciente[2] == "urgente":
            urgente.append(paciente)
        elif paciente[1] >= 60:
            idosos.append(paciente)
        else:
            normal.append(paciente)
            
    # 2. A CORREÇÃO PRINCIPAL: A REGRA DE DESEMPATE
    #    Agora que temos todos os pacientes urgentes, ordenamos essa lista específica.
    #    - key=lambda p: p[1] diz para usar a idade (índice 1) como critério.
    #    - reverse=True ordena do maior para o menor (mais velho primeiro).
    urgente.sort(key=lambda p: p[1], reverse=True)
    
    # Agora o resto do seu código já funciona perfeitamente!
    fila_final = urgente + idosos + normal
    nomes_ordenados = [paciente[0] for paciente in fila_final]      
    
    return nomes_ordenados


# --- CÓDIGO PRINCIPAL ---

# Entrada do número de pacientes
n = int(input().strip())

# Lista para armazenar pacientes
pacientes = []

# Loop para entrada de dados (com uma pequena melhoria para robustez)
for _ in range(n):
    # Usar map(str.strip, ...) limpa os espaços de todas as partes de uma vez
    nome, idade_str, status = map(str.strip, input().strip().split(","))
    idade = int(idade_str)
    pacientes.append((nome, idade, status))


# TODO: Ordene por prioridade: urgente > idosos > demais:
# Chamamos sua função corrigida para obter a lista de nomes na ordem certa.
ordem_atendimento = prioridade_paciente(pacientes)

# TODO: Exiba a ordem de atendimento com título e vírgulas:
# A sua linha de exibição já estava perfeita.
print(f"Ordem de Atendimento: {', '.join(ordem_atendimento)}")