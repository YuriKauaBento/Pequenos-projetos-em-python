from rich import print
from rich import inspect


class Funcionario:
    #Atributos de classe
    empresa = 'Nova Distribuidora'

    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
    
    def apresentar(self):
        return f':handshake: Olá, meu nome é [blue]{self.nome}[/] sou {self.cargo} do setor de {self.setor} da empresa [bold]{self.__class__.empresa}[/]'


f1 = Funcionario('Yuri', 'Controle de qualidade', 'Garantista')
#inspect(f1)
print(f1.apresentar())

f2 = Funcionario('Stephany', 'atendimento', 'caixa')
print(f2.apresentar())