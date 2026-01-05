from abc import ABC, abstractmethod, abstractproperty


# Uma classe abstrata não pode ser instanciada diretamente.
# Ela serve como um "molde" ou "contrato" para as classes filhas.
# Para definir uma classe abstrata em Python, herdamos de 'ABC' (Abstract Base Class).
class ControleRemoto(ABC):
    
    # Um método abstrato define uma assinatura que TODAS as classes filhas DEVEM implementar.
    # Se uma classe filha não implementar todos os métodos abstratos, ela também será considerada abstrata e não poderá ser instanciada.
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    # Propriedades também podem ser abstratas, forçando as classes filhas a implementarem o getter correspondente.
    @property
    @abstractproperty
    def marca(self):
        pass


# Classe filha que implementa o "contrato" da classe abstrata ControleRemoto
class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV...")
        print("Ligada!")

    def desligar(self):
        print("Desligando a TV...")
        print("Desligada!")

    @property
    def marca(self):
        return "Philco"


# Outra classe filha que implementa o mesmo contrato, mas com comportamentos específicos
class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o Ar Condicionado...")
        print("Ligado!")

    def desligar(self):
        print("Desligando o Ar Condicionado...")
        print("Desligado!")

    @property
    def marca(self):
        return "LG"


# Exemplo de uso:
# Note que podemos tratar diferentes objetos (TV e Ar Condicionado) de forma genérica
# porque sabemos que ambos respeitam o contrato de 'ControleRemoto'.

controle = ControleTV()
controle.ligar()
controle.desligar()
print(f"Marca da TV: {controle.marca}\n")


controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(f"Marca do Ar Condicionado: {controle.marca}")

