import pandas as pd
df = pd.read_csv(r'C:\ALBERTO\Personales\ISTQB\Python\Ejercicios\population.csv')
#a=df[df["District"]=="Texas"]
#print("\n")
#print(df[df.District=="Illinois"])
print(df[(df["District"]=="Texas") | (df["Name"]=="Dallas") ][["Name", "District"]])



