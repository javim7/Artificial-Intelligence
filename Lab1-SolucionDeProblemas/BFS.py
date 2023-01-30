from framework import *

class BFS(Framework):
    def __init__(self, matriz, inicial, finales, caminables):
        super().__init__(matriz, inicial, finales, caminables)
        self.final = None

    def actions(self, estado):
        i, j = estado
        
        moves = []
        
        if ((i+1,j) in self.caminables):
            moves.append((i+1,j))
        if ((i,j-1) in self.caminables):
            moves.append((i,j-1))
        if ((i-1,j) in self.caminables):
            moves.append((i-1,j))
        if ((i,j+1) in self.caminables):
            moves.append((i,j+1))
        
        return moves

    def result(self, estado, accion):
        return accion

    def goal_test(self, estado):
        return estado in self.finales

    def stepCost(self, estado, accion, estado2):
        pass

    def path_cost(self, matriz):
        pass

    def bfs(self):
        fronteras = self.fronteras.copy()
        visitados = self.visitados.copy()
        path = {}

        while True:
            if len(fronteras):

                popeado = fronteras.pop(0)
                if popeado not in visitados:
                    visitados.append(popeado)
                visitados.append(popeado)        
                estado = visitados[-1]

                if self.goal_test(estado):
                    return self.pathRecorrido(path, estado)

                acciones = self.actions(estado)
                for a in acciones:
                    if a not in visitados:
                        fronteras.append(a)
                        visitados.append(a)
                        path[a] = popeado
            else:
                return False

    def pathRecorrido(self, diccionario, estado):
        path = {}
        pos = []
        pathF = self.pathFinal.copy()

        while estado != self.inicial:
            path[diccionario[estado]] = estado
            estado = diccionario[estado]
        
        for llave,valor in path.items():
            pos.append(valor)
        pathF.append(pos)
        return pathF[0]
            
