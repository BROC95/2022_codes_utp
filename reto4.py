
from functools import reduce


# positivos_C19 = {
# 'Colombia ': {
# 'Risaralda ': [( 'Pereira ', 45) , (' Dosquebradas ', 15) , ('La Virginia ', 30) ],
# 'Quindio ': [( 'Armenia ', 75) , ('Montenegro ', 86)]
# },
# 'Mexico ': {
# 'Quintana Roo ': [( 'Benito Juarez ', 101) , (' Solidaridad ',
# 56) ],
# 'Nayarit ': [( 'Compostela ', 23) , ('San Blas ', 35) , ('Xalisco ', 74) , ('Del Nayar ', 46) ]
# }
# }
def analizaPacientes ( opt :int , db:dict , pais :str= ''):
    # print(opt)
  
    if opt ==0: #  el promedio de pacientes positivos para todos los pa´ıses (opci´on 0)
        
        if pais !='':
            mensaje= "La opción no recibe país"
            return mensaje
        else:
            paisDat =[]
            paisDatval =[]
        
            DatosXPais=[]
            DataPais =[]
            sumaP=[]
            for pais in db:
                paisDat.append(db[pais])
                items= db[pais].items()
                for x,j in items:
                    # print(x,j)
                    # print(j[1])
                    mun, val = zip(*j)
                    listval =[x for x in val]
                    # print(listval)
                    paisDatval.append(listval)
                    
                    listmun =[x for x in mun]
                    
                
                # 
                i=0
                # print("N")
                sumatoriaP = reduce(lambda acu =0,ele=0:acu +ele,paisDatval)
                sumaP.append(sumatoriaP)
                while i<len(paisDatval):
                    try:
                        # print(paisDatval)
                        paisDatval[0].extend(paisDatval[i+1])
                        # print(i)
                    except IndexError:
                        pass
                    i+=1
                # print("n")
                # print(paisDatval)
                DataPais.append(paisDatval)
                # print(DataPais)
                dato=paisDatval.pop(0)
                # print("Dato")
                # print(dato)
                paisDatval.clear()
           
                DatosXPais.append(dato)
                
                    
       
                
            # print("Datos por pais")
            # print(DatosXPais)
            # Npais = len(DatosXPais)
            Npais = [ len(n) for n in DatosXPais ]
            # print(Npais)
            sumas=[]
            # print(sum(DatosXPais[0]))
            # print(sum(DatosXPais[1]))
            promedP={}
            for i,pais in enumerate(db):
                sumatoriaN = reduce(lambda acu =0,ele=0:acu +ele,DatosXPais[i])
                sumas.append(sumatoriaN)
                promedPn={pais:round(sumatoriaN/Npais[i],2)}
                promedP.update(promedPn)

            # print(sumatoriaP)
            # print(sumas)
            # print(promedP)
            return promedP
            
    elif opt==1: #  y el promedio de pacientes para todos los estados de un 
                # pa´ıs (opci´on 1, en este caso se debe indicar el pa´ıs a consultar)
        try:
            if pais in db:
                paisDatval=[]
                deptName=[]
                # print(pais)
            # print(db[pais])
                items= db[pais].items()
            # print(items)
                for dept,j in items:
                    # print(dept,j)
                    # print(j[1])
                    deptName.append(dept)
                    mun, val = zip(*j)
                    listval =[x for x in val]
                    # print(listval)
                    paisDatval.append(listval)
                        
                    listmun =[x for x in mun]
                # print("val")
                # print(paisDatval)
                Npais = [ len(n) for n in paisDatval ]
                # print(Npais)
                # print(listmun)
                promedD ={}
                # print(deptName)
                # print(len(deptName))
                for i in range(len(paisDatval)):
                    sumatoriaN = reduce(lambda acu =0,ele=0:acu +ele,paisDatval[i])
                    promedDn={deptName[i]:round(sumatoriaN/Npais[i],2)}
                    promedD.update(promedDn)
                    # print(i)
            return promedD

            

        except:
            mensaje="La opción ingresada requiere de un país valido"
            return mensaje

        
    elif opt ==2: # a conocer la localidad con mayor numero de pacientes en un pa´ıs
        if pais == '':
            mensaje="La opción ingresada requiere de un país valido"
            return mensaje
        else:
            if pais in db:
                print(pais,1)
                paisDatval=[]
                # print(pais)
                # print(db[pais])
                items= db[pais].items()
                
                munMax={}
                for x,j in items:
                    # print(x,j)
                    # print(j[1])
                    mun, val = zip(*j)
                    listval =[x for x in val]
    
                    paisDatval.append(listval)
                    maxI= listval.index(max(listval))
                    maxN= max(listval)
                    munM= {db[pais][x][maxI][0]:maxN}
                    munMax.update(munM)

                        

                valorM=max(munMax.values())
            
                for key,val in munMax.items():
                    if val == valorM:
                        clave=key
                
                return tuple((clave,valorM))
      
        
        
            
    else:
        mensaje = "La opción no es valida"
        return mensaje
    




# Se sugiere el uso de lambda y reduce para el calculo del promedio en una
# funci´on que le permita reutilizar parte del c´odigo. Recuerde que try except le
# permite manejar excepciones.



# Pruebas
print ( analizaPacientes (0 , positivos_C19 ))
print ( analizaPacientes (0 , positivos_C19 ,'Mexico'))
print ( analizaPacientes (0 , positivos_C19 ,'perro'))
print ( analizaPacientes (1 , positivos_C19 , 'Mexico '))
print ( analizaPacientes (1 , positivos_C19 , 'Colombia '))
print ( analizaPacientes (1 , positivos_C19 ))
print ( analizaPacientes (2 , positivos_C19 , 'Mexico '))
print ( analizaPacientes (2 , positivos_C19 , 'Colombia '))
print ( analizaPacientes (2 , positivos_C19 ))
print ( analizaPacientes (5 , positivos_C19 ))