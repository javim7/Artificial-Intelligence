from PIL import Image

class Resultado():
    def __init__(self, matriz1, matriz2):
        self.laberinto = matriz1
        self.path = matriz2
    
    def marcarPath(self):
        laberinto = self.laberinto.copy()
        self.path.pop(0)
        for i,j in self.path:
            laberinto[i][j] = 4
        return laberinto
    
    def filename(self, path, algo):
        return './resultados/' + path.split('/')[-1].split('.')[0] + '_' + algo + '.bmp'

    def dibujarFinal(self, matriz1, filename):
        matriz = matriz1.copy()
        img = Image.new('RGB', (len(matriz[0]), len(matriz)), "white")
        pixels = img.load()
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                if matriz[j][i] == 0:
                    pixels[i,j] = (0,0,0)
                elif matriz[j][i] == 1:
                    pixels[i,j] = (255,255,255)
                elif matriz[j][i] == 2:
                    pixels[i,j] = (255,0,0)
                elif matriz[j][i] == 3:
                    pixels[i,j] = (0,255,0)
                elif matriz[j][i] == 4:
                    pixels[i,j] = (0,0,255)
        img.save(filename)
        