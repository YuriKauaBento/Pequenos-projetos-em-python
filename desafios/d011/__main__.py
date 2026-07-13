from d011 import *

def main():
    f1 = Horista("Stephany", 100, 180)
    f1.calcular_sal()
    print(f1.analisar_sal())

    f2 = Mensalista("Yuri", 2700)
    f2.calcular_sal()
    print(f2.analisar_sal())


if __name__ == '__main__':
    main()
