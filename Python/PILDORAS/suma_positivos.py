print("Programa para sumar números positivos \n")
salida=False
suma=0
#num1=int(input("Digite número positivo: "))
while salida==False:
    #print(num1) 
    num1=int(input("Digite número positivo: "))
    if num1<0:
        salida=True
    else:
        suma=suma+num1
print("La suma de los números positivos digitados es ",suma) 

    