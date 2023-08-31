from ListaSimple import ListaSimple

class Cola(ListaSimple):

    def enconlar(self, dato):
        ListaSimple.agregarInicio(self, dato)

    def desencolar(self):
        ListaSimple.eliminarFinal(self)

    def graficar(self, nombre="cola"):
        ListaSimple.graficar(self, nombre, "LR")