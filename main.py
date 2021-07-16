from opensimplex import OpenSimplex
from PIL import Image
from colour import Color
import random
import numpy as np
import math

# Constants
WIDTH = 500
HEIGHT = 500
MARGIN = 10
STEEPNESS = 2
ZOOM = 160
STEPS = 4
BIAS = 0.1
SEED = random.randint(0, 1000)

COLOR_BIAS = 10
BASE_RGB = Color("red", hue=np.round(random.random(), 2))


def getColor(val):  # , bins
    BASE_RGB.set_luminance((max(val - COLOR_BIAS, 0)) / 255)
    return int(BASE_RGB.get_red() * 255), int(BASE_RGB.get_green() * 255), int(BASE_RGB.get_blue() * 255)


BASE_RGB = Color("red", hue=np.round(random.random(), 2))

# Noise function
noise = OpenSimplex(SEED)

# Data of map
data = np.zeros((WIDTH, HEIGHT), dtype=np.uint8)
img = np.zeros((WIDTH, HEIGHT, 3), dtype=np.uint8)

for y in range(0, HEIGHT):
    for x in range(0, WIDTH):
        data[y][x] = (noise.noise2d(x / ZOOM, y / ZOOM) + 1) / 2 * 255

        # Calculate distance from center
        distX = abs(WIDTH / 2 - x)
        distY = abs(HEIGHT / 2 - y)
        dist = math.sqrt(distX * distX + distY * distY)

        # Calculate mask from position
        maxW = WIDTH / 2 - MARGIN
        delta = dist / maxW
        gradient = delta ** STEEPNESS + BIAS
        data[y][x] = int(data[y][x] * max(0.0, 1 - gradient))

        # Apply color
        img[y][x] = getColor(data[y][x])  # , bins

image = Image.fromarray(img, 'RGB')
image.save(str(SEED) + '.png')
print("Saved " + str(SEED) + ".png!")
