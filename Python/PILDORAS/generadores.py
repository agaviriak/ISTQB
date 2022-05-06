#Generadores
def devuelve_ciudades(*ciudades):
    for i in ciudades:
        yield i

ciudades_devuetas=devuelve_ciudades("Cali","Bogotá","Medellin", "Tumaco")

for i in range(4):
    print(next(ciudades_devuetas))
    
