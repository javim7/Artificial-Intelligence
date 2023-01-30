from abc import ABC, abstractmethod

class Framework(ABC):
    def __init__(self, matriz, inicial, finales, caminables):
        self.inicial = inicial
        self.finales = finales
        self.caminables = caminables
        self.matriz = matriz
        self.camino = []
        self.visitados = [] #closed
        self.fronteras = [] #opened
        self.pathFinal = []
        self.fronteras.append(inicial)
        # self.visitados.append(inicial)
    
    @abstractmethod
    def actions(self, estado):
        pass

    @abstractmethod
    def result(self, estado, accion):
        pass

    @abstractmethod
    def goal_test(self, estado):
        pass

    @abstractmethod
    def path_cost(self, matriz):
        pass

    @abstractmethod
    def stepCost(self, estado, accion, estado2):
       pass
