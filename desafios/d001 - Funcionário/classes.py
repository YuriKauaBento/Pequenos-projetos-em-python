from rich import print


class Funcionario:
    empresa = "Google"

    def __init__(self, nome, cargo, setor):
        self.nome = nome
        self.cargo = cargo
        self.setor = setor

    def apresentar(self):
        return f"Olá! Meu nome é {self.nome}, trabalho no setor {self.setor} como {self.cargo} na empresa {Funcionario.empresa}"
