from rich import print

class Caneta:
    def __init__(self, cor):
        escolha = ""
        match cor.lower().strip():
            case "azul":
                escolha = "[blue]"
            case "vermelho" | "vermelha":
                escolha = "[red]"
            case "verde":
                escolha ="[green]"
            case _:
                escolha = "[white]"
        self.cor = escolha
        self.tampa = True

    def destampar(self):
        self.tampa = False
        return self.tampa
    
    def tampar(self):
        self.tampa = True
        return self.tampa
    
    def pular_linha(self, linhas=1):
        print(f'\n' * linhas, end='')

    def escrever(self, frase):
        if self.tampa:
            print(f'A {self.cor}caneta[/] está tampada!')
        elif self.cor == '[white]':
            print(f'A cor {self.cor} está indisponível!')
        else:
            print(f'{self.cor}{frase}[/]', end=' ')

c1 = Caneta('Vermelho')
c2 = Caneta('Verde')
c3 = Caneta('Azul')
c4 = Caneta('preta')
c5 = Caneta('verde')

c1.destampar()
c1.escrever('Mensagem')
c1.pular_linha()

c2.destampar()
c2.escrever('Mensagem')
c2.pular_linha()

c3.destampar()
c3.escrever('Mensagem')
c3.pular_linha(2)

c4.destampar()
c4.escrever('Mensagem')

c5.escrever('Mensagem')
