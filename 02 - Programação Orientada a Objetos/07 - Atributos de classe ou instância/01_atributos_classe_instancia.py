class Estudante:
    # ATRIBUTO DE CLASSE:
    # Esta variável é definida diretamente no corpo da classe, fora de qualquer método.
    # Ela pertence à CLASSE Estudante, e não a um objeto específico.
    # Isso significa que TODOS os estudantes compartilham a mesma "escola".
    # Se mudarmos esse valor na classe, ele muda para todos (a menos que seja sobrescrito na instância).
    escola = "DIO"

    def __init__(self, nome, matricula):
        # ATRIBUTOS DE INSTÂNCIA:
        # Estas variáveis são definidas usando 'self'.
        # Elas pertencem a CADA OBJETO (instância) individualmente.
        # Cada estudante tem seu próprio nome e sua própria matrícula.
        # Alterar o nome de um estudante NÃO afeta os outros.
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"


def mostrar_valores(*objs):
    for obj in objs:
        print(obj)


# --- EXEMPLO PRÁTICO ---

# Criando dois objetos (instâncias) da classe Estudante.
# Cada um tem seus próprios dados (nome e matrícula), mas compartilham a escola "DIO".
aluno_1 = Estudante("Guilherme", 1)
aluno_2 = Estudante("Giovanna", 2)

print("--- Antes da mudança da escola ---")
mostrar_valores(aluno_1, aluno_2)

# MODIFICANDO O ATRIBUTO DE CLASSE:
# Aqui estamos acessando a classe Estudante diretamente e mudando o valor de 'escola'.
# Como 'escola' é um atributo compartilhado, essa mudança afeta IMEDIATAMENTE
# todas as instâncias que não tenham sobrescrito esse valor.
Estudante.escola = "Python"

# Criando um novo aluno após a mudança.
aluno_3 = Estudante("Chappie", 3)

print("\n--- Depois da mudança da escola (afeta todos) ---")
# Perceba que aluno_1 e aluno_2 AGORA mostram "Python" como escola,
# mesmo tendo sido criados antes da mudança. Isso prova que eles leem o valor da classe.
mostrar_valores(aluno_1, aluno_2, aluno_3)

# CURIOSIDADE (Shadowing):
# Se fizéssemos aluno_1.escola = "Outra", criaríamos um atributo de INSTÂNCIA
# chamado 'escola' apenas para o aluno_1. Ele deixaria de ler o valor da classe.
# Mas enquanto não fizermos isso, ele continua lendo o valor compartilhado.
