# Classe base (ou superclasse) que define um conceito genérico de Animal.
# É o topo da nossa hierarquia de classes.
class Animal:
    def __init__(self, nro_patas):
        print("Inicializador de Animal chamado")
        self.nro_patas = nro_patas

    # Método __str__ para uma representação legível do objeto.
    def __str__(self):
        # Este método é herdado por todas as subclasses e funcionará nelas também.
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


# Classe que herda de Animal, especializando-o como Mamifero.
class Mamifero(Animal):
    # O uso de **kw (keyword arguments) é uma técnica fundamental para herança cooperativa.
    # Ele age como um "coletor" de argumentos nomeados que não são explicitamente definidos
    # neste método (neste caso, 'cor_pelo').
    def __init__(self, cor_pelo, **kw):
        print("Inicializador de Mamifero chamado")
        self.cor_pelo = cor_pelo
        # A chamada a super() aqui é crucial. Ela não chama necessariamente o __init__ de Animal.
        # Ela chama o __init__ da PRÓXIMA classe na "Method Resolution Order" (MRO).
        # **kw desempacota o dicionário de argumentos coletados, passando-os para o próximo construtor.
        # Isso permite que a cadeia de inicialização continue de forma flexível.
        super().__init__(**kw)


# Classe que também herda de Animal, especializando-o como Ave.
class Ave(Animal):
    # A lógica é idêntica à de Mamifero, mas para o atributo 'cor_bico'.
    def __init__(self, cor_bico, **kw):
        print("Inicializador de Ave chamado")
        self.cor_bico = cor_bico
        super().__init__(**kw)


# Gato herda apenas de Mamifero (Herança Simples).
class Gato(Mamifero):
    # Como não há um método __init__ definido aqui, o Python procurará na hierarquia (MRO).
    # O primeiro __init__ que ele encontrar será o de Mamifero, que será executado.
    pass


# Herança Múltipla: Ornitorrinco herda de Mamifero E de Ave.
# Isso cria o clássico "Problema do Diamante": Ornitorrinco herda de Mamifero e Ave,
# e ambos herdam de Animal. Como garantir que o construtor de Animal seja chamado
# de forma correta e apenas uma vez?
#
# A resposta do Python é o MRO (Method Resolution Order). Ele cria uma lista linearizada
# e previsível de classes para procurar métodos. A ordem em que as classes são listadas
# na herança (Mamifero, Ave) é FUNDAMENTAL para definir o MRO.
#
# Para ver o MRO: print(Ornitorrinco.mro())
# MRO para Ornitorrinco: [Ornitorrinco, Mamifero, Ave, Animal, object]
class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_bico, cor_pelo, nro_patas):
        print("Inicializador de Ornitorrinco chamado")
        # Esta única chamada a super().__init__ inicia uma cadeia de chamadas cooperativas
        # que segue o MRO. Todos os argumentos necessários são passados de uma vez.
        #
        # O FLUXO DE EXECUÇÃO SERÁ:
        # 1. Ornitorrinco.__init__ chama super().__init__(...), que aponta para Mamifero.__init__.
        # 2. Mamifero.__init__ é executado. Ele pega 'cor_pelo' e usa. O resto ('cor_bico', 'nro_patas')
        #    é capturado por **kw e passado para o seu super().__init__(**kw).
        # 3. O super() de Mamifero aponta para a PRÓXIMA classe no MRO, que é Ave.
        # 4. Ave.__init__ é executado. Ele pega 'cor_bico' e usa. O resto ('nro_patas') é
        #    capturado por **kw e passado para o seu super().__init__(**kw).
        # 5. O super() de Ave aponta para a PRÓXIMA classe no MRO, que é Animal.
        # 6. Animal.__init__ é executado. Ele pega 'nro_patas' e usa. A cadeia termina aqui.
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, nro_patas=nro_patas)


print("--- Criando Gato ---")
# Ao criar um Gato, o __init__ de Mamifero é chamado. 'cor_pelo' é usado por ele,
# e 'nro_patas' é passado para o __init__ de Animal via **kw e super().
gato = Gato(nro_patas=4, cor_pelo="Preto")
print(gato)

print("\n--- Criando Ornitorrinco ---")
# Ao criar um Ornitorrinco, seu __init__ é chamado, que por sua vez invoca a cadeia
# de inicialização completa (Mamifero -> Ave -> Animal) de forma organizada.
ornitorrinco = Ornitorrinco(nro_patas=2, cor_pelo="vermelho", cor_bico="laranja")
print(ornitorrinco)
