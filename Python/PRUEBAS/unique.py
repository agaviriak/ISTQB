import pandas as pd
#import numpy as np

df_repo = pd.DataFrame({'Nombre_Rep':[1,1,1,2,2,2,7,8,9],'Estrellas':[1,1,1,1,3,4,2,6,8],
                    'Bifurcaciones':[6,4,8,7,3,4,9,6,8]})
print(df_repo)
df_repo = df_repo.append({'Nombre_Rep':22,'Estrellas':1,
                    'Bifurcaciones':66}, ignore_index=True)
print(df_repo.groupby(['Nombre_Rep'])['Estrellas'].sum())

#IMPORTO LIBRERIAS y SETEO OBJETO CON CONEXION GITHUB (MEDIANTE TOKEN)
from github import Github
g=Github("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")

#REPOSITORIOS DE MEETUP y LLENADO DEL DATAFRAME
print("\n...Obteniendo datos de Github.  Espere un momento por favor.....\n")
repos_m=g.search_repositories(query="user:defunkt followers:>600")
registro_repo=  {'Nombre_Rep': [], 'Estrellas': [],'Bifurcaciones': [], 'Seguidores': [],}
df_repo = pd.DataFrame(data=registro_repo)
#llenado del dataframe df_repo
for i in repos_m:
    new_repo= {'Nombre_Rep': i.full_name, 'Estrellas': i.stargazers_count,
    'Bifurcaciones': i.forks_count, 'Seguidores': i.subscribers_count}
    df_repo = df_repo.append(new_repo, ignore_index=True)
    print(i.full_name)

print(df_repo)    
print(df_repo.groupby(['Nombre_Rep'])['Estrellas'].sum())