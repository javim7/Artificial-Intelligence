from BFS import *
from DFS import *
from AStar import *
from reader import *
from resultado import *
from framework import *
from laberinto import *


'''
algoritmo BFS y dibujando el resultado
'''
def bfsAlgorithm(path, matriz, inicial, finales, caminables):
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
def dfsAlgorithm(path, matriz, inicial, finales, caminables):
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
# algoritmo A* con manhattan y dibujando el resultado
# '''
def aManhattan(path, matriz, inicial, finales, caminables):
    reader = Reader(path)
    reader.imageReader()
    matriz = reader.matriz

    astar = AStar(matriz, inicial, finales, caminables)
    celdas = astar.matrizACeldas(matriz) #definiendo diccionario de celdas
    astar.inicialFinal(celdas) # inicial y finales
    pathAStar = astar.AStarM()

    resultadoAStar = Resultado(matriz, pathAStar)
    matrizAStar = resultadoAStar.marcarPath()
    filename = resultadoAStar.filename(path, 'A_Manhattan')
    resultadoAStar.dibujarFinal(matrizAStar, filename)

# '''
# algoritmo A* con euclidean y dibujando el resultado
# '''
def aEuclidean(path, matriz, inicial, finales, caminables):
    reader = Reader(path)
    reader.imageReader()
    matriz = reader.matriz

    astar = AStar(matriz, inicial, finales, caminables)
    celdas = astar.matrizACeldas(matriz) #definiendo diccionario de celdas
    astar.inicialFinal(celdas) # inicial y finales
    pathAStar = astar.AStarE()

    resultadoAStar = Resultado(matriz, pathAStar)
    matrizAStar = resultadoAStar.marcarPath()
    filename = resultadoAStar.filename(path, 'A_Euclidean')
    resultadoAStar.dibujarFinal(matrizAStar, filename)

def main():
    print("\n----Lab 1: Solucion de Problemas----")
    path = input("\nIngrese la ruta del laberinto (ej: lab1): ")
    path = "./laberintos/" + path + ".bmp"
    menu(path)

def menu(path):
    '''
    obteniendo la matriz
    '''
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

    while True:
        print("\n----Menu----")
        print("[1] BFS")
        print("[2] DFS")
        print("[3] A*")
        print("[4] Salir")
        opcion = int(input("Opcion -> "))
        if opcion in [1,2,3,4]:
            if opcion == 1:
                bfsAlgorithm(path, matriz, inicial, finales, caminables)
                print("\nRuta encontrada, ir a la carpeta resultados para ver solucion!")
            elif opcion == 2:
                dfsAlgorithm(path, matriz, inicial, finales, caminables)
                print("\nRuta encontrada, ir a la carpeta resultados para ver solucion!")
            elif opcion == 3:
                while True:
                    print("\n----Menu A*----")
                    print("[1] Manhattan")
                    print("[2] Euclidean")
                    opcion = int(input("Opcion -> "))
                    if opcion in [1,2]:
                        if opcion == 1:
                            aManhattan(path, matriz, inicial, finales, caminables)
                            print("\nRuta encontrada, ir a la carpeta resultados para ver solucion!")
                            break
                        elif opcion == 2:
                            aEuclidean(path, matriz, inicial, finales, caminables)
                            print("\nRuta encontrada, ir a la carpeta resultados para ver solucion!")
                            break
              
            elif opcion == 4:
                print("Salir")
                exit()

if __name__ == '__main__':
    main()