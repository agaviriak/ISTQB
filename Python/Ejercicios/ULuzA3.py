import csv
with open("C:/ALBERTO/Personales/ISTQB/Python/Ejercicios/mpg.csv","r") as csv_file:
    datos = list(csv.DictReader(csv_file))

def averiguarClaves(datos):
    '''Función que retorna la cantidad de datos en el dataset'''
    # YOUR CODE HERE
    claves=list(datos)
    return claves
    raise NotImplementedError()
assert averiguarClaves(datos[0]) == ['','manufacturer','model','displ','year','cyl','trans','drv','cty','hwy','fl','class','register']




