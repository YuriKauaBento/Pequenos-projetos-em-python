from rich import print


class Diario:
    def __init__(self, senha="Widoumaker7!"):
        self.__segredos = []
        self.__senha = senha

    def escrever(self, segredo):
        if isinstance(segredo, str) and len(segredo) > 0:
            return self.__segredos.append(segredo.strip())
    
    def ler(self, senha=None):
        if senha == self.__senha:
            print("[green]DIÁRIO LIBERADO![/]")
            for a, b in enumerate(self.__segredos):
                print(f"{a+1} - {b}")
                print()
        else:
            raise PermissionError("Senha inválida!")
        

    @property
    def senha(self):
        raise PermissionError("Ninguém tem permissão para ver a senha.")