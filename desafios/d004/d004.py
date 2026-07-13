from time import sleep
from rich import print

class Livro:
    def __init__(self, titulo, paginas):
        self.title = titulo
        self.pag = paginas
        self.pag_atual = 1
        print(f"Você acabou de abrir o livro [blue]'{self.title}'[/] que tem [green]{self.pag} paginas [/]"
              f"e você está na [yellow]{self.pag_atual}[/]")
        
    def avancar(self, qtd=1):
        c = 0
        for i in range(0, qtd, 1):
            if not self.fim():
                self.pag_atual += 1
                print(f'Pag{self.pag_atual} :arrow_forward:' , end='')
                sleep(0.5)
                c +=1
        print(f'Você avançou [blue]{c} páginas[/] e agora está na página [yellow]{self.pag_atual}[/]')
        if self.fim():
            print(f'Você chegou ao final do livro {self.title}')

    def fim(self):
        if self.pag_atual == self.pag:
            return True
        else:
            return False
        

l1 = Livro("Sei la", 20)
l1.avancar(10)
l1.avancar(20)