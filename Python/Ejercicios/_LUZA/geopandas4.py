from multiprocessing.sharedctypes import Value
from operator import index
import pandas as pd
import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt #Importar el modulo pyplot
from shapely.geometry import Point

mapa = gpd.read_file(r"C:\ALBERTO\Personales\ISTQB\_archivos\colombia.geo.json")
posiciones = pd.read_csv(r"C:\ALBERTO\Personales\ISTQB\_archivos\Dpt-longitud-latitud.csv",index_col=[0])
df=pd.read_csv(r"C:\ALBERTO\Personales\ISTQB\_archivos\Casos_positivos_de_COVID-19_en_Colombia.csv")

def hacerPunto(fila):
    return Point(fila.longitud, fila.latitud)

puntos = posiciones.apply(hacerPunto, axis=1)
valores = gpd.GeoDataFrame(posiciones, geometry=puntos)

#__________________________________________________________


#Agregar código corto en df COVID de la misma forma que el df Valores (Coordenadas)
#divipola= df["Código DIVIPOLA"]
#df["cod"]=0
#df["cod"]=[(str(i)[:-3]) for i in divipola]

#Se obtiene la cantidad de casos agrupados por el cod de departamento
agrupado_ciu=df.groupby(['Código DIVIPOLA']).size().reset_index(name='casos')
divipola=agrupado_ciu["Código DIVIPOLA"]
agrupado_ciu["cod"]=0
agrupado_ciu["cod"]=[(str(i)[:-3]) for i in divipola]
agrupado_ciu = (agrupado_ciu.sort_values('casos',ascending=False)).head(10)
#Se crea lista con Nro de casos por dpto para el llenado del campo en la tabla valores
lista=[]
cod_valores=valores["Cod Dpto"]
cod_agrupado=agrupado_ciu["cod"]
for i in cod_agrupado:
    for y in cod_valores:
        if int(i)==int(y):
            casos=((agrupado_ciu.loc[agrupado_ciu["cod"] == str(y)][["casos"]]).iloc[0,0])
            lista.append(casos)
        else:
            lista.append(0)
    

valores["Covid"]=0
#valores["Covid"]=[i for i in lista ]

#if agrupado_ciu["cod"]==valores["Cod Dpto"]:


print("Agrupado por ciudad")
print(agrupado_ciu)
print(lista)
print("DANE existente en valores")
print(valores)
#print(valores.info())

#___________________________________________________________
#Plotear

#Se plotea el mapa
#ax=mapa.plot(color='lightblue', linewidth=0.5, edgecolor='white',figsize=(20,10))
#Se plotean los valores de la columna valores["Covid"]
#valores.plot(markersize=valores["Covid"], alpha=0.7, ax=ax, figsize=(20,10), column="Covid")
#ax.axis('off')

#plt.show()
