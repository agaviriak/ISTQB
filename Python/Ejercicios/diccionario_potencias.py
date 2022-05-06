def potencias():
    dic={}
    entrada=int(input("Digite numnero: "))
    for i in range(1,entrada+1,2):
        dic[i]=i**4
    print(dic)

potencias()
