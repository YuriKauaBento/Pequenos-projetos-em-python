from frete import *

def main():
    dist = 6

    entrega1 = Drone(dist)
    entrega2 = Caminhao(dist)
    entrega3 = Moto(dist)
    
    print(entrega1.calcular_frete())
    print(entrega2.calcular_frete())
    print(entrega3.calcular_frete())

if __name__ == '__main__':
    main()