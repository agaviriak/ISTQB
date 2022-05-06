import pandas as pd
df = pd.read_csv("C:\ALBERTO\Personales\ISTQB\_archivos\Vehiculos.csv", sep=',')
#mas3=df[df.Nota.notnull()]
#mas3=df[df.Nota.isnull()]
#mas3=df[df.Nota<4]
#mas3=df[df.Nota.isin([2.7,4.0])]
#mas3=df[~df.Nota.isin([2.7,4.0])]
#mas3=df[(df.Materia=="matematicas") & (df.Nota<=3.8)]
#mas3=df.query("Materia=='matematicas' & Nota<=4.8 & Nombre.str.endswith('o')")
#mas3=df.query("Materia=='matematicas' & Nota<=4.8 & Nombre.str.startswith('Al')")
#mas3=df.query("Materia=='matematicas' & Nota<=4.8 & Nombre.str.startswith('Al')")
#print(mas3[['Nombre','Nota']])
print(df)