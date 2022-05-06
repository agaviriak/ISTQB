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
print(valores.head())

def randomCovid(f):
    return np.random.randint(1,200)

valores["Covid"]=0
valores["Covid"]= valores["Covid"].apply(randomCovid)
print(valores.head())

#Se plotea el mapa
ax=mapa.plot(color='lightblue', linewidth=0.5, edgecolor='white',figsize=(20,10))
#Se plotean los valores de la columna valores["Covid"]
valores.plot(markersize=valores["Covid"], alpha=0.5, ax=ax, figsize=(20,10), column="Covid")
ax.axis('off')

#__________________________________________________________

def CovidDpto(f):
    casos=len(f["cod"])
     
    return casos



divipola= df["Código DIVIPOLA"]
df["cod"]=0
#fila=0
#for i in divipola:
#    i= (str(i)[:-3])
#    df.loc[fila,"cod"]=i
#    fila=fila+1

df["cod"]=[(str(i)[:-3]) for i in divipola]

print("Dataframe Covid")
print(df[["Código DIVIPOLA","cod"]])
print("Tabla de dptos con coordenadas llmada valores")
print(valores[["Cod Dpto","longitud","latitud"]].head())
print(CovidDpto(df))
#___________________________________________________________

#agrupado_dep=df.groupby(by="cod").count()
agrupado_dep=df.groupby(['cod']).size().reset_index(name='casos')
#numcasos=agrupado_dep["ID de caso"]
print(agrupado_dep.head(3))
#print(agrupado_dep.get_group("cod"))
#print(numcasos.head(3))
#for i in numcasos:
#    print(i)

#plt.show()
