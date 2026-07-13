from rich.panel import Panel
from rich import print
from time import sleep

class Controle:
        canal_min = 1
        canal_max = 5
        vol_min = 1
        vol_max = 5

        def __init__(self, canal=1, volume=2):
            self.canal_atual = canal
            self.vol_atual = volume
            self.ligado = False

        def liga_desliga(self):
            self.ligado = not self.ligado

        def canal_mais(self):
            if self.ligado:
                if self.canal_atual == self.canal_max:
                    self.canal_atual = self.canal_min
                else:
                    self.canal_atual += 1
        
        def canal_menos(self):
            if self.ligado:
                if self.canal_atual == self.canal_min:
                    self.canal_atual = self.canal_max
                else:
                    self.canal_atual -= 1
        
        def vol_mais(self):
            if self.ligado:
                if self.vol_atual != self.vol_max:
                    self.vol_atual += 1
                  
        def vol_menos(self):
            if self.ligado:
                if self.vol_atual != self.vol_min:
                    self.vol_atual -= 1

        def mostrar_tv(self):
            conteudo = ""
            if not self.ligado:
                conteudo = "[red]A TV está desligada[/]"
            else:
                conteudo = "CANAL  = "
                for canal in range(self.canal_min, self.canal_max + 1):
                    if canal == self.canal_atual:
                        conteudo += f"[yellow on yellow] {canal} [/]"
                    else:
                        conteudo += f" {canal} "
                conteudo += f"\nVOLUME = "
                for volume in range(self.vol_min, self.vol_max + 1):
                    if volume <= self.vol_atual:
                        conteudo += "[black on cyan] [/]"
                    else:
                        conteudo += "[black on white] [/]"

            painel = Panel(conteudo, title="[ TV ]", width=30)
            print(painel)
    

tv = Controle()
while True:
    tv.mostrar_tv()
    op = str(input(f"< CH{tv.canal_atual} >  - VOL{tv.vol_atual} + "))
    if op == '@':
        tv.liga_desliga()
    elif op == '<':
        tv.canal_menos()
    elif op == '>':
        tv.canal_mais()
    elif op == '-':
        tv.vol_menos()
    elif op == '+':
        tv.vol_mais()
    elif op == '0':
        break
    else:
        print("[red]Opção inválida[/]")
        sleep(1)
