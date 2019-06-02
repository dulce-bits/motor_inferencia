#   Autor: Alejandro Rafael Salvador
#   Fecha: 30/05/2019
#   Descripcion: Este script almacena la logica del motor de inferencia

from ventana import *   #Hace una importacion de los graficos para su ejecucion

from generador import *
from encadenamientos import *

if __name__ == "__main__":
    generador = Generador()

    print ("Encadenamiento hacia adelante")
    EncadenamientoHAd([generador.GenerarBC(6), generador.GenerarBH(3), generador.GenerarMeta()])
    
    print()

    print ("Encadenamiento hacia atras")
    print('|NM   | Meta   | R  |     BH     ') #se imprime el encabezado aqui porque la recursividad lo imprimiria muchas veces
    EncadenamientoHA([generador.GenerarBC(6), generador.GenerarBH(3), generador.GenerarMeta()])
    