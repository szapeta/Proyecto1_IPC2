class Amplitud:
    def __init__(self, amplitud, dato=0):
        self.amplitud = amplitud
        self.dato = dato

    def getAmplitud(self):
        return self.amplitud
    
    def getDato(self):
        return self.dato
    
    def print(self):
        print(self.amplitud, self.dato)