#IMPORTO LIBRERIAS y SETEO OBJETO CON CONEXION GITHUB (MEDIANTE TOKEN)
import pandas as pd
import numpy as np
from github import Github
g=Github("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")
pd.set_option("max_rows", None)
#REPOSITORIOS DE MEETUP y LLENADO DEL DATAFRAME
print("\n...Obteniendo datos de Github.  Espere un momento por favor.....\n")
#repos_m= g.search_repositories(query="org:meetup")
#repos_m= g.search_repositories(query="user:defunkt")
repos_m=g.search_repositories(query="user:defunkt followers:>600")
registro_repo=  {'Nombre_Rep': [], 'Estrellas': [],'Bifurcaciones': [], 'Seguidores': [],}
registro_cont=  {'Contribuidor': [], 'Contribuciones': [],
                'Nombre_Rep': [], 'Estrellas': [],'Bifurcaciones': [], 'Seguidores': []}
df_repo = pd.DataFrame(data=registro_repo)
df_cont = pd.DataFrame(data=registro_cont)
#llenado del dataframe df_repo
for i in repos_m:
    new_repo= {'Nombre_Rep': i.full_name, 'Estrellas': i.stargazers_count,
    'Bifurcaciones': i.forks_count, 'Seguidores': i.subscribers_count}
    df_repo = df_repo.append(new_repo, ignore_index=True)

    #repo_name = 'meetup/mwp-cli'
    print(i.full_name)
    repo_each = g.get_repo(i.full_name)
    contributors = repo_each.get_contributors()
    for y in contributors:
        print(y.login)
        print(y.contributions)
        new_cont= {'Contribuidor': y.login, 'Contribuciones': y.contributions,
        'Nombre_Rep': i.full_name, 'Estrellas': i.stargazers_count,
        'Bifurcaciones': i.forks_count, 'Seguidores': i.subscribers_count}
        df_cont = df_cont.append(new_cont, ignore_index=True)

#FUNCIONES DE IMPRESION DE OPCIONES
def imprime_todo():
    print(df_repo.iloc[:,:])
    print("")
def imprime_estrellas():
    print(df_repo.sort_values(by=["Estrellas"], ascending=False).iloc[0:3,[0,1]])
    print("")
def imprime_bifuracaciones():
    print(df_repo.sort_values(by=["Bifurcaciones"], ascending=False).iloc[0:3,[0,2]])
    print("")
def imprime_seguidores():
    print(df_repo.sort_values(by=["Seguidores"], ascending=False).iloc[0:3,[0,3]])
    print("")
def imprime_contribuciones():
    print(df_cont.sort_values(by=['Contribuciones'], ascending=False).iloc[:,[0,1,2]])
    #print(df_cont.groupby(['Contribuidor'])['Contribuciones'].sum())
def imprime_contribuyentes():
    #print(df_cont.sort_values(by=['Contribuciones'], ascending=False).iloc[:,[0,1,2]])
    #print(df_cont.groupby(['Contribuidor']))
    kilo=(df_cont.sort_values(by=['Contribuciones'], ascending=False).iloc[:,0])
    print(kilo.drop_duplicates().sort_values())
    #print(kilo)


opc=0
while opc != 8:
    print("\n***** MENU DE OPCIONES *****\n")
    print("1. Listar todos los repositorios")
    print("2. Listar los 3 repositorios con mas estrellas")
    print("3. Listar los 3 repositorios con mas bifurcaciones")
    print("4. Listar los 3 repositorios con mas seguidores")
    print("5. Listar Contribuciones por repositorios")
    print("6. Listar Contribuyentes únicos")
    print("8. Salir\n")
    opc=int(input("Digite la opción deseada: "))
    if opc==1:
        imprime_todo()
        input("Presione una tecla para continuar....")
    elif opc==2:
        imprime_estrellas()
        input("Presione una tecla para continuar....")
    elif opc==3:
        imprime_bifuracaciones()
        input("Presione una tecla para continuar....")
    elif opc==4:
        imprime_seguidores()
        input("Presione una tecla para continuar....")
    elif opc==5:
        imprime_contribuciones()
        input("Presione una tecla para continuar....")
    elif opc==6:
        imprime_contribuyentes()
        input("Presione una tecla para continuar....")
    else:
        print("\n\n***********Entrada inválida*************\n")
        input("Presione una tecla para continuar....")
    
        

