def compute_closest_to_zero(ts):
    positivos=[]
    for i in ts:
        positivos.append(abs(i))
    minimo=min(positivos)
    #print(min(positivos))
    for i in ts:
        if minimo-(abs(i))==0:
            close_cero=i
    return close_cero        

medicion=[7,-10,13,8,-7,-8,2]
print(compute_closest_to_zero(medicion))