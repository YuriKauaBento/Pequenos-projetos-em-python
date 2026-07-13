from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, distancia):
        self.dist = distancia
        self.frete = 0

    @abstractmethod
    def calcular_frete(self):
        pass


class Moto(Transporte):
    fator = 0.5
    def __init__(self, distancia):
        super().__init__(distancia)

    def calcular_frete(self) -> float:
        self.frete = self.dist * Moto.fator
        return f"R${self.frete:.2f}"
    
class Caminhao(Transporte):
    fator = 1.2
    def __init__(self, distancia):
        super().__init__(distancia)

    def calcular_frete(self):
        if self.dist < 50:
            return "Distância mínima de 50Km para este serviço!"
        else:
            self.frete = self.dist * Caminhao.fator
            return f"R${self.frete:.2f}"

    
class Drone(Transporte):
    fator = 9.5
    def __init__(self, distancia):
        super().__init__(distancia)

    def calcular_frete(self):
        if self.dist > 10:
            return "Distância máxima de 10Km para esse serviço!"
        else:
            self.frete = self.dist * Drone.fator
            return f"R${self.frete:.2f}"