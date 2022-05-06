equipo1 =["América de Cali",
         "Juan Cruz Real",
         "Juan Pablo Segovia",
         "Joel Graterol",
         "Marlon Torres",
         "Edwin Velasco",
         "Cristian Arrieta",
         "Jefferson Murillo",
         "Héctor Quiñones",
         "Carlos Sierra",
         "Juan Camilo Mesa",
         "Felipe Jaramillo",
         "Yesus Cabrera",
         "Rafael Carrascal",
         "Juan David Pérez",
         "Duván Vergara",
         "Adrian Ramos",
         ["Millonarios", "Atlético Nacional", "Deportivo Cali", "Jaguares"],
         3,
         1,
         0
         ]
equipo2 = [ "Deportivo Cali",
         "Alfredo Arias",
         "Juan Camilo Angulo",
         "Johan Wallens",
         "Kevin Moreno",
         "Jhon Vásquez",
         ["Millonarios", "Tolima",  "Jaguares", "América de Cali"],
         1,
         2,
         0
        ]

def procesar_equipo(L):
    dic={}
    largo=(len(L))
    dic['equipo_nombre']=(L[0])
    dic['equipo_entrenador']=(L[1])
    dic['equipo_capitan']=(L[2])
    jugadores=[]
    for i in range(3,len(L)-4):
        jugadores.append(L[i])
    dic['equipo_jugadores']=jugadores
    dic['partidos_jugados']=(L[largo-4])
    dic['partidos_ganados']=(L[largo-3])
    dic['partidos_perdidos']=(L[largo-2])
    dic['partidos_empatados']=(L[largo-1])
    cta_partidos=len(L[largo-4])
    sum_partidos=(L[largo-3])+(L[largo-2])+(L[largo-1])
    if cta_partidos==sum_partidos:
        dic['datos_correctos']=True
    else:
        dic['datos_correctos']=False
    return dic
    raise NotImplementedError()

def comparar_equipos(D1,D2):
    dic_resumen={}
    puntaje1=(D1['partidos_ganados']*3)+(D1['partidos_empatados']*1)
    puntaje2=(D2['partidos_ganados']*3)+(D2['partidos_empatados']*1)
    if puntaje1>puntaje2:
        dic_resumen['mejor_puntaje']=((D1['equipo_nombre']),puntaje1)
        dic_resumen['peor_puntaje']=((D2['equipo_nombre']),puntaje2)
    else:
        dic_resumen['mejor_puntaje']=((D2['equipo_nombre']),puntaje2)
        dic_resumen['peor_puntaje']=((D1['equipo_nombre']),puntaje1)

    jugados1= len(D1['partidos_jugados'])
    jugados2= len(D2['partidos_jugados'])
    if jugados1>jugados2:
        dic_resumen['mas_partidos_jugados']=(D1['equipo_nombre'])
    elif jugados1<jugados2:
        dic_resumen['mas_partidos_jugados']=(D2['equipo_nombre'])
    else:
        dic_resumen['mas_partidos_jugados']="Igual"
    
    ganados1=D1['partidos_ganados']
    ganados2=D2['partidos_ganados']
    if ganados1>ganados2:
        dic_resumen['mas_ganados']=(D1['equipo_nombre'])
    elif ganados1<ganados2:
        dic_resumen['mas_ganados']=(D2['equipo_nombre'])
    else:
        dic_resumen['mas_ganados']="Igual"

    perdidos1=D1['partidos_perdidos']
    perdidos2=D2['partidos_perdidos']
    if perdidos1>perdidos2:
        dic_resumen['mas_perdidos']=(D1['equipo_nombre'])
    elif perdidos1<perdidos2:
        dic_resumen['mas_perdidos']=(D2['equipo_nombre'])
    else:
        dic_resumen['mas_perdidos']="Igual"

    empatados1=D1['partidos_empatados']
    empatados2=D2['partidos_empatados']
    if empatados1>empatados2:
        dic_resumen['mas_empatados']=(D1['equipo_nombre'])
    elif empatados1<empatados2:
        dic_resumen['mas_empatados']=(D2['equipo_nombre'])
    else:
        dic_resumen['mas_empatados']="Igual"

    error1=D1['datos_correctos']
    error2=D2['datos_correctos']
    if (error1==True or error2==True):
        dic_resumen['posible_error']=True
    else:
        dic_resumen['posible_error']=False

    return dic_resumen

print(comparar_equipos(procesar_equipo(equipo1),procesar_equipo(equipo2)))

