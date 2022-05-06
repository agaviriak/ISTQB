def suma(lista):
    acum_s=0
    for i in lista:
        acum_s=acum_s+i
    return acum_s
def multiplica(lista):
    acum_m=1
    for i in lista:
        acum_m=acum_m*i
    return acum_m

mylista=[1,2,3,4]
print(suma(mylista))
print(multiplica(mylista))