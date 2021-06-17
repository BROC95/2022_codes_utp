
import json
from numpy.core.numeric import NaN
from numpy.lib.function_base import percentile
from numpy.lib.utils import info
from numpy.testing._private.utils import print_assert_equal
import pandas as pd
import numpy as np
import requests
import urllib


from functools import reduce
def preProcesado (DF):
    # Funcion que prepara los generos en un DF para ser codificadas en la matriz
    # Devuelve tambien los generos en una lista

   
    categoriasDF = DF['categories'].apply(pd.Series )
    categoriasDF ['business_id'] = DF['business_id']
    # categoriasDF = categoriasDF.drop_duplicates (['business_id'])
    categoriasDF.set_index('business_id', inplace = True )
    # categories = [ categoriasDF [ categorie ].unique() for categorie in categoriasDF.columns ]
    # categories = [ categorie for lista in categories for categorie in lista if all([ pd.isnull ( categorie ) == False , categorie != ' ', categorie != '', len (str ( categorie )) > 1]) ]
    # categories = list ( set ( categories ))
    # categoriasDF = DF['categories'].apply(pd.Series )
    Unircat = reduce(lambda acu =0,ele=0:acu +ele,categoriasDF.values)
    Unircat = reduce(lambda acu =0,ele=0:acu +ele,Unircat)
    categories =list(set(Unircat))
    categoriesDat= pd.DataFrame(categories)


    return categoriasDF , categoriesDat

def codificaMatriz (DF , genres : list , producto : list ):
    # Funcion que inserta unos en la matriz
    # Su codigo aqui
    DF=pd.read_csv(DF,sep=';',header=None,names= ["id","puntuacion"])
    DF= pd.DataFrame(DF)
    # DF.index.name='business_id'
    
    
    # #(DF.transpose())
    filas= DF.items
    # #(filas)
    # #(columnas)
    datosF= producto.values
    # #(datosF)
    # #(DF.values)
    valDF = DF.apply(pd.Series )
    # #(valDF.loc[1])
    # #(DF.columns)
    idnames=genres.index
    informacion = idnames[0].items()
    columnasN=[]
    for key, value in informacion:
        # #(key,value)
        columnasN.append(value)
    n=len(datosF)
    m=int(len(columnasN))
    # #("Matriz",n,"x",m)
    datosC=np.zeros((n,m))
    datosV= DF['puntuacion'].values
    # #(len(datosV))
    # #(len(columnasN))
    DF_M=pd.DataFrame(datosC,columns=columnasN,index=datosF)
    DF_V=pd.DataFrame(datosV).transpose()
    # #(DF_V.transpose())
    DF_V.columns=columnasN
    DF_V.index=["Puntuacion"]
    # #("Matrix")
    # #(DF_M)
    # #(DF_V)
    # # #(genres.shape)
    # #(informacion)
    # #(genres.columns)
    # #(genres.values.shape)
    #(DF_M.columns)


    
    # categoriasDF.set_index('business_id', inplace = True )
    # #("uu")
    # #(infoDat[0])
    # #(infoDat[1].values)
    # #(DF_M.shape)
    
    # #(genres['10'].values)
    for indexc in DF_M.columns:
        # #(indexc)
        for genero in range(n):
            # #(genero)
            for  key,value in informacion:
                if value== indexc: 
                    # #(value,indexc)
                        # #(type(producto[0][genero]))
                        # #("Busque")
                        Unir = reduce(lambda acu =0,ele=0:acu +ele,genres[key].values)
                        # #(Unir)
                        # #(producto[0][genero])
                        # #(producto[0][genero])
                        if producto[0][genero] in Unir:
                            # #(producto[0][genero])
                            # #(Unir)
                            # #(True)
                            # #("Existe")
                            # #(DF_M[indexc][genero])
                            DF_M[indexc][genero]=1

                            # #(DF_M[indexc][genero])

                        else:
                            # #(False)
                            continue
            
                
                  
    return DF_M, DF_V# Debe retornar un DF como el de la Tabla 1.

def codificaMatriz3 ( genres : list , producto : list ):
    # Funcion que inserta unos en la matriz
    # Su codigo aqui
    # DF=pd.read_csv(DF,sep=';',header=None,names= ["id","puntuacion"])
    DF= pd.DataFrame(producto)
    # DF.index.name='business_id'
    
    
    # #(DF.transpose())
    filas= DF.items
    # #(filas)
    # #(columnas)
    datosF= producto.values
    # #(datosF)
    # #(DF.values)
    valDF = DF.apply(pd.Series )
    # #(valDF.loc[1])
    # #(DF.columns)
    idnames=genres.index
    informacion = idnames[0].items()
    columnasN=[]
    for key, value in informacion:
        # #(key,value)
        columnasN.append(value)
    n=len(datosF)
    m=int(len(columnasN))
    # #("Matriz",n,"x",m)
    datosC=np.zeros((n,m))
    # datosV= DF['puntuacion'].values
    # #(len(datosV))
    # #(len(columnasN))
    DF_M=pd.DataFrame(datosC,columns=columnasN,index=datosF)
    # DF_V=pd.DataFrame(datosV).transpose()
    # #(DF_V.transpose())
    # DF_V.columns=columnasN
    # DF_V.index=["Puntuacion"]
    # #("Matrix")
    # #(DF_M)
    # #(DF_V)
    # # #(genres.shape)
    # #(informacion)
    # #(genres.columns)
    # #(genres.values.shape)
    #(DF_M.columns)


    
    # categoriasDF.set_index('business_id', inplace = True )
    # #("uu")
    # #(infoDat[0])
    # #(infoDat[1].values)
    # #(DF_M.shape)
    
    # #(genres['10'].values)
    for indexc in DF_M.columns:
        # #(indexc)
        for genero in range(n):
            # #(genero)
            for  key,value in informacion:
                if value== indexc: 
                    # #(value,indexc)
                        # #(type(producto[0][genero]))
                        # #("Busque")
                        Unir = reduce(lambda acu =0,ele=0:acu +ele,genres[key].values)
                        # #(Unir)
                        # #(producto[0][genero])
                        # #(producto[0][genero])
                        if producto[0][genero] in Unir:
                            # #(producto[0][genero])
                            # #(Unir)
                            # #(True)
                            # #("Existe")
                            # #(DF_M[indexc][genero])
                            DF_M[indexc][genero]=1

                            # #(DF_M[indexc][genero])

                        else:
                            # #(False)
                            continue
            
                
                  
    return DF_M # Debe retornar un DF como el de la Tabla 1.
def getResponse(url):
    operUrl = urllib.request.urlopen(url)
    if(operUrl.getcode()==200):
        data = operUrl.read()
        jsonData = json.loads(data)
    else:
        print("Error receiving data", operUrl.getcode())
    return jsonData
def recomiendaNegocio ( url_puntuacion :str , url_perfil :str , url_recomendacion : str)->json :

    # Su codigo aqui
    DF= pd.DataFrame([getResponse(url_perfil)])
    generos, categoria = preProcesado(DF)
    Tabla1, punt1 = codificaMatriz(url_puntuacion,generos,categoria)
    Tabla2= punt1.values*Tabla1.values
    #("tabla 1")
    #(Tabla1.values)
    #(punt1.values)
    #("tabla 2")
    #(Tabla2)
    totalM=sum(sum(Tabla2))
    perfilUsuarioD=Tabla2/totalM
    # perfilUsuarioD=round(Tabla2/totalM,2)
    #("Tabla2D")
    # #(perfilUsuarioD)
   
    n,m=perfilUsuarioD.shape
    VectorUs=[]
    for k in range(n):
        datosNocero = list(filter(lambda n: n  != 0, perfilUsuarioD[k]))
        VectorUs.append(datosNocero)
 

    DatPer= [sum(n) for n in VectorUs]
    #(DatPer)
    #(len(DatPer))
    Perfil_de_Usuario= pd.DataFrame(DatPer)
    Perfil_de_Usuario.columns=['Perfil_de_Usuario']
    Perfil_de_Usuario.index=Tabla1.index
    #(Perfil_de_Usuario)

    ############################## 3 
    DFR= pd.DataFrame([getResponse(url_recomendacion)])

    DFR_D,DFR_C = preProcesado(DFR)
    Tabla3_1= codificaMatriz3(DFR_D,DFR_C)
    # #(DFR_D,DFR_C)
    # #(Tabla3)
    Tabla3=Tabla3_1.values
    totalMR=sum(sum(Tabla3))
    #(totalMR)
    perfilUsuarioDr=Tabla3
    # perfilUsuarioD=round(Tabla2/totalM,2)
    #("Tabla2D")
    # #(perfilUsuarioD)
   
    n,m=perfilUsuarioDr.shape
    VectorUsr=[]
    for k in range(n):
        datosNocero = list(filter(lambda n: n  != 0, perfilUsuarioDr[k]))
        VectorUsr.append(datosNocero)
 

    DatPerR= [sum(n) for n in VectorUsr]
    #(DatPerR)
    #(len(DatPerR))
    R=len(DatPerR)
    datosR=np.zeros(R)
    Perfil_de_UsuarioR= pd.DataFrame(datosR)
    Perfil_de_UsuarioR.columns=['Perfil_de_Usuario']
    Perfil_de_UsuarioR.index=Tabla3_1.index
    #(Perfil_de_UsuarioR.iloc[0].name)
    # for k in range(R):
    #     if Perfil_de_Usuario.index.any in Perfil_de_UsuarioR.iloc[k].name:
    #         #(k)
    #         #(Perfil_de_Usuario.index.all)
    #         #(Perfil_de_UsuarioR.iloc[k].name)
    for k in range(R):
        if Perfil_de_UsuarioR.iloc[k].name in Perfil_de_Usuario.index:
            #(k)
            # #(Perfil_de_Usuario.index)
            # #(Perfil_de_UsuarioR.iloc[k].name)
            key=Perfil_de_UsuarioR.iloc[k].name
            #(key)
            # Perfil_de_UsuarioR[key]=Perfil_de_Usuario[key]
            # #(Perfil_de_UsuarioR[k].values)
            #(Perfil_de_UsuarioR.iloc[k].values)
            # #(Perfil_de_Usuario.loc[key].values)
            
            # #(Perfil_de_UsuarioR.iloc[k].values)
            infoPer_Usu= Perfil_de_Usuario.items()
            # #(infoPer_Usu)
            for fila, col in infoPer_Usu:
                # #(col[key])
                Perfil_de_UsuarioR.iloc[k]=col[key]    
                # #("Nuevo",Perfil_de_UsuarioR.iloc[k])


    #(Perfil_de_UsuarioR.values)
    #(Tabla3)

    Matcandi=Perfil_de_UsuarioR.values*Tabla3
    # #(Matcandi)
    # #(Matcandi)
    Matcandi = pd.DataFrame(Matcandi,columns=Tabla3_1.columns,index=Tabla3_1.index)
    # #(Matcandi.head(3))
    #(Matcandi.values)

    
    n,m= Matcandi.shape
    datPond=0
    MatcandiD=Matcandi.values
    #(type(MatcandiD))
    #(n,m)
    # for col in range(m):
    #     Ponderacion=np.apply_along_axis(sum, col, MatcandiD)
    Ponderacion=np.apply_along_axis(np.sum, 0, MatcandiD)
    # #(np.round(Ponderacion,5))
    Ponderacion= np.round(Ponderacion,5)

    DF_Pond= pd.DataFrame(Ponderacion,columns=['P'],index=Matcandi.columns)
    # #(DF_Pond.sort_values)
    #(DF_Pond.columns)
    df= DF_Pond.replace(0,NaN)
    df=df.dropna(how='all',axis=0)
    df=df.replace(NaN,0)
    #(df.values)
    #(df.sort_values(['Pond'],ascending=False))

    df=df.sort_values(['P'],ascending=False)
    datosVal= df.values
    datosIndex= df.index
  

    # df= df.rename(columns={'Pond':NaN})
    df_R_Js= df.to_json(orient='columns')
    parsed= json.loads(df_R_Js)
    DF_Re= json.dumps(parsed,indent=4)
    # print(DF_Re)
    # #(type(DF_Re))
    # jsonData = '{"name": "Frank", "age": 39}'
    jsonToPython = json.loads(DF_Re)
    #(type(jsonToPython))
    #(jsonToPython.items)
    # items=jsonToPython.items()
    for k ,j in jsonToPython.items():
        #(k,j)
        datosR=j
    
    DF_Re= json.dumps(datosR,indent=4)
    return DF_Re

    


    


    
url_puntuacion= "https://git.io/JZKue"
url_perfil = "https://git.io/JZK0H"
url_recomendacion= "https://git.io/JZKE4"

url_puntuacion= "https://git.io/JZKuk"
url_perfil= "https://git.io/JZK0A"
url_recomendacion ="https://git.io/JZKEg"

# #(preProcesado(url_puntuacion))
# #(codificaMatriz(url_puntuacion,[],[]))


print(recomiendaNegocio(url_puntuacion,url_perfil,url_recomendacion))




