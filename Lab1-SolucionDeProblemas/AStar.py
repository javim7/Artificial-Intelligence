from framework import *
from celda import *
import math

class AStar(Framework):
    def __init__(self, matriz, inicial, finales, caminables):
        super().__init__(matriz, inicial, finales, caminables)
        self.final = None
        self.celdas = {}
        self.opened = []
        self.closed = []

    def inicialFinal(self, dic):
        self.finales = []
        for key, value in dic.items():
            if value.color == 2:
                self.inicial = value
            if value.color == 3:
                self.finales.append(value)

    def matrizACeldas(self, matriz):
        celdas = {}
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                celdas[(i,j)] = Celda((i,j), matriz[i][j])
        self.celdas = celdas
        return self.celdas

    def manhattanHeuristic(self, celda):
        i, j = celda.pos
        x, y = self.finales[0].pos
        return abs(i-x) + abs(j-y)

    def euclideanHeuristic(self, celda):
        i, j = celda.pos
        x, y = self.finales[0].pos
        return math.sqrt((i-x)**2 + (j-y)**2)

    def gCost(self, celda):
        i, j = celda.pos
        x, y = self.inicial.pos
        if abs(i-x) != 0:
            return abs(i-x)
        else:
            return abs(j-y)
    
    def fMenor(self, opened):
        menor = opened[0]
        for celda in opened:
            if celda.f < menor.f:
                menor = celda
        return menor

    def actions(self, estado):
        pos = estado.pos
        i, j = pos
        
        moves = []
        
        for key, value in self.celdas.items():
            if value.pos == (i,j+1) and value.color != 0:
                moves.append(value)
            if value.pos == (i,j-1) and value.color != 0:
                moves.append(value)
            if value.pos == (i+1,j) and value.color != 0:
                moves.append(value)
            if value.pos == (i-1,j) and value.color != 0:
                moves.append(value)
        
        return moves

    def result(self, estado, accion):
        return accion

    def goal_test(self, estado):
        return estado in self.finales

    def stepCost(self, estado, accion, estado2):
        return 1

    def path_cost(self, matriz):
        pass

    def AStarM(self):
        self.opened.append(self.inicial)

        x = 0
        while True:
            x+=1
            if self.opened:
                q = self.fMenor(self.opened)
                # print("estado", q.pos)
                self.opened.remove(q)
                q.g = self.gCost(q)
                # print("q.g ",q.g)

                if self.goal_test(q):
                     return self.pathRecorrido(q)

                acciones = self.actions(q)
                for a in acciones:
                    if a in self.closed:
                        continue
                    if a not in self.opened:
                        self.opened.append(a)
                        a.g = self.gCost(a) + q.g
                        # print("a.g ",a.g)
                        a.h = self.manhattanHeuristic(a)
                        a.f = a.g + a.h
                        a.parent = q
                self.closed.append(q)
                # print("opened", self.opened)
                # print("closed", self.closed)

            else:
                False

    def AStarE(self):
        self.opened.append(self.inicial)

        x = 0
        while True:
            x+=1
            if self.opened:
                q = self.fMenor(self.opened)
                # print("estado", q.pos)
                self.opened.remove(q)
                q.g = self.gCost(q)
                # print("q.g ",q.g)

                if self.goal_test(q):
                     return self.pathRecorrido(q)

                acciones = self.actions(q)
                for a in acciones:
                    if a in self.closed:
                        continue
                    if a not in self.opened:
                        self.opened.append(a)
                        a.g = self.gCost(a) + q.g
                        # print("a.g ",a.g)
                        a.h = self.euclideanHeuristic(a)
                        a.f = a.g + a.h
                        a.parent = q
                self.closed.append(q)
                # print("opened", self.opened)
                # print("closed", self.closed)

            else:
                False

    def pathRecorrido(self, estado):
        path = []
        pathF = []
        while estado.parent:
            path.append(estado)
            estado = estado.parent
        for celda in path:
            pathF.append(celda.pos)
        return pathF
       