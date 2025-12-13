class Ventilador:
    def __init__(self, marca, cor, voltagem):
        # Estamos definindo as características do objeto
        self.marca = marca
        self.cor = cor
        self.voltagem = voltagem
        self.velocidade = 0 # Atributo que não veio no argumento, mas inicia padrão

    def ligar(self):
        # Altera o estado do objeto
        if self.velocidade == 0:
            self.velocidade = 1
            print("Ventilador ligado na velocidade 1.")
        else:
            print("O ventilador já está ligado!")

    def desligar(self):
        self.velocidade = 0
        print("Parando as hélices... Ventilador desligado.")

    def aumentar_velocidade(self):
        # Uma lógica simples para simular mudança de estado
        if self.velocidade > 0 and self.velocidade < 3:
            self.velocidade += 1
            print(f"Aumentando velocidade para {self.velocidade}. Vuuuoshhh!")
        elif self.velocidade == 0:
            print("Você precisa ligar o ventilador primeiro!")
        else:
            print("Já está na velocidade máxima!")

    # Este método é idêntico ao do seu arquivo original
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

# --- Área de Testes (Instanciando os Objetos) ---

# Criando o objeto v1 (o produto saindo da fábrica)
v1 = Ventilador("Arno", "Preto", 220)

# Mostrando o estado inicial (usando o __str__)
print(v1)

# Realizando ações
v1.ligar()
v1.aumentar_velocidade()
v1.desligar()

# Mostrando o estado final
print(v1)