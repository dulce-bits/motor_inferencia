from generador import *
from encadenamientos import *
import os

def comp(lista1, lista2):
    for val in lista1:
        if val not in lista2:
            return False
    return True

if __name__ == "__main__":
    gen = Generador()
    ctrl = True
    while(ctrl):
        print('Motor de inferencia\nElaborado por:\nDulce Celeste Cruz Ramírez\nRuben Esau García Gómez')
        
        print('Ingrese ruta del archivo que contiene la base de conocimientos')
        filename = input()
        BC = gen.GenerarBC(filename)

        print('Ingrese el numero de elementos en la base de hechos')
        n = int(input())
        BH = gen.GenerarBH(n)

        print('Ingrese la meta')
        m = input()

        flag = True
        while(flag):
            print('Elija el mecanismo de evaluación\n1 - Encadenamiento hacia adelante\n2 - Encadenamiento hacia atrás')
            opc = input()
            flag = False
            if opc == '1':
                print('Encadenamiento hacia adelante')
                EncadenamientoHAd([BC,BH,m])
            elif opc == '2':
                print('Encadenamiento hacia atrás')
                print('|NH   | Meta | R  |     BH     ')
                print('|     |  '+m+'   |    |'+str(BH))
                m, BH= EncadenamientoHA([BC,BH,m])
                if comp(m, BH):
                    print('El sistema si tiene solución')
                else:
                    print("El sistema no tiene solución")  
            else:
                print('Error, intentelo de nuevo')
                flag = True
        
        flag = True
        while(flag):
            print('¿Desea hacer otra ejecución?\nS - Si\nN - No')
            opc = input()
            flag = False
            if opc == 'S':
                os.system('cls')
            elif opc == 'N':
                ctrl = False
            else:
                print('Error, intentelo de nuevo')
                flag=True
        print('Terminando programa...\nAdios')