micadena="aaaaaAAA"
def num_caracteres(cadena):
    dic={}
    for i in cadena:
        c=0
        for y in cadena:
            if i==y:
                c=c+1
        dic[i]=c
    return dic

print(num_caracteres(micadena))

