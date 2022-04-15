import random
from PIL import Image, ImageDraw, ImageFont
from screeninfo import get_monitors
from random import randint


def check_distance_x (L,x):
    for element in L:
        if abs(x-element)<10:
            return False
    return True

def check_distance_y(J,y):
    for coordinate in J:
        if abs(y-coordinate)<10:
            return False
    return True


def gen_allum(nb_img):
    choices = []
    for i in range (nb_img):
        L = []
        J = []
        nb_allumettes = randint(3, 15)
        img = Image.new(mode="RGB", size=(get_monitors()[0].width, get_monitors()[0].height), color=(0, 0, 0))
        choices.append([4*nb_allumettes, nb_allumettes + randint(5, 20)])
        for j in range(nb_allumettes):
            foreground = Image.open("allumette.png").rotate(90, expand=True)
            x = randint(50,900)
            while not check_distance_x(L,x):
                x = randint(50, 900)
            L.append(x)
            y = 100
            img.paste(foreground, (x, y), foreground)
            foreground = Image.open("allumette.png").rotate(90, expand=True)
            x = randint(1000,1900)
            while not check_distance_x(L, x):
                x = randint(1000,1900)
            L.append(x)
            y = 550
            img.paste(foreground, (x, y), foreground)
            foreground = Image.open("allumette.png")
            x = 100
            y = randint(550, 800)
            while not check_distance_y(J,y):
                y = randint(550, 800)
            J.append(y)
            img.paste(foreground, (x, y), foreground)
            foreground = Image.open("allumette.png")
            x = 1000
            y = randint(100,500)
            while not check_distance_y(J, y):
                y = randint(100,500)
            J.append(y)
            img.paste(foreground, (x, y), foreground)
            img.save(f'img/img_{75+i}.png')
    return choices


L_choices = gen_allum(25)
print(L_choices)

