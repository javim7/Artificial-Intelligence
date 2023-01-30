from BFS import *
from DFS import *
from AStar import *
from reader import *
from resultado import *
from framework import *
from laberinto import *

'''
obteniendo la matriz
'''
path = "./laberintos/lab3.bmp"
reader = Reader(path)
reader.imageReader()
matriz = reader.matriz

'''
creando el laberinto
'''
laberinto = Laberinto(matriz)
inicial = laberinto.estadoInicial()
finales = laberinto.estadosFinales()
caminables = laberinto.getCaminables()

'''
algoritmo BFS y dibujando el resultado
'''
reader = Reader(path)
reader.imageReader()
matriz = reader.matriz

bfs = BFS(matriz, inicial, finales, caminables)
pathBFS = bfs.bfs()

resultadoBFS = Resultado(matriz, pathBFS)
matrizBFs = resultadoBFS.marcarPath()
filename = resultadoBFS.filename(path, 'BFS')
resultadoBFS.dibujarFinal(matrizBFs, filename)
'''
algoritmo DFS y dibujando el resultado
'''
reader = Reader(path)
reader.imageReader()
matriz = reader.matriz

dfs = DFS(matriz, inicial, finales, caminables)
pathDFS = dfs.dfs()

resultadoDFS = Resultado(matriz, pathDFS)
matrizDFs = resultadoDFS.marcarPath()
filename = resultadoDFS.filename(path, 'DFS')
resultadoDFS.dibujarFinal(matrizDFs, filename)

# '''
# algoritmo A* y dibujando el resultado
# '''
reader = Reader(path)
reader.imageReader()
matriz = reader.matriz

astar = AStar(matriz, inicial, finales, caminables)
celdas = astar.matrizACeldas(matriz) #definiendo diccionario de celdas
astar.inicialFinal(celdas) # inicial y finales
pathAStar = astar.AStar()

resultadoAStar = Resultado(matriz, pathAStar)
matrizAStar = resultadoAStar.marcarPath()
filename = resultadoAStar.filename(path, 'AStar')
resultadoAStar.dibujarFinal(matrizAStar, filename)
