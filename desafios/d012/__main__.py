from RPG import *


def main():
    p1 = Guerreiro("gorgoroth", 20, 10)
    p2 = Mago("Nephthys", 12, 8)

    p2.atacar(p1, 10)
    p1.curar()


if __name__ == '__main__':
    main()