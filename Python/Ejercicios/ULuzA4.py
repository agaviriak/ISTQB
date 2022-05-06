import csv
with open("C:/ALBERTO/Personales/ISTQB/Python/Ejercicios/mpg.csv","r") as csv_file:
    datos = list(csv.DictReader(csv_file))

def cantidadRegistros(datos):
    '''Función que retorna la cantidad de datos en el dataset'''
    # YOUR CODE HERE
    cantidad = len(datos)
    return cantidad
    raise NotImplementedError()

print(cantidadRegistros(datos))

assert cantidadRegistros(datos) == 234


