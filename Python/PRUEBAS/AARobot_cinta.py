def solve(weight_0, weight_1, weight_2):
    arreglo=[weight_0,weight_1,weight_2]
    maximo=max(arreglo)
    if maximo==weight_0:
        return 0
    elif maximo==weight_1:
        return 1
    else: 
        return 2
    
    #return maximo
print(solve(195,18,500))    