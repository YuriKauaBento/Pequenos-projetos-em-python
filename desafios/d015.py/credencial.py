from hashlib import sha256
from rich import print


class Credencial():
    def __init__(self):
        self.__hash = None

    @property
    def senha(self):
        return self.__hash
    
    @senha.setter
    def senha(self, chave):
        if len(chave) > 0:
            self.__hash = sha256(chave.encode('utf-8')).hexdigest()
        else:
            raise ValueError("Senha inválida!")
        
    def validar(self, chave):
        usuario = sha256(chave.encode('utf-8')).hexdigest()
        if usuario == self.__hash:
            print("[green]Senha correta![/]")
            return True
        else:
            print("[red]Senha incorreta![/]")
            return False
    