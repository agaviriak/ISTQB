class Persona():
    def __init__(self,nombre,cc,ciudad):
        self.nombre=nombre
        self.cc=cc
        self.ciudad=ciudad
    def mostrar_persona(self):
        print("Nombre: ", self.nombre)
        print("cc: ", self.cc)
        print("ciudad: ", self.ciudad)
            
alberto=Persona("Alberto","1234","Cali")
alberto.mostrar_persona()
print("-------------------------------------------")   
class Empleado(Persona):
    def __init__(self,nombre,cc,ciudad,salario,cargo):
        super().__init__(nombre,cc,ciudad)
        self.salario=salario
        self.cargo=cargo

    def mostrar_empleado(self):
        super().mostrar_persona()
        print("Salario: ",self.salario)
        print("Cargo: ",self.cargo)

empleado1=Empleado("Antonio","344444","Cali",2500,"gerente")
empleado1.mostrar_empleado()
print(isinstance(alberto, Empleado))
