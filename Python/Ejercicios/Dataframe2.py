import pandas as pd
df = pd.read_csv("C:/ALBERTO\Personales/ISTQB/_archivos/Vehiculos.csv", sep=',')
#print(df.query("Sunroof=='NO' & Wheel_Drive=='YES' and Type=='SUV'"))
print(df.drop_duplicates(subset='Customer', keep='last').query("Sunroof=='YES'"))
new_excel=pd.ExcelWriter("C:/ALBERTO\Personales/ISTQB/_archivos/myexcel.xlsx")
df.to_excel(new_excel,"HojaDatos")
new_excel.save()