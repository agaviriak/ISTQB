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

#Se incluyen datos solo a anivel de dptos, por lo cual se excluyen los distritos
#especiales, excepto Bogotá DC que tiene código DANE propio y no lo comparte con Cundinamarca

mascara1 = (valores["Dpto"] == "Barranquilla D.E.")
mascara2 = (valores["Dpto"] == "Cartagena D.T. y C.")
mascara3 = (valores["Dpto"] == "Santa Marta D.T. y C.") 
mascara4 = (valores["Dpto"] == "Buenaventura D.E.")

valores=valores[~mascara1]
valores=valores[~mascara2]
valores=valores[~mascara3]
valores=valores[~mascara4]

#Agregar código corto en df COVID de la misma forma que el df Valores (Coordenadas)
divipola= df["Código DIVIPOLA"]
df["cod"]=0
df["cod"]=[(str(i)[:-3]) for i in divipola]

#Se obtiene la cantidad de casos agrupados por el cod de departamento
agrupado_dep=df.groupby(['cod']).size().reset_index(name='casos')

#Se crea lista con Nro de casos por dpto para el llenado del campo en la tabla valores
lista=[]
cod_valores=valores["Cod Dpto"]
cod_agrupado=agrupado_dep["cod"]
for i in cod_valores:
    for y in cod_agrupado:
        if int(i)==int(y):
            casos=((agrupado_dep.loc[agrupado_dep["cod"] == str(y)][["casos"]]).iloc[0,0]/500)
            lista.append(casos)
    
valores["Covid"]=0
valores["Covid"]=[i for i in lista]

#___________________________________________________________
#Plotear

#Se plotea el mapa
ax=mapa.plot(color='lightblue', linewidth=0.5, edgecolor='white',figsize=(20,10))
#Se plotean los valores de la columna valores["Covid"]
valores.plot(markersize=valores["Covid"], alpha=0.7, ax=ax, figsize=(20,10), column="Covid")
ax.axis('off')

plt.show()
