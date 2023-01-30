import networkx as nx

class Laberinto():
    def __init__(self, matriz):
        self.matriz = matriz
        self.inicial = None
        self.finales = []
        self.caminables = []
        self.grafo = nx.Graph()

    def estadoInicial(self):
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                if self.matriz[i][j] == 2:
                    self.inicial = (i,j)
        return self.inicial
    
    def estadosFinales(self):
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                if self.matriz[i][j] == 3:
                    self.finales.append((i,j))
        return self.finales

    def getCaminables(self):
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                if self.matriz[i][j] == 1 or self.matriz[i][j] == 2 or self.matriz[i][j] == 3:
                    self.caminables.append((i,j))
        return self.caminables

    def crearGrafo(self):
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                if self.matriz[i][j] == 1 or self.matriz[i][j] == 2 or self.matriz[i][j] == 3:
                    self.grafo.add_node((i,j))
                    try:
                        if self.matriz[i][j+1] == 1:
                            self.grafo.add_edge((i,j),(i,j+1))
                    except:
                        pass
                    try:
                        if self.matriz[i][j-1] == 1:
                            self.grafo.add_edge((i,j),(i,j-1))
                    except:
                        pass
                    try:
                        if self.matriz[i+1][j] == 1:
                            self.grafo.add_edge((i,j),(i+1,j))
                    except:
                        pass
                    try:
                        if self.matriz[i-1][j] == 1:
                            self.grafo.add_edge((i,j),(i-1,j))
                    except:
                        pass
        return self.grafo