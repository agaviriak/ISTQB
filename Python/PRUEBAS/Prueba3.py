import pandas as pd
from github import Github
g=Github("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")
repos_n= g.search_repositories(query="user:defunkt forks:>100 followers:>50 stars:>2")
#repos_n= g.search_repositories(query="org:meetup")

registro=  {'Nombre_Rep': [], 'Estrellas': [], 
            'Bifurcaciones': [], 'Seguidores': []}
df = pd.DataFrame(data=registro)

for i in repos_n:
    new_registro= {'Nombre_Rep': [i.full_name], 'Estrellas': [i.stargazers_count], 'Bifurcaciones': [i.forks_count], 'Seguidores': [i.subscribers_count]}
    df = df.append(new_registro, ignore_index=True)

 #   print(i)
  #  print(i.full_name) #Nombre
   # print(i.stargazers_count) #Stars
   # print(i.forks_count) #Bifurcaciones
   # print(i.subscribers_count) #watchers
    
print(df)
print("")
#print(df.iloc[:,[0,1]])
print(df.sort_values(by=["Estrellas"], ascending=False).iloc[0:3,[0,1]])
print("")
print(df.sort_values(by=["Bifurcaciones"], ascending=False).iloc[0:3,[0,2]])
print("")
print(df.sort_values(by=["Seguidores"], ascending=False).iloc[0:3,[0,3]])
    



 