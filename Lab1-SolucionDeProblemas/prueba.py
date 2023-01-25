from PIL import ImageDraw
from PIL import Image

# Open the image
path = "grid_colored_image.jpg"
# path = "laberinto.jpg"
# path = "lab1.bmp"
im = Image.open(path)

# Create a new image with the same size as the original image
new_im = im.copy()

# Create a draw object
draw = ImageDraw.Draw(new_im)

# Set the grid color to red
grid_color = (255, 0, 0)

# Set the grid width
grid_width = 4

# Draw horizontal lines
for y in range(0, im.height, grid_width):
    draw.line([(0, y), (im.width, y)], fill=grid_color, width=1)

# Draw vertical lines
for x in range(0, im.width, grid_width):
    draw.line([(x, 0), (x, im.height)], fill=grid_color, width=1)

# Save the new image
new_im = new_im.convert("RGB")
new_im.save("grid_image.jpg")
