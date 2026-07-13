from credencial import *
from rich import print


def main():
    a = Credencial()

    try:
        a.senha = ""
        print(a.senha)
    except Exception as e:
        print(f"[red]Erro:[/] [purple]{e}[/]")

    a.validar("Widoumaker7!")


if __name__ == "__main__":
    main()