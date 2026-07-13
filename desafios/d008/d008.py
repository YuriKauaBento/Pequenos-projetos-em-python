from abc import ABC, abstractmethod

class Poligono(ABC):
    def __init__(self, lado=0):
        self.comp = lado
    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Quadrado(Poligono):
    def __init__(self, lado=1):
        super().__init__(4)
        self.comp = lado

    def perimetro(self):
        per = self.comp * 4
        return per
    
    def area(self):
        ar = self.comp ** 2
        return ar
    

class Circulo(Poligono):
    def __init__(self, raio):
        self.pi = 3
        self.raio = raio

    def perimetro(self):
        per = 2 * self.pi * self.raio
        return per
    
    def area(self):
        ar = self.pi * self.raio ** 2
        return ar

p1 = Quadrado(5)
print(f"Perimetro = {p1.perimetro()}")
print(f"Area = {p1.area()}")

p2 = Circulo(5)
print(f"Perimetro = {p2.perimetro()}")
print(f"Area = {p2.area()}")