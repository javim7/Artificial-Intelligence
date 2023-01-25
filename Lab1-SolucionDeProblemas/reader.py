from PIL import Image, ImageDraw
import collections

class Reader():

    def __init__(self, path):
        self.path = path
        self.matriz = []
        self.grid_width = 0

    def imageReader(self):
        # abrir la imagen
        # im = Image.open("lab1.bmp") #24 - 500
        # im = Image.open("lab2.bmp") #9
        im = Image.open(self.path) #4 - 640

        # definir el tamaño del grid
        if im.width <= 500:
            self.grid_width = (im.width//100)*5
        if im.width == 320:
            self.grid_width = (im.width//100)*3
        if im.width > 600:
            self.grid_width = (im.width//100)
        if im.width == 640:
            self.grid_width = (im.width//100)-2

        # crear una nueva imagen 
        nuevaImagen = Image.new("RGB", (im.width, im.height), (255, 255, 255))

        self.grid_width = self.divisible_number(im.width, self.grid_width)
        self.matriz = [[0 for _ in range(im.width//self.grid_width)] for _ in range(im.height//self.grid_width)]

        # iterar el grid
        for y in range(0, im.height, self.grid_width):
            for x in range(0, im.width, self.grid_width):
                pixels = []
                # iterar los pixeles del grid
                for y_i in range(y, y + self.grid_width):
                    for x_i in range(x, x + self.grid_width):
                        if x_i < im.width and y_i < im.height:
                            pixels.append(im.getpixel((x_i, y_i)))
            
                # ver que color es el que mas tiene cada grid
                queColor = max(collections.Counter(pixels).items(), key=lambda x: x[1])[0]
                #llenar el grid con su color mas dominante
                queNumero = self.queNumero(queColor)
                nuevaImagen.paste(queColor, (x, y, x + self.grid_width, y + self.grid_width))
                #llenar la matriz con el color mas dominante
                self.matriz[y//self.grid_width][x//self.grid_width] = queNumero

        '''
        dibujar el grid gris en la nueva imagen
        '''
        dibujar = ImageDraw.Draw(nuevaImagen)
        colorDelGrid = (128, 128, 128)
        # Draw horizontales
        for y in range(0, im.height, self.grid_width):
            dibujar.line([(0, y), (im.width, y)], fill=colorDelGrid, width=1)
        # dibujar verticales
        for x in range(0, im.width, self.grid_width):
            dibujar.line([(x, 0), (x, im.height)], fill=colorDelGrid, width=1)


        # guardar la imagen
        nuevaImagen.save("./resultados/laberinto.bmp")

    #funcion para ver si el numero es divisible
    def divisible_number(self, larger_number, smaller_number):
        for i in range(smaller_number, 0,  -1):
            if larger_number % i == 0:
                return i

    def queNumero(self, rgb, threshold=100):
        if rgb[0] <= 20 and rgb[1] <= 20 and rgb[2] <= 20:
            return 0
        elif rgb[0] >= 240 and rgb[1] >= 240 and rgb[2] >= 240:
            return 1
        elif rgb[0] >= rgb[1] and rgb[0] >= rgb[2] and rgb[0]-rgb[1] > threshold and rgb[0]-rgb[2] > threshold:
            return 2
        elif rgb[1] >= rgb[0] and rgb[1] >= rgb[2] and rgb[1]-rgb[0] > threshold and rgb[1]-rgb[2] > threshold:
            return 3