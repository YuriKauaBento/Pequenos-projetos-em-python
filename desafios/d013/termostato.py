class Termostato:
    def __init__(self):
        self.__temp = 24

    @property
    def temp(self):
        return self.__temp

    @temp.setter
    def temp(self, valor):
        if valor < 16:
            self.__temp = 16
        if valor > 30:
            self.__temp = 30
        elif valor % 0.5 != 0:
            raise ValueError(f"Temperatura de {valor}°C é inválida!")
        else:
            self.__temp = valor

    @property
    def ftemp(self):
        return f"{self.__temp}°C"