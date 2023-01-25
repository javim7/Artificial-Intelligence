from abc import ABC, abstractmethod

class Framework(ABC):
    def __init__(self, matriz, inicial, finales, caminables):
        self.inicial = inicial
        self.finales = finales
        self.caminables = caminables
        self.matriz = matriz
        self.visitados = []
        self.camino = []
        self.fronteras = []
        self.fronteras.append(inicial)
        # self.visitados.append(inicial)
    
    @abstractmethod
    def actions(self, estado):
        return self.matriz.get_actions(estado)

    @abstractmethod
    def result(self, estado, accion):
        return self.matriz.get_result(estado, accion)

    @abstractmethod
    def goal_test(self, estado):
        return estado == self.sestadoFinales

    @abstractmethod
    def path_cost(self, matriz):
        costo = 0
        for i in range(len(matriz)-1):
            costo += self.stepCost(matriz[i], matriz[i+1])
        return costo

    @abstractmethod
    def stepCost(self, estado, accion, estado2):
       return self.matriz.get_step_cost(estado, accion)
