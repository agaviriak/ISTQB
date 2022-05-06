from github import Github
g=Github("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")
#repos_n= g.search_repositories(query="Language:phyton")
#repos_n= g.search_repositories(query="user:defunkt")
#repos_n= g.search_repositories(query="org:bradtraversy")
repos_n= g.search_repositories(query="user:defunkt forks:>100 followers:>50 stars:>2")
repos_s= g.search_repositories(query="user:meetup")

lista=repos_n.get_page

for i in repos_n:
    print(i)
    print(i.stargazers_count) #Stars
    print(i.forks_count) #Bifurcaciones
    print(i.full_name)
    print(i.subscribers_count)  #watchers
    print(i.open_issues_count)

print(lista)

    



 