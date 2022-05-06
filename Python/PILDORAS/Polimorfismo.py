class Apartaestudio():
    def caracteristica(self):
        print ("\n Soy un apartaestudio \n")

class Apartamento():
    def caracteristica(self):
        print ("\n Soy un apartamento \n")

class Casa():
    def caracteristica(self):
        print ("\n Soy una casa \n")


def constructora(inmueble):
        inmueble.caracteristica()

#propiedad=Apartamento()
constructora(Casa())

