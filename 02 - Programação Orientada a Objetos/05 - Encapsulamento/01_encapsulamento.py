class Conta:
    def __init__(self, nro_agencia, saldo=0):
        # ENCAPSULAMENTO:
        # O encapsulamento é um dos pilares da POO. Ele serve para agrupar dados e métodos
        # que operam nesses dados em uma única unidade (a classe) e restringir o acesso
        # direto a alguns componentes do objeto. Isso protege a integridade dos dados.

        # ATRIBUTO PROTEGIDO (_saldo):
        # Em Python, a convenção de usar um único underscore (_) antes do nome do atributo
        # indica que ele é "protegido". Isso é um aviso para outros programadores:
        # "Não acesse ou modifique isso diretamente fora da classe ou de suas subclasses".
        # Diferente de linguagens como Java, o Python não impede o acesso técnico,
        # mas é uma forte convenção da comunidade (PEP 8).
        self._saldo = saldo
        
        # ATRIBUTO PÚBLICO (nro_agencia):
        # Atributos sem underscore inicial são públicos. Eles fazem parte da interface
        # estável da classe e podem ser acessados e modificados livremente por qualquer
        # parte do código que use um objeto Conta.
        self.nro_agencia = nro_agencia

    def depositar(self, valor):
        # MÉTODOS PÚBLICOS COMO INTERFACE:
        # Métodos públicos (sem _) servem como a interface controlada para interagir
        # com os dados protegidos.
        # Vantagem 1: Validação. Poderíamos verificar se valor > 0 antes de somar.
        # Vantagem 2: Abstração. O usuário não precisa saber COMO o saldo é guardado,
        # apenas que ele pode depositar.
        # ...
        self._saldo += valor

    def sacar(self, valor):
        # Aqui também poderíamos ter lógica de validação, como verificar se há
        # saldo suficiente antes de permitir o saque. Ao encapsular o acesso ao
        # _saldo, garantimos que o saldo nunca fique negativo por um acesso direto indevido.
        # ...
        self._saldo -= valor

    def mostrar_saldo(self):
        # ACESSO DE LEITURA (Getter):
        # Este método permite que o mundo externo LEIA o saldo, mas não o altere.
        # Se o atributo _saldo fosse público, qualquer um poderia fazer conta.saldo = -1000.
        # Com esse método, garantimos acesso somente leitura ao valor atual.
        # ...
        return self._saldo


# --- EXEMPLO DE USO ---

# Criando uma instância da classe Conta
conta = Conta("0001", 100)

# Modificando o estado interno (saldo) através de um método público.
# Isso é seguro e segue as regras definidas pela classe.
conta.depositar(100)

# Acessando um atributo público.
# Como nro_agencia é público, não há problema em acessá-lo diretamente.
print(conta.nro_agencia)

# Lendo o saldo através do método público.
# Esta é a forma correta de obter o valor de um atributo protegido.
print(conta.mostrar_saldo())

# NOTA SOBRE ACESSO DIRETO:
# O código abaixo funcionaria tecnicamente:
# print(conta._saldo)
# Mas isso viola o encapsulamento. Se a implementação interna de _saldo mudar
# (ex: virar uma string ou ser calculado na hora), o código que acessa direto quebraria.
# Usando .mostrar_saldo(), a implementação interna pode mudar sem quebrar o código externo.
