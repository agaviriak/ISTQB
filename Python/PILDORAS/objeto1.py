#Primero Objeto
class Avion():
    #Metodo constructor
    def __init__(self):
        self.__motores=2
        self.Fabricante="Airbus"
        self.__aerolinea="Ninguna"
        self.estado="En Angar"

    def despegar(self):
        self.estado="Volando"

    def aterrizar(self):
        self.estado="En pista"
    
    def guardar(self):
        self.estado="En Angar"

    def informar(self):
        print("motores: ",self.__motores)
        print("Fabricante: ",self.Fabricante)
        print("aerolinea: ",self.__aerolinea)
        print("Estado: ",self.estado)
    
    def cambiar_aerolinea(self):
        nueva_aero=input("Digite nombre de la nueva aerolinea: ")
        self.__aerolinea=nueva_aero


a320=Avion()
a330=Avion()
despegue=input("Quiere que el avión a320 despegue? (Y/N) : ")
if despegue=="Y":
    a320.despegar()
print("AVION A320")
a320.informar()
print("\n")
print("AVION A330")
a330.informar()
a330.cambiar_aerolinea()
a330.informar()
