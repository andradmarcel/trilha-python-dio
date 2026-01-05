class Passaro:
    def voar(self):
        print("Voando...")


# HERANÇA E POLIMORFISMO:
# Aqui criamos classes que HERDAM de Passaro.
# Isso significa que elas "são" Pássaros e ganham suas características.
class Pardal(Passaro):
    def voar(self):
        # SOBRESCRITA DE MÉTODO (Overriding):
        # O Pardal tem um jeito específico de voar.
        # Ao redefinir o método voar() aqui, substituímos o comportamento padrão da classe pai (Passaro).
        print("Pardal pode voar")


class Avestruz(Passaro):
    def voar(self):
        # O Avestruz também é um Pássaro, mas ele NÃO voa.
        # O polimorfismo nos permite lidar com essa diferença de comportamento
        # mantendo o mesmo nome do método (voar).
        print("Avestruz não pode voar")


# NOTE: Exemplo ruim do uso de herança para "ganhar" o método voar.
# Por que é ruim? Porque semanticamente, um Avião NÃO É um Pássaro.
# Em POO, herança deve indicar uma relação "É UM" (Is-A).
# Se você só quer o comportamento (voar), seria melhor usar interfaces ou mixins, não herança direta.
class Aviao(Passaro):
    def voar(self):
        print("Avião está decolando...")


# FUNÇÃO POLIMÓRFICA:
# Esta função demonstra o poder do Polimorfismo.
# Observe que o parâmetro se chama 'obj'. A função NÃO sabe se vai receber um Pardal,
# um Avestruz ou um Avião. E ela NÃO PRECISA saber!
#
# Ela só precisa saber de uma coisa: "O objeto tem um método chamado voar()?"
# Se tiver, ela executa. Isso permite que o mesmo código (obj.voar())
# tenha comportamentos diferentes dependendo de QUEM é o objeto.
def plano_voo(obj):
    obj.voar()


# --- TESTANDO O POLIMORFISMO ---

print("--- Pardal ---")
# Passamos um objeto Pardal. O Python vai executar o voar() da classe Pardal.
plano_voo(Pardal())

print("\n--- Avestruz ---")
# Passamos um objeto Avestruz. O Python vai executar o voar() da classe Avestruz.
# Mesmo método, comportamento diferente.
plano_voo(Avestruz())

print("\n--- Avião ---")
# Passamos um objeto Avião. Funciona porque Avião também tem o método voar().
plano_voo(Aviao())
