from abc import ABC, abstractmethod

class BebidaQuente(ABC):
    def __init__(self):
        self.inicio = "Iniciando preparo"
        self.fim = "Bebida Pronta"
        
    def preparar(self):
        preparo = f"""{self.inicio.center(50, "-")}
{self.ferver_agua()}
{self.misturar()}
{self.servir()}
{self.fim.center(50, "-")}"""
        return preparo

    def ferver_agua(self):
        return "1. Fervendo água à 100 graus Célsius."

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass


class Cafe(BebidaQuente):
    def misturar(self):
        return "2. Passando água pressurizada pelo pó de café moído."

    def servir(self):
        return "3. Servindo em xícara pequena."
    

class Cha(BebidaQuente):
    def misturar(self):
        return "2. Mergulhando o sachê de ervas na água."
    
    def servir(self):
        return "3. Servindo na caneca de porcelana com limão."
    

class Leite(BebidaQuente):
    def misturar(self):
        return "2. Passando vapor pressurizado pelo bico do leite."
    
    def servir(self):
        return "3. Servindo na caneca grande, já com café."