#Se define la clase
canalN=1
print(canalN)
class Televisor():
    #crear método constructor
    def __init__(self):
        #Caracteristicas o propiedades
        self.__serial=""
        self.__marca=""
        self.__tamaño=""
        self.__smarttv=""
        self.encendido=False
        self.volume=""
        self.canal=""
    #cierre método constructor
    #Métodos o acciones
    def inventariar(self):
        self.__serial=input("Digite serial del Televisor: ")
        self.__marca=input("Digite marca del Televisor: ")
        self.__tamaño=input("Digite tamaño del Televisor en pulagadas: ")
        self.__smarttv=input("El Televisor es smarttv ? (Y/N) : ")
    def apagar(self):
        self.encendido=False
        self.canal=""
        self.volume=""
    def encender(self):
        self.encendido=True
        self.canal=canalN
    def cambiar_volume(self):
        vol=int(input("Digite volume requerido: "))
        if vol>=0:
            self.volume=vol
        else:
            print("El valor debe ser numérico")
    def cambiar_canal(self):
        canalN=input("digite canal requerido: ")
        self.canal=canalN
    def mostrar_info(self):
        print("Serial: ",self.__serial)
        print("Marca: ",self.__marca)
        print("Tamaño: ",self.__tamaño)
        print("Smart-tv?:", self.__smarttv)
    def mostrar_estado(self):
        print("Encendido: ",self.encendido)
        print("Volume: ",self.volume)
        print("Canal:", self.canal)
        

#Fin Clase Televisor
#stock=[1,2]
#cont=0
tv01=Televisor()
opc=0
while opc != 8:
    print("*** MENU PRINCIPAL ***\n")
    print("1. Inventariar nuevo Televisor")
    print("2. Mostar Info del Televisor")
    print("3. Mostrar estado del Televisor")
    print("4. Apagar Televisor")
    print("5. Encender Televisor")
    print("6. Cambiar volume del Televisor")
    print("7. Cambiar canal del Televisor")
    print("8. Salir\n")
    opc=int(input("Digite la opción deseada: "))
    if opc==1:
        tv01.inventariar()
    elif opc==2:
        tv01.mostrar_info()
        input("Presione una tecla para continuar....")
    elif opc==3:
        tv01.mostrar_estado()
        input("Presione una tecla para continuar....")
    elif opc==4:
        tv01.apagar()
    elif opc==5:
        tv01.encender()
    elif opc==6:
        tv01.cambiar_volume()
    elif opc==7:
        tv01.cambiar_canal()
    else:
        print("Entrada inválida")


        


