from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f'{self.nome}: R$ {self.preco:.2f}'
    
    def etiqueta(self):
        conteudo = self.nome.center(30, '-')
        precof = f'R$ {self.preco:.2f}'
        conteudo += f'{precof.center(30, '.')}'
        etiqueta = Panel(conteudo, title="Produto", width=34)
        return etiqueta

p1 = Produto('faca', 59.90)
print(p1)
print(p1.etiqueta())