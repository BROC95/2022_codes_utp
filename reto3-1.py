

from math import ceil

def bancoAmigo ( nuip : int , depositos : []) -> tuple :
    """
    Parametros
    nuip ( int ): Numero de i d e n t i f i c a c i o n del usuario
    list ([]) : lista con los 12 depositos del mes
    Retorno
    Tuple : de la forma ( ahorroTotal , interesGenerado , montoFinal )
    """
  
    inte7=7/100
    inte12=12/100
    inte5=5/100
    AhorroMax=3600000
    mes300= 300000
    InteresAnual=0

    totalmesAnterior=0
  
    # Su codigo
    meses = len(depositos)
    
    if meses ==12:
        ahorroTotal= sum(depositos)
        if ahorroTotal < AhorroMax:
            interesGenerado=ahorroTotal*inte7
        else:
            interesGenerado=ahorroTotal*inte12

        for mes in depositos:

            A= totalmesAnterior+mes
            
            if mes>=mes300:
                interesMes= A*inte5
                
          
            else:
                interesMes=0
            InteresAnual+=interesMes
            totalmesAnterior= A+interesMes
            
        interesGenerado=interesGenerado+InteresAnual
        montoFinal=ahorroTotal+interesGenerado


    return nuip , ahorroTotal , ceil ( interesGenerado ) , ceil (montoFinal )


# Caso de prueba 1:
print ( bancoAmigo (2148542 ,
[300000 ,450000 ,0 ,0 ,0 ,0 ,260000 ,0 ,500000 ,0 ,420000 ,0]) )
# (2148542 , 1930000 , 369584 , 2299584)

# Caso de prueba 2:
print ( bancoAmigo (10821247 ,
[50000 ,0 ,350000 ,0 ,720000 ,0 ,220000 ,0 ,0 ,455000 ,0 ,60000]) )
# (10821247 , 1855000 , 300450 , 2155450)

# Caso de prueba 3:
print ( bancoAmigo (1254221 ,
[0 ,0 ,700000 ,1520000 ,0 ,0 ,0 ,580000 ,0 ,520000 ,0 ,0]) )
# (1254221 , 3320000 , 708295 , 4028295)