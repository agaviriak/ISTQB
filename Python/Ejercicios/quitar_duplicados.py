def quitar_duplicados(lista):
    lista.sort()
    print(lista)
    lista2=[]
    for i in lista:
        if i not in lista2:
            lista2.append(i)
    lista=lista2
    return lista
        

lista1=[1,2,1,4,1,6,2,7,8,1,1,4,2,1]
print(quitar_duplicados(lista1))

