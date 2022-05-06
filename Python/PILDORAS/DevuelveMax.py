print("HOLLLLAAAAAAA")    
def DevuelveMax(lista):
    maximo=max(lista)
    return maximo
 
lista1= []
for i in range(5):
    nro=int(input(f"Digite número {i+1}: "))
    lista1.append(nro)
print("")
print("El valor maximo es: ",DevuelveMax(lista1)) 
print(lista1) 
print(DevuelveMax([5,7,9]))  
  

