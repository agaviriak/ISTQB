def cuentaOcurrencias(lista):
    l1=[]
    l2=[]

    contador = 0
    for i in lista:
        if i not in l1:
            l1.append(i)       
    l1 = sorted(l1)

    for i in l1:
        ocurrencia=lista.count(i)
        l2.append(ocurrencia)

    return(l1,l2)

'''Caso1'''
assert cuentaOcurrencias(["rojo","negro","blanco","negro","rojo","verde","rojo"]) == (['blanco', 'negro', 'rojo', 'verde'], [1, 2, 3, 1])
''' Caso 2 '''
assert cuentaOcurrencias(["rojo","negro","blanco","negro","rojo","rojo"]) == (['blanco', 'negro', 'rojo'], [1, 2, 3])


