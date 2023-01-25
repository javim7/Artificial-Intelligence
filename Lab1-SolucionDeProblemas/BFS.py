from PIL import Image

class BFS():
    def __init__(self, ImagePath):
        self.image = Image.open(ImagePath)
        self.width, self.height = self.image.size
        self.start = None
        self.goals = set()
        self.colores = []
        self.walkable = set()
        self.recorridos = []
        self.puntosNoAlcanzados = 0
        self.load_image()