import csv
with open("C:/ALBERTO/Personales/ISTQB/Python/Ejercicios/mpg.csv","r") as csv_file:
    datos = list(csv.DictReader(csv_file))

def calcularRespuestas3(datos):
    manufacturer = sorted (set([ i["manufacturer"] for i in datos]))
    cyl =sorted (set([ i["cyl"] for i in datos]))
    drv =sorted (set([ i["drv"] for i in datos]))
    cty =sorted (map(int, set([ i["cty"] for i in datos])))
    hwy =sorted (map(int, set([ i["hwy"] for i in datos])))
    return (manufacturer, cyl, drv, cty, hwy) #No modificar este retorno

#print(datos)    
#print(calcularRespuestas3(datos))
manufacturer,cyl,drv,cty,hwy = calcularRespuestas3(datos) 
#print(manufacturer)
assert manufacturer == ['audi','chevrolet','dodge','ford','honda','hyundai','jeep','land rover','lincoln','mercury','nissan','pontiac','subaru','toyota','volkswagen']
assert cyl == ['4', '5', '6', '8']
