from rich import print
from rich.panel import Panel
from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, bruto, salario):
        self.nome = nome
        self.sal_bruto = bruto
        self.salario = salario
        self.sal_min = 1612
        self.inss = 7.5

    @abstractmethod
    def calcular_sal(self):
        pass

    def analisar_sal(self):
        minimos = self.salario / self.sal_min
        conteudo = f"O salário de [blue]{self.nome}[/] ([pink]{type(self).__name__}[/]) é de "
        conteudo += f"[green]R${self.salario:.2f}[/] e corresponde a [yellow]{minimos:.1f} salarios mínimos.[/]"
        painel = Panel(conteudo, title="Análise de Salário", width=50)
        return painel
    

class Horista(Funcionario):
    def __init__(self, nome, valor_hora, horas, bruto=0, salario=0):
        super().__init__(nome, bruto, salario)
        self.nome = nome
        self.bruto = bruto
        self.salario = salario
        self.valor = valor_hora
        self.horas = horas

    def calcular_sal(self):
        self.bruto = self.valor * self.horas
        desc = self.bruto * (self.inss / 100)
        self.salario = self.bruto - desc
        return self.salario
    

class Mensalista(Funcionario):
    def __init__(self, nome, bruto, salario=0):
        super().__init__(nome, bruto, salario)
        self.nome = nome
        self.bruto = bruto
        self.salario = salario

    def calcular_sal(self):
        desc = self.bruto * (self.inss / 100)
        self.salario = self.bruto - desc
        return self.salario

