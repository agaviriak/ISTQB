def invertir(algo):
    nuevo=[]
    inicio=len(algo)
    for i in range(inicio):
        nuevo.append(algo[inicio-1])
        inicio=inicio-1
    return nuevo

def invertir_ca(algo):
    nuevo_ca=""
    global palindrome
    for i in algo:
        nuevo_ca= i + nuevo_ca
    if algo==nuevo_ca:
        palindrome= True
    else:
        palindrome=False
    return nuevo_ca

mylista=["a","b",1,2,3,4,5,6,7,8,9]
mycadena="solos"
print(mycadena)
print(invertir_ca(mycadena))
print(palindrome)
print(mylista)
print(invertir(mylista))
