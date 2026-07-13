from rich import print
from rich.panel import Panel

class Churrasco:
    consumo = 0.4
    preco_kg = 82.40
    def __init__(self, titulo, pessoas):
        self.pessoas = pessoas
        self.title = titulo

    def __str__(self):
        return f'Esse é nosso {self.title} com {self.pessoas} pessoas participando'
    
    def calcular_qtd_carne(self) -> float:
        return self.pessoas * Churrasco.consumo

    def calcular_preco_total(self):
        return self.calcular_qtd_carne() * Churrasco.preco_kg

    def calcular_preco_individual(self):
        return self.calcular_preco_total() / self.pessoas

    def analise(self):
        conteudo = f'Analisando [green]{self.title}[/] com [blue]{self.pessoas}[/]'
        conteudo += f'\nCada participante comerá {Churrasco.consumo:.3f}KG e cada KG custa R$ {Churrasco.preco_kg:.2f}'
        conteudo += f'\nRecomendo [blue]comprar {self.calcular_qtd_carne():.3f}KG[/] de carne'
        conteudo += f'\nO custo total será de [red]R$ {self.calcular_preco_total():.2f}[/]'
        conteudo += f'\nCada pessoa pagará [yellow]R$ {self.calcular_preco_individual():.2f}[/] para participar'
        painel = Panel(conteudo, title=self.title, width=65)
        return painel
    

churrasco = Churrasco('Churrasco a Dois', 7)
print(churrasco)
print(churrasco.analise())
