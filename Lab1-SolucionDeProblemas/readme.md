# Nombre
### Laboratorio 1: Solucion de problemas

# Descripcion
#### Descripcion general
El programa recibe una imagen cuadrada como entrada, la cual representa un laberinto. Con dicha imagen, el programa debe de dibujar la solucion de este laberinto. Para esto, se deben de completar 4 tasks.

#### Restricciones a considerar
- Las dimensiones de entrada podrán variar entre ejecuciones (pero siempre será una imagen cuadrada)
- Las áreas blancas representan caminos libres
- Las áreas negras representan paredes sobre las cuales no se puede pasar
- Las áreas verdes representan la meta (goalTest positivos) (pueden ser varios)
- La área roja representa el punto de inicio (solo podrá haber uno

#### Tasks a completar
1. Se representa la imagen dada, de forma discreta. La cantidad de pixeles por cuadro depende del tamaño de la imagen.
2. Se usa una interfaz generica para definir el problema formal. Dicha interfaz, recibe la matriz de la imagen discreta como entrada y deduce las funciones del framework, como actions(s), result(a,s), stepCost(s,a,s'), etc.
3. Se construyen 3 de los algoritmos mas reconocidos para buscar grafos. Estos son, Breadth-First, Depth-First y A*.
4. Por ultimo, se dibujo la solucion en la matriz discreta y se crea la imagen nueva con la solucion. 

# Uso
1. Para poder correr el programa, se debe de correr el main e ingresar el path de uno de los laberintos, ej: 'lab1.bmp'.
2. Luego, se despliega un menu el cual despliega las siguientes opciones.
    1. BFS algorithm
    2. DFS algorithm
    3. A* algorithm
3. Se seleciona una de las siguientes opciones y tener en cuenta que la opcion 3 tiene dos subopciones las cuales son las huristicas. 
    1. Manhattan Heuristic
    2. Euclidean Heuristic

# Heuristicas
Para el algoritmo A*, se utilizaron dos heuristicas, Manhattan y Euclidean.
1. Manattan fue la priemra eleccion, ya que este heuristica sirve para laberintos o mapas en donde solo se puede mover en 4 direcciones; arriba, abajo, derecha e izquierda. Ya que este era el caso de los laberintos utilizados, se decidio utilizar esta heuristica.
2. Euclidean fue la segunda eleecion, esta heuristica se puede utilizare para mapas en donde se pueda mover en cualquier direccion, pero tambien es valido usarla en mapas en donde solo se pueda mover en 4 direcciones. Por lo tanto, se decidio utilizar esta heuristica en el programa.

# Autor 
### Javier Mombiela