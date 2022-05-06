#IMPORTO LIBRERIAS y SETEO OBJETO CON CONEXION GITHUB (MEDIANTE TOKEN)
import pandas as pd
from github import Github
g=Github("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")

#REPOSITORIOS DE MEETUP y LLENADO DEL DATAFRAME
print("\n Obteniendo datos de Github.  Espere un momento por favor.....\n")
repos_m= g.search_repositories(query="org:meetup")
registro=  {'Nombre_Rep': [], 'Estrellas': [], 
            'Bifurcaciones': [], 'Seguidores': []}
df_repo = pd.DataFrame(data=registro)
#llenado del dataframe df_repo
for i in repos_m:
    new_registro= {'Nombre_Rep': [i.full_name], 'Estrellas': [i.stargazers_count],
    'Bifurcaciones': [i.forks_count], 'Seguidores': [i.subscribers_count]}
    df_repo = df_repo.append(new_registro, ignore_index=True)


    repo_name = 'meetup/mwp-cli'
    repo = g.get_repo(repo_name)
    contributors = repo.get_contributors()
    #for i in contributors:
    #    print(i.login)
    #    print(i.contributions)


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

#MENU PARA ELEGIR LAS DIFERENTES OPCIONES
opc=0
while opc != 8:
    print("\n***** MENU DE OPCIONES *****\n")
    print("1. Listar todos los repositorios")
    print("2. Listar los 3 repositorios con mas estrellas")
    print("3. Listar los 3 repositorios con mas bifurcaciones")
    print("4. Listar los 3 repositorios con mas seguidores")
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
    else:
        print("Entrada inválida")
    
        

