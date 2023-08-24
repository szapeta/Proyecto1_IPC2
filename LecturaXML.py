import xml.etree.ElementTree as ET
from ListaSimple import ListaSimple
from  Senal import Senal
from Pila import Pila
import copy

class LecturaXML():
    def __init__(self, path):
        self.raiz = ET.parse(path).getroot()
        self.pila = Pila()

    def getSenal(self):
        listSenales = ListaSimple()
        for senal in self.raiz.findall('senal'):
           nombreSenal = senal.get('nombre')
           tiempoMaximo = senal.get('t')
           amplitudMaxima = senal.get('A')
           tmpSenal = Senal(nombreSenal, tiempoMaximo, amplitudMaxima)


        print("_____Lista de senales_____")
        senalGuardada = listSenales.getInicio()
        while senalGuardada != None:
            print(senalGuardada.getDato().getNombre())
            senalGuardada = senalGuardada.getSiguiente()

    def getDatos(self):
        for senal in self.raiz.findall('senal'):
            for dato in senal.findall('dato'):
                self.pila.push(int(dato.text))

        pilaBinaria = copy.deepcopy(self.pila)
        pilaBinaria.convertirABinario()
        pilaBinaria.graficar('pilaBinaria')
        self.pila.graficar('pila')


objLectura = LecturaXML('entrada.xml')
#objLectura.getSenal()
objLectura.getDatos()
