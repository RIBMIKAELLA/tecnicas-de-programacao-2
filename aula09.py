from abc import ABC, abstractmethod

# Componente 
class Bebida(ABC):
    @abstractmethod
    def custo(self): # são para definir um método abstrato que vai se chamar custo, dentro da classe abstrata ABC
         pass

    @abstractmethod
    def descricao(self):
         pass


# Componente Concreto
class CafeSimples(Bebida):
    def custo(self):
        return 5.0 # a implementação concreta do método abstrato definido na parte inicial do código acima

    def descricao(self):
        return "Café Simples"


# Decorator 
class DecoradorBedida(Bebida):
    def __init__(self, bebida):
        self._bebida = bebida # Serve para armazenar a instância do objeto que estamos "decorando"


# Decoradores Concretos
class Leite(DecoradorBebida):
    def custo(self):
        return self._bebida.custo() + 2.0

    def descricao(self):
        return self._bebida.descricao() + ", Leite"


class Chocolate(DecoradorBebida):
    def custo(self):
        return self._bebida.custo() + 3.0

    def descricao(self):
        return self._bebida.descricao() + ",Chocolate"


# Utilização 
bebida = CafeSimples()
bebida = Leite(bebida)
bebida = Chocolate(bebida)

print("Descrição:", bebida.descricao())
print("Custo: R$", bebida.custo())

