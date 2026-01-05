class Pessoa:
    def __init__(self, nome, ano_nascimento):
        # Atributo público: pode ser acessado e modificado livremente.
        self.nome = nome
        
        # Atributo protegido: armazena o estado interno (ano de nascimento).
        # O _ indica que não deve ser acessado diretamente.
        self._ano_nascimento = ano_nascimento

    # @property define um método que é acessado como um atributo.
    # Neste caso, 'idade' é uma PROPRIEDADE CALCULADA.
    # Ela não armazena um valor fixo na memória; o valor é calculado
    # toda vez que alguém acessa 'pessoa.idade'.
    @property
    def idade(self):
        _ano_atual = 2022
        return _ano_atual - self._ano_nascimento
    
    # OBSERVAÇÃO IMPORTANTE:
    # Como não definimos um @idade.setter, essa propriedade é SOMENTE LEITURA (Read-Only).
    # Tentar fazer 'pessoa.idade = 30' geraria um erro (AttributeError).
    # Isso é útil para valores que dependem de outros dados (como idade depende do ano de nascimento).


# --- EXEMPLO DE USO ---

pessoa = Pessoa("Guilherme", 1994)

# Acessando a propriedade calculada
# Note que usamos pessoa.idade (sem parênteses), como se fosse uma variável.
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")

# Se tentássemos alterar a idade diretamente, daria erro:
# pessoa.idade = 30  # AttributeError: can't set attribute
