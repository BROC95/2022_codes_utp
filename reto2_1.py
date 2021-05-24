# Reto 2
# La entidad Av´ıcola Colombia debe administrar las facturas que tiene por cobrar, por venta de sus productos.
#  Estas facturas son almacenadas en una base
# de datos en forma de diccionario, en donde la clave es igual al numero de la
# factura, y el valor igual al valor total de la factura. Se requiere para la gesti´on
# de este proceso un programa que le permita a la entidad a˜nadir nuevas facturas,
# de igual forma deber´a poderse abonar a estas facturas un valor parcial o pagarla
# completamente, en caso de realizarse un abono por el valor total de la factura,
# esta deber´a ser eliminada. Se asume que nunca se va a realizar un abono superior al valor pendiente. 
# 
# Posterior a la operaci´on de abono o adici´on de factura,
# se deber´a mostrar por pantalla, como mensaje los valores de el cliente, el numero de factura, 
# la cantidad abonada hasta el momento y el valor pendiente:
# {’cliente’: idCliente, ’factura’: numFactura, ’abono’: valorCalculado, ’valor’:
# valorCalculado}, y el estado de la base de datos. Si la factura sobre la que
# se desea abonar no existe deber´a mostrar como mensaje: {‘numFactura’: ‘No
# existe la factura’}
# Cada factura tiene asociado un cliente, antes de poder realizar cualquier operaci´on sobre una factura 
# deber´a existir el cliente asociado. Para el cliente solo
# se almacena idCliente. Cada cliente inicia con un diccionario vaci´o. Si trata
# de operar sobre una factura para un cliente que no existe deber´a mostrar como
# mensaje: {‘idCliente’: ‘No existe el cliente’}
# Si se hace un llamado para la creaci´on de un cliente y se envian datos de una
# factura no se podr´a crear el cliente y se deber´a mostrar el mensaje para cliente
# que no existe. Al crear un cliente se debe mostrar como mensaje: {‘idCliente’:
# ‘Cliente creado’}.

# opcion int valor entero entre 0 y 3
# idCliente int valor entero mayor a 0
# numFactura int valor entero mayor a 0
# valor float valor flotante mayor a 0
# db dict diccionario con el estado actual de la base de datos


def facturas ( opcion : int , idCliente : int = 0, numFactura : int =0, valor : int = 0, db: dict ={}) -> dict :
    # Su codigo
    valorCalculado=0
    Mensaje={}
    # 0 Crear cliente
    # 1 Añadir factura
    # 2 Abono parcial o totalnote
    # 3 Mostrar base de datos
   
    Pasa=False
    if opcion >=0 and opcion <=3 and idCliente >=0 and numFactura>=0 and valor >= 0:
        Pasa=True
    else:
        facturas( opcion , idCliente , numFactura , valor, db)
    


    if opcion == 0:

      
        ClienteN={str(idCliente):"Cliente creado"}
     
        # for clave,valor in ClienteN.items(): 
        #     # print ("El valor de la clave %s es %s" % (clave, valor))
        #     valor1=valor
        #     clave1=int(clave)
        Mensaje=ClienteN
        newdb={}
        Estado ={idCliente:newdb}
        db.update(Estado)

    if opcion ==1:
        if idCliente in db:
         Mensaje={'cliente': idCliente,'factura': numFactura, 'abono': valorCalculado, 'valor':valor}
         facturaN={numFactura:valor}
         db[idCliente].update(facturaN)
        
        else:
             Mensaje={str(idCliente): "No existe el cliente"}
        
            

    elif opcion ==2:
        if idCliente in db:
           
            if numFactura in db[idCliente]:
               
                valorCalculado= db[idCliente][numFactura]-valor
               
                if valorCalculado >0:
                    Mensaje={'cliente': idCliente,'factura': numFactura, 'abono': valor, 'valor':valorCalculado}
                    facturaN={numFactura:valorCalculado}
                    
                    db[idCliente].update(facturaN)
                else:
                    Mensaje={'cliente': idCliente,'factura': numFactura, 'abono': valor, 'valor':valorCalculado}
                    db[idCliente].pop(numFactura)
            
            else:
                Mensaje={str(numFactura): "No existe la factura"}
        else:
             Mensaje={str(idCliente): "No existe el cliente"}


            
   
    elif opcion ==3:
        Mensaje= {'print': "estado de la base de datos"}
    # pass
    
 
    return Mensaje , db
    
# msj , dbFacturas = facturas (0 ,2541)
# print (msj , dbFacturas )
# msj , dbFacturas = facturas (0 ,2542)
# print (msj , dbFacturas )
# msj , dbFacturas = facturas (1 ,2541 , 1, 300000 , db=dbFacturas )
# print (msj , dbFacturas )
# msj , dbFacturas = facturas (2 ,2541 , 1, 300000 , db= dbFacturas )
# print (msj , dbFacturas )
# msj , dbFacturas = facturas (2 ,2541 , 10, 300000 , db=dbFacturas )
# print (msj , dbFacturas )
# msj , dbFacturas = facturas (1 ,2541 , 2, 500000 , db=dbFacturas )
# print (msj , dbFacturas )
# msj , dbFacturas = facturas (3 ,
# db= dbFacturas )
# print (msj , dbFacturas )



# def facturas (opcion: int, idCliente: int = 0, numFactura: int = 0, valor: int = 0, db: dict ={}) -> dict:
#     mensaje = {}
#     if(opcion == 0):
#         if(numFactura !=0 or valor != 0):
#             mensaje = {str(idCliente): "no existe cliente"}
#         else:
#             db.update({idCliente: {}})
#             mensaje = {str(idCliente): "cliente creado"}
#     elif(opcion == 1):

#         if idCliente in db:
#             db[idCliente].update({numFactura: valor})
#             mensaje = {"cliente": idCliente, "factura": numFactura, "abono":0, "valor": valor}
#         else:
#             mensaje = {str(idCliente): "no existe el cliente"}

#     elif(opcion ==2):

#         if idCliente in db:
#             if numFactura in db[idCliente]:
#                 restante = db[idCliente][numFactura] - valor
#                 if restante <=0:
#                     del db[idCliente][numFactura]
#                 else:
#                     db[idCliente][numFactura] = restante
#                 mensaje = {"cliente": idCliente, "factura": numFactura, "abono": valor, "valor": restante}
#             else:
#                 mensaje = {numFactura: "no existe la factura"}
#         else:
#             mensaje = {str(idCliente): "no existe el cliente"}
#     elif(opcion == 3):

#         mensaje = {"print:":"estado de la base de datos"}

#     return mensaje, db










# Pruebas
msj , dbFacturas = facturas (0 ,2541)
print (msj , dbFacturas )
msj , dbFacturas = facturas (1 ,2541 , 1, 300000 , db=dbFacturas )
print (msj , dbFacturas )
msj , dbFacturas = facturas (2 ,2541 , 1, 25000.25487 , db= dbFacturas )
print (msj , dbFacturas )
msj , dbFacturas = facturas (1 ,2541 , 2, 500000 , db=dbFacturas )
print (msj , dbFacturas )
# msj , dbFacturas = facturas (3 ,db= dbFacturas )
# print (msj , dbFacturas )
msj , dbFacturas = facturas (2 ,1429 , 5, 25000.25487 , db= dbFacturas )
print (msj , dbFacturas )
# msj , dbFacturas = facturas (3 ,db= dbFacturas )
# print (msj , dbFacturas )
msj , dbFacturas = facturas (1 ,1429 , 1, 700000 , db=dbFacturas )
print (msj , dbFacturas )
msj , dbFacturas = facturas (2 ,1429 , 1, 700000 , db=dbFacturas )
print (msj , dbFacturas )
msj , dbFacturas = facturas (0 ,1429 , 1, 700000 , db=dbFacturas )
print (msj , dbFacturas )
msj , dbFacturas = facturas (0 ,1429 , db= dbFacturas )
print (msj , dbFacturas )
msj , dbFacturas = facturas (1 ,
1429 , 1, 700000 , db=dbFacturas )
print (msj , dbFacturas )
msj , dbFacturas = facturas (5,2541 , 1, 274999.74513 ,db= dbFacturas )
print (msj , dbFacturas )
msj , dbFacturas = facturas (3 ,db= dbFacturas )
print (msj , dbFacturas )
