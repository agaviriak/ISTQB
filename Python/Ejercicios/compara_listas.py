lista1=[1,2,3,4,5]
lista2=[1,2,6,7,8,9,10]
def compara(lista1,lista2):
    global comun
    comun=[]
    for i in lista1:
        for y in lista2:
            if i==y:
                comun.append(i)
    if len(comun)>=1:
        conf=True
    else:
        conf=False
    return conf

print(compara(lista1,lista2))
print(comun)

