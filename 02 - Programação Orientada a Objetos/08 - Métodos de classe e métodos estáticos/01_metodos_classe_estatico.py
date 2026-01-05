class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Um método de classe recebe a própria classe (cls) como primeiro argumento, em vez da instância (self).
    # É comumente usado para criar "métodos de fábrica" (factory methods), que retornam uma nova instância da classe
    # configurada de uma maneira específica.
    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        # Aqui usamos a lógica para calcular a idade a partir do ano de nascimento
        idade = 2022 - ano
        # Retornamos uma nova instância da classe chamando 'cls(nome, idade)'
        return cls(nome, idade)

    # Um método estático não recebe nem a classe (cls) nem a instância (self) como argumento.
    # Ele se comporta como uma função normal, mas reside dentro do namespace da classe.
    # É útil para funções utilitárias que têm alguma relação lógica com a classe, mas não precisam
    # acessar atributos da classe ou da instância.
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18


# Criando uma instância usando o método de fábrica (classmethod)
p = Pessoa.criar_de_data_nascimento(1994, 3, 21, "Guilherme")
print(f"Nome: {p.nome}, Idade: {p.idade}")

# Chamando o método estático diretamente pela classe
# Note que não precisamos de uma instância para chamar um método estático ou de classe
print(f"É maior de idade? {Pessoa.e_maior_idade(18)}")
print(f"É maior de idade? {Pessoa.e_maior_idade(8)}")

