import io
archivo = open("archivos_planos\kilo.txt", "r") 
#contenido = archivo.read()
#contenido.seek(11)
archivo.seek(8)
print(archivo.read(5))