import graphviz

class Graph():
    def __init__(self, nombreArchivo):
        self.nombreArchivo = nombreArchivo
        self.dot = graphviz.Digraph('structs', filename=f'{self.nombreArchivo}.gv', node_attr={'shape': 'record', 'fontname':'Helvetica'})    

    def add(self, nodoInicio, nodoSiguiente):
        if(nodoSiguiente != None):
            self.dot.node(str(nodoInicio.getId()), str(nodoInicio.getDato()))
            self.dot.node(str(nodoSiguiente.getId()), str(nodoSiguiente.getDato()))
            self.dot.edge(str(nodoInicio.getId()), str(nodoSiguiente.getId()))

    def generar(self):
       self.dot.render(outfile=f'img/{self.nombreArchivo}.png').replace('\\', '/')
       f'img/{self.nombreArchivo}.png' 
