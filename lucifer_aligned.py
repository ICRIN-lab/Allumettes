import random
from PIL import Image, ImageDraw, ImageFont
from screeninfo import get_monitors
from random import randint


def check_distance(L, x):
    for element in L:
        if abs(x - element) < 20:
            return False
    return True


nb_allumettes = randint(5,30)
nb_img = 25
for i in range(nb_img):
    L = []
    img = Image.new(mode="RGB", size=(get_monitors()[0].width, get_monitors()[0].height), color=(0, 0, 0))
    for j in range(nb_allumettes):
        foreground = Image.open("allumette.png").rotate(90, expand=True)
        x = randint(50, 1900)
        while not check_distance(L, x):
            print(j)
            x = randint(50, 1900)
        L.append(x)
        y = 550
        img.paste(foreground, (x, y), foreground)
    img.save(f'img/lines/lucifer_line_{i}.png')

