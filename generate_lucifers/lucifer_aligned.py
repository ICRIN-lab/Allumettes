import random
from PIL import Image, ImageDraw, ImageFont
from screeninfo import get_monitors
from random import randint


def check_distance(L, x):
    for element in L:
        if abs(x - element) < 20:
            return False
    return True



def gen_align(nb_img):
    choices = []
    for i in range(nb_img):
        L = []
        img = Image.new(mode="RGB", size=(get_monitors()[0].width, get_monitors()[0].height), color=(0, 0, 0))
        nb_allumettes = randint(5, 30)
        choices.append([nb_allumettes, nb_allumettes + randint(5, 20)])
        for j in range(nb_allumettes):
            foreground = Image.open("allumette.png").rotate(90, expand=True)
            x = randint(50, 1900)
            while not check_distance(L, x):
                print(j)
                x = randint(50, 1900)
            L.append(x)
            y = 550
            img.paste(foreground, (x, y), foreground)
            img.save(f'img/img_{50+i}.png')
    return choices


L_choices = gen_align(25)
print(L_choices)

