def maslarga(lista):
    largo=0
    for i in lista:
        if len(i)>largo:
            mostrar=i
    return lista, mostrar

lista1=["Hola","Hola mundo","Hola mundo feliz"]
print(maslarga(lista1))

