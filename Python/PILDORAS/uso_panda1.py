#uso de dataframe & API jason
import pandas as pd
import requests
json_covid=requests.get("https://services.arcgis.com/BQTQBNBsmxjF8vus/ArcGIS/rest/services/Colombia_COVID19V/FeatureServer/6/query?where=1%3D1&outFields=*&outSR=4326&f=json").json()
datos_covid=pd.DataFrame.from_dict(json_covid["features"])
print(datos_covid,sep=":")
p=datos_covid.to_csv