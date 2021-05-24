"""
Created on Sat May  8 13:29:45 2021

@author: BROC95
"""

"""Descripci´on del problema:
Un coleccionista de figuras abstractas basadas en cubos requiere calcular
 el volumen y el area de las figuras para determinar el espacio que ocupar´an
  en sus bodegas. Se le ha contratado para desarollar un programa
   que permita determinar estos valores. Lo unico que se conoce como
    valor de entrada es el tama˜no del lado de una de las caras del cubo."""


def abstracta ( lado : int , cubos : int = 4) -> tuple :
    """
    Parámetros
    lado ( int ): lado de una cara del cubo
    cubos ( int ) : cantidad de cubos usados para la pieza
    Retorno
    Tuple : de la forma ( lado , area , volumen )
    """
    # Su código
    Areacara=lado**2   # Área de cuadrado
    Areacubo=6*Areacara # Área de un cubo 
    Volcubo=lado**3    # Volumen de un cubo

    # Pieza
    area=cubos*Areacubo # Área por número de cubos
    volumen=cubos*Volcubo   #  Volumen por número de cubos
    return lado , area , volumen


# x=int(input("Ingrese la cantidad de cubos:"))  # Ingrese la cantidad de cubos
                                          # de la figura

# Casos de prueba 
# Coleccion de piezas Pn:(Lado,Cubos)  
coleccion = {"P0":(5,4),"P1":(41,9),"P2":(26,9),"P3":(17,9),"P4":(3,3)}

i=0
for Pieza, cubos in coleccion.items():  # recorre diccionario
    # Información
    # print('Pieza {0}: {1}'.format(Pieza, cubos))  # muestra datos pieza
    # print('Datos lado {0}: '.format( cubos[0]))  # muestra lado metros
    # print('Datos cubos {0}: '.format( cubos[1]))  # muestra cubos
    
    print("Caso de prueba ",i)  # Casos de prueba
    # Calculo requerido
    print ( abstracta (cubos[0] , cubos[1]) )
    
    i+=1 #contador de casos

# print("prueba")
# print ( abstracta (17 , 9) )


