from ListaSimple import ListaSimple

class Pila(ListaSimple): #uso de herencia

    def push(self, dato):
        ListaSimple.agregarInicio(self, dato)
    
    def imprimir(self):
        ListaSimple.imprimir(self)

    def graficar(self, nombreArchivo):
        ListaSimple.graficar(self, nombreArchivo)

    def convertirABinario(self):
        ListaSimple.convertirABinario(self)