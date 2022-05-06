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

def calcularRespuesta5b(datos, cyl1, cyl2, año):
    hwy1_p = sum(map(int,[ i["hwy"] for i in datos 
    if i["cyl"]==cyl1 and i["year"]==año]))/len([ i["hwy"] for i in datos 
    if i["cyl"]==cyl1 and i["year"]==año])
    
    hwy2_p = sum(map(int,[ i["hwy"] for i in datos 
    if i["cyl"]==cyl2 and i["year"]==año]))/len([ i["hwy"] for i in datos 
    if i["cyl"]==cyl2 and i["year"]==año])
    
    return (hwy1_p, hwy2_p) #No modificar este retorno

print(calcularRespuesta5a(datos,"chevrolet","audi","1999"))
print(calcularRespuesta5b(datos,"4","8","1999"))

cilindros = {d['cyl'] for d in datos}
print(cilindros)



