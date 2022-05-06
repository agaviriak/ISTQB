import csv

from numpy import average
with open("C:/ALBERTO/Personales/ISTQB/Python/Ejercicios/mpg.csv","r") as csv_file:
    datos = list(csv.DictReader(csv_file))

def calcularRespuesta5a(datos, fabricante1, fabricante2, año):
    fabricante1_p =  sum(map(int,[ i["cty"] for i in datos 
    if i["manufacturer"]==fabricante1 and i["year"]==año]
    ))/len([ i["cty"] for i in datos 
    if i["manufacturer"]==fabricante1 and i["year"]==año])

    fabricante2_p =  sum(map(int,[ i["cty"] for i in datos 
    if i["manufacturer"]==fabricante2 and i["year"]==año]
    ))/len([ i["cty"] for i in datos 
    if i["manufacturer"]==fabricante2 and i["year"]==año])
      
    return (fabricante1_p, fabricante2_p) #No modificar este retorno

cilindros = sorted({m['cyl'] for m in datos})

print(cilindros)

