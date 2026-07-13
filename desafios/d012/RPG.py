import random
from rich import print
from abc import ABC, abstractmethod


class Personagem(ABC):
    def __init__(self, nome, vida, ca):
        self.nome = nome
        self.vida = vida
        self.ca = ca
        self.morto = False
        self.golpes = []

    def atacar(self, alvo, poder):
        if alvo.morto == True:
            print(f"O alvo {alvo} está [red]MORTO[/]! [blue]*Não foi possível atacar o alvo*[/]")
        else:
            dado = random.randint(1, 20)
            if dado > alvo.ca:
                golpe = self.golpes[random.randrange(0, len(self.golpes))]
                print(f"[purple]{self.nome}[/] atacou [red]{alvo.nome}[/] com [green]{golpe}[/].")
                dano = alvo.receber_dano(poder)
                print(f"[red]{alvo.nome}[/] ficou com [green]{dano}[/] pontos de vida.")
            else:
                print(f"[purple]{self.nome}[/] errou o ataque em [red]{alvo.nome}[/].")

    def receber_dano(self, dano):
        fator = random.randint(1, dano)
        self.vida = self.vida - fator
        if self.vida <= 0:
            Personagem.morto = True
        return self.vida

    @abstractmethod
    def curar(self):
        pass


class Guerreiro(Personagem):
    def __init__(self, nome, vida, ca):
        super().__init__(nome, vida, ca)
        self.golpes = ["Golpe de machado", "Tremor", "Ataque aéreo", "Golpe giratório"]

    def curar(self):
        if self.morto == False:
            fator = random.randint(1, 6)
            self.vida = self.vida + fator
            if self.vida > 20:
                self.vida = 20
            print(f"[purple]{self.nome}[/] usou ataduras para fazer um curativo e ficou com [green]{self.vida}[/] pontos de vida.")
        else:
            print(f"[purple]{self.nome}[/] não pode ser curado pois está [red]MORTO[red]!")


class Mago(Personagem):
    def __init__(self, nome, vida, ca):
        super().__init__(nome, vida, ca)
        self.golpes = ["Bola de fogo", "Nevasca", "Orbe de gelo", "Relâmpago"]

    def curar(self):
        if self.morto == False:
            fator = random.randint(1, 6)
            self.vida = self.vida + fator
            if self.vida > 20:
                self.vida = 20
        else:
            print(f"[purple]{self.nome}[/] não pode ser curado pois está [red]MORTO[red]!")

