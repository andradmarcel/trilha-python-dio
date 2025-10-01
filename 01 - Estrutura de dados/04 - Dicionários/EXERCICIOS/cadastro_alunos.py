

alunos = {
    "100": {
        "nome": "marcel",
        "curso": "engenharia",
        "notas": {
            "matematica": 9,
            "programacao": 10,
            "computacao": 8.5
        }
    },
    "101": {
        "nome": "mariana",
        "curso": "engenharia",
        "notas": {
            "matematica": 10,
            "programacao": 8,
            "nuvem": 9.5
        }
    }
}


print(10*"=","Consulta Aluno",10*"=")
while True: 
    try:
        id_aluno = input("Digite o ID do aluno para consulta e 'sair' para fechar o programa: ").lower().strip()
        if id_aluno == "sair":
            print("Encerrando consulta")
            break
        
        if id_aluno in alunos:
            nome = alunos[id_aluno]["nome"]
            curso = alunos[id_aluno]["curso"]
            notas = alunos[id_aluno]["notas"]

            print(f"O aluno '{nome}'".title(),f"esta cursando '{curso}'")
            print(f"Notas do aluno {nome.title()}:")
        
            for materia, nota in notas.items():
                print(f"{materia.title()} nota: {nota:.2f}")
            sim_ou_nao = input(f"Gostaria de adicionar uma nova materia e nota para o aluno(a) {nome.title()} [s/n]: ").lower().strip()
            if sim_ou_nao == "s" or sim_ou_nao == "sim":
                nova_materia = input("Digite a materia: ").lower().strip()
                try:                   
                    nova_nota = float(input("Digite a nota: ").replace(',', '.'))
                    notas[nova_materia] = nova_nota
                    print(f"\nNota de {nova_materia.title()} adicionada com sucesso!")
                    print(f"--- Notas atualizadas de {nome.title()} ---")
                    for materia, nota in notas.items():
                        print(f"{materia.title()} nota: {nota:.2f}")
                except ValueError:
                    print("Erro: A nota digitada não é um número válido. A operação foi cancelada.")
                    
            else:
                print("Ok, voltando ao menu de consulta.")
                
                
                
        else: 
            print("Aluno nao encontrado")
    except ValueError:
        print("Erro inesperado, tente novamente")