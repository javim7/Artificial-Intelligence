from PIL import Image, ImageDraw
import collections

class Reader():

    def __init__(self, path):
        self.path = path
        self.matriz = []

    def imageReader(self):
        # abrir la imagen
        # im = Image.open("lab1.bmp") #24 - 500
        # im = Image.open("lab2.bmp") #9
        im = Image.open(self.path) #4 - 640

        # definir el tamaño del grid
        if im.width <= 500:
            grid_width = (im.width//100)*5
        if im.width == 320:
            grid_width = (im.width//100)*3
        if im.width > 600:
            grid_width = (im.width//100)
        if im.width == 640:
            grid_width = (im.width//100)-2

        # crear una nueva imagen 
        nuevaImagen = Image.new("RGB", (im.width, im.height), (255, 255, 255))

        grid_width = self.divisible_number(im.width, grid_width)
        matriz = [[0 for _ in range(im.width//grid_width)] for _ in range(im.height//grid_width)]

        # iterar el grid
        for y in range(0, im.height, grid_width):
            for x in range(0, im.width, grid_width):
                pixels = []
                # iterar los pixeles del grid
                for y_i in range(y, y + grid_width):
                    for x_i in range(x, x + grid_width):
                        if x_i < im.width and y_i < im.height:
                            pixels.append(im.getpixel((x_i, y_i)))
            
                # ver que color es el que mas tiene cada grid
                queColor = max(collections.Counter(pixels).items(), key=lambda x: x[1])[0]
                #llenar el grid con su color mas dominante
                nuevaImagen.paste(queColor, (x, y, x + grid_width, y + grid_width))
                #llenar la matriz con el color mas dominante
                matriz[y//grid_width][x//grid_width] = queColor

        '''
        dibujar el grid gris en la nueva imagen
        '''
        dibujar = ImageDraw.Draw(nuevaImagen)
        colorDelGrid = (128, 128, 128)
        # Draw horizontales
        for y in range(0, im.height, grid_width):
            dibujar.line([(0, y), (im.width, y)], fill=colorDelGrid, width=1)
        # dibujar verticales
        for x in range(0, im.width, grid_width):
            dibujar.line([(x, 0), (x, im.height)], fill=colorDelGrid, width=1)


        # guardar la imagen
        nuevaImagen.save("laberinto.bmp")
        self.matriz = matriz
        

    #funcion para ver si el numero es divisible
    def divisible_number(self, larger_number, smaller_number):
        for i in range(smaller_number, 0,  -1):
            if larger_number % i == 0:
                return i