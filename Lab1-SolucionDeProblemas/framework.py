from abc import ABC, abstractmethod

class Framework(ABC):
    def __init__(self, matriz):
        self.estadoInicial = None
        self.matriz = matriz
    
    @abstractmethod
    def actions(self):
        pass

    @abstractmethod
    def result(self):
        pass

    @abstractmethod
    def goal_test(self):
        pass

    @abstractmethod
    def path_cost(self):
        pass

    @abstractmethod
    def stepCost(self):
        pass
