from Nodo import Nodo
from Graph import Graph

class ListaSimple():
    id = 0
    def __init__(self):
        self.nodoInicio = None
        self.nodoFinal = None
        self.size = 0

    def getInicio(self):
        return self.nodoInicio

    def estaVacia(self):
        return self.nodoInicio == None
        #return self.size == 0

    def agregarFinal(self, dato):
        nuevo = Nodo(self.id, dato)
        self.id += 1
        if self.estaVacia():
            self.nodoInicio = nuevo
            self.nodoFinal = nuevo
        else:
            self.nodoFinal.setSiguiente(nuevo)
            self.nodoFinal = nuevo
        self.size += 1

    def agregarInicio(self, dato):
        nuevo = Nodo(self.id, dato)
        self.id += 1
        if self.estaVacia():
            self.nodoInicio = nuevo
            self.nodoFinal = nuevo
        else:
            nuevo.setSiguiente(self.nodoInicio)
            self.nodoInicio = nuevo
        self.size += 1

    def agregarEnOrden(self, dato):
        nuevo = Nodo(self.id, dato)
        self.id += 1
        if self.estaVacia():
            self.nodoInicio = nuevo
            self.nodoFinal = nuevo
        elif dato < self.nodoInicio.getDato():
            nuevo.setSiguiente(self.nodoInicio)
            self.nodoInicio = nuevo
        elif dato > self.nodoFinal.getDato():
            self.nodoFinal.setSiguiente(nuevo)
            self.nodoFinal = nuevo
        else:
            tmp = self.nodoInicio
            while tmp.getSiguiente().getDato() < dato:
                tmp = tmp.getSiguiente()
            nuevo.setSiguiente(tmp.getSiguiente())
            tmp.setSiguiente(nuevo)
        self.size += 1

    def eliminarInicio(self):
        if not self.estaVacia():
            if self.nodoInicio == self.nodoFinal: #solo hay un elemento
                self.nodoInicio = None
                self.nodoFinal = None
            else:
                self.nodoInicio = self.nodoInicio.getSiguiente()
            self.size -= 1
         

    def eliminarFinal(self):
        if not self.estaVacia():
            if self.nodoInicio == self.nodoFinal:
                self.nodoInicio = None
                self.nodoFinal = None
            else:
                tmp = self.nodoInicio
                while tmp.getSiguiente() != self.nodoFinal:
                    tmp = tmp.getSiguiente()
                tmp.setSiguiente(None)
                self.nodoFinal = tmp
            self.size -= 1

    def imprimir(self):
        tmp = self.nodoInicio
        while tmp != None:
            print(tmp.getDato())
            tmp = tmp.getSiguiente()

    def graficar(self, nombreArchivo, direccion="TB"):
        graph = Graph(nombreArchivo, direccion)
        tmp = self.nodoInicio
        while tmp != None:
            graph.add(tmp, tmp.getSiguiente())
            tmp = tmp.getSiguiente()
        graph.generar()

    def convertirABinario(self):
        tmp = self.nodoInicio
        while tmp != None:
            if(int(tmp.getDato())>=1):
                tmp.setDato(1)
            tmp = tmp.getSiguiente()

        