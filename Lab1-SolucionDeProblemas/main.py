from BFS import *
from BFS import *
from AStar import *
from reader import *
from framework import *
from laberinto import *
import networkx as nx
import matplotlib.pyplot as plt

reader = Reader("./laberintos/lab1.bmp")

reader.imageReader()
matriz = reader.matriz
# print(matriz)

laberinto = Laberinto(matriz)
inicial = laberinto.estadoInicial()
finales = laberinto.estadosFinales()
caminables = laberinto.getCaminables()
# grafo = laberinto.crearGrafo()

# print(inicial)
# print(finales)
# print(caminables)
# print(grafo)
# print(list(grafo.adj[(18,2)]))

bfs = BFS(matriz, inicial, finales, caminables)
bfs.bfs()

