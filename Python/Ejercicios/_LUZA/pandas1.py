import pandas as pd # Librería que nos permitirá cargar los datos fácilmente
import numpy as np

data = pd.read_json('C:/ALBERTO/Personales/ISTQB/Python/Ejercicios/_LUZA/cancer-data.json')  
print(data["diagnosis"].unique())
mascara1 = (data["diagnosis"] == "desconocido")
data=data[~mascara1]
mascara2 = (data["diagnosis"]=="igno")
data=data[~mascara2]
data["diagnosis"] = data["diagnosis"].str.replace("Ben","B")
data["diagnosis"] = data["diagnosis"].str.replace("Mal","M")
data["diagnosis"] = data["diagnosis"].str.replace("Mlig","M")
print(data["diagnosis"].unique())