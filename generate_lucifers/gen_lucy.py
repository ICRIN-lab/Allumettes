# petit code qui génère un nombre aléatoire d'allumettes
import random

from PIL import Image, ImageDraw, ImageFont
from screeninfo import get_monitors
from random import randint


def gen_allum(nb_img):
    choices = []
    for i in range(nb_img):
        nb_allumettes = randint(10, 90)
        choices.append([nb_allumettes, nb_allumettes + randint(5, 20)])
        img = Image.new(
            mode="RGB",
            size=(get_monitors()[0].width, get_monitors()[0].height),
            color=(0, 0, 0),
        )
        for j in range(nb_allumettes):
            angle = randint(0, 180)
            foreground = Image.open("../allumette.png").rotate(angle, expand=True)
            x = randint(0, get_monitors()[0].width - 300)
            y = randint(0, get_monitors()[0].height - 300)
            img.paste(foreground, (x, y), foreground)
            img.save(f"img/example_{i+997}.png")
        print(f"Image n°{i}")
    return choices


L_choices = gen_allum(3)
print(L_choices)
