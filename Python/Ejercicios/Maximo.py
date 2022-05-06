def Maximo(num1, num2):
    if num1>num2:
        Nmax=num1
    elif num2>num1:
        Nmax=num2
    else:
        Nmax="Los números son iguales"
    return Nmax

print(Maximo(16,16))