# Classe base (Pai) que define características e comportamentos comuns a todos os veículos
# A ideia da herança é promover o reuso de código. Em vez de repetir cor, placa e rodas
# em cada classe (Carro, Moto, Caminhão), definimos uma vez aqui.
class Veiculo:
    # O método __init__ é o construtor. Ele é chamado automaticamente quando criamos um novo objeto.
    # 'self' é uma referência à instância atual sendo criada.
    def __init__(self, cor, placa, numero_rodas):
        # Atributos de instância: cada objeto terá seus próprios valores para estas variáveis.
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    # Método simples que representa um comportamento do veículo.
    def ligar_motor(self):
        print("Ligando o motor")

    # Método especial (dunder method) para retornar uma representação em string legível do objeto.
    # Sem isso, ao dar print(objeto), veríamos algo como <__main__.Veiculo object at 0x...>.
    def __str__(self):
        # self.__class__.__name__: Pega o nome da classe (ex: "Carro", "Motocicleta").
        # self.__dict__: Retorna um dicionário com todos os atributos do objeto (ex: {'cor': 'preta', ...}).
        # A list comprehension cria strings "chave=valor" e o join as une com vírgulas.
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


# Herança Simples: Motocicleta herda tudo de Veiculo (atributos e métodos).
# A sintaxe class Filha(Pai) estabelece a relação de herança.
class Motocicleta(Veiculo):
    # A palavra-chave 'pass' indica que a classe não tem implementação adicional por enquanto.
    # Ela é apenas uma cópia especializada de Veiculo, mas sem mudanças de comportamento.
    pass


# Carro também herda de Veiculo sem adicionar novos métodos ou atributos.
# Isso permite tratar Carro como um tipo específico, mesmo que o código seja igual ao Pai.
class Carro(Veiculo):
    pass


# Caminhao herda de Veiculo, mas personaliza a inicialização e adiciona um novo método
class Caminhao(Veiculo):
    # Sobrescrita de método (Overriding): Estamos redefinindo o __init__ da classe pai.
    # O Caminhão precisa de um atributo extra: 'carregado'.
    def __init__(self, cor, placa, numero_rodas, carregado):
        # super() retorna um objeto temporário da superclasse (Veiculo), permitindo chamar seus métodos.
        # Aqui chamamos o __init__ do Veiculo para configurar cor, placa e rodas, evitando reescrever código.
        super().__init__(cor, placa, numero_rodas)
        # Definimos o atributo específico desta classe.
        self.carregado = carregado

    # Novo método que existe apenas em Caminhao, não em Veiculo, Carro ou Motocicleta.
    def esta_carregado(self):
        # Uso de operador ternário para imprimir 'Sim' ou 'Não' baseado no booleano self.carregado.
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")


# Instanciando os objetos.
# Note que Motocicleta e Carro usam o construtor (__init__) herdado de Veiculo.
moto = Motocicleta("preta", "abc-1234", 2)
carro = Carro("branco", "xde-0098", 4)

# Caminhao usa seu próprio construtor, que pede 4 argumentos.
caminhao = Caminhao("roxo", "gfd-8712", 8, True)

print(moto)
print(carro)
print(caminhao)
