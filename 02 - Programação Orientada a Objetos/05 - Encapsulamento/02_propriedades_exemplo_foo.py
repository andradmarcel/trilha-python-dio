class Foo:
    def __init__(self, x=None):
        # Atributo protegido (convenção _).
        self._x = x

    # @property transforma um método em uma "propriedade" de leitura.
    # Isso permite acessar o valor como se fosse um atributo (foo.x) ao invés de método (foo.x()).
    @property
    def x(self):
        # Lógica personalizada no acesso: se _x for None ou falso, retorna 0.
        return self._x or 0

    # @x.setter define o que acontece quando tentamos atribuir um valor a foo.x (foo.x = valor).
    # O nome do método deve ser o mesmo da propriedade.
    @x.setter
    def x(self, value):
        # Aqui podemos adicionar validação ou lógica extra.
        # Neste exemplo específico, o setter está INCREMENTANDO o valor ao invés de substituir.
        # Isso é um comportamento incomum, mas mostra o poder de controlar a atribuição.
        self._x += value

    # @x.deleter define o que acontece quando usamos "del foo.x".
    @x.deleter
    def x(self):
        # Ao invés de apagar o atributo do objeto, aqui estamos apenas zerando o valor.
        self._x = 0


# --- EXEMPLO DE USO ---

foo = Foo(10)

# Acessando a propriedade (chama o método decorado com @property)
print(foo.x)  # Imprime 10

# Deletando a propriedade (chama o método decorado com @x.deleter)
del foo.x
print(foo.x)  # Imprime 0 (pois o deleter zerou o _x)

# Atribuindo valor à propriedade (chama o método decorado com @x.setter)
foo.x = 10
print(foo.x)  # Imprime 10 (0 + 10)

# Observe o comportamento curioso do setter definido acima:
foo.x = 5
print(foo.x)  # Imprime 15 (10 + 5), pois o setter faz += e não =
