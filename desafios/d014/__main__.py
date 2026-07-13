from diario import *


def main():
    d = Diario()

    d.escrever("Olá, me chamo Yuri")
    d.escrever("Como vai?")
    d.escrever("")

    try:
        d.ler("Widoumaker7")
    except Exception as e:
            print(f"[red]ERRO:[/] [purple]{e}[/]")


if __name__ == "__main__":
    main()