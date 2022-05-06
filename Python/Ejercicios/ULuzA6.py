import csv

from numpy import average
with open("C:/ALBERTO/Personales/ISTQB/Python/Ejercicios/mpg.csv","r") as csv_file:
    datos = list(csv.DictReader(csv_file))

def calcularRespuestas4(datos):
    prom_cty =  sum(map(int,[ i["cty"] for i in datos]))/len(datos)
    prom_hwy = sum(map(int,[ i["hwy"] for i in datos]))/len(datos)
    prom_cty_e = sum(map(int,[ i["cty"] for i in datos if i["fl"]=="e"]))/len([ i["cty"] for i in datos if i["fl"]=="e"])
    min_hwy_p = min(map(int,[ i["hwy"] for i in datos if i["fl"]=="p"]))
    return (prom_cty, prom_hwy, prom_cty_e, min_hwy_p) #No modificar este retorno

print(calcularRespuestas4(datos))
assert calcularRespuestas4(datos) == (16.858974358974358, 23.44017094017094, 9.75, 14.0)



