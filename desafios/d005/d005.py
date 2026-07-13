from rich.panel import Panel
from rich import print

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favs = []

    def add_favoritos(self, jogo):
        self.favs.append(jogo)
        self.favs = sorted(self.favs, key=str.lower)

    def ficha(self):
        conteudo = f'Nome real: [black on blue]{self.nome}[/]'
        conteudo += f"\nJogos favoritos:"
        for num, game in enumerate(self.favs):
            conteudo += f"\n:video_game: [blue]{game}[/]"
        painel = Panel(conteudo, title=f"Jogador <{self.nick}>", width=40)
        print(painel)

g1 = Gamer('Yuri', 'Yruka',)
g1.add_favoritos('Baldurs Gate 3')
g1.add_favoritos('God of War')
g1.add_favoritos('Cyberpunk 2077')
g1.ficha()

g2 = Gamer('Luan', 'Lili')
g2.add_favoritos('League of Legends')
g2.add_favoritos('Stardew Valley')
g2.ficha()