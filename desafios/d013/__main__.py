from termostato import *
from rich import print


def main():
    t = Termostato()
    try:
        t.temp = 20.3
        print(f"A temperatura é {t.ftemp}")
    except Exception as e:
        print(f"[red]Erro:[/] {e}")

if __name__ == "__main__":
    main()