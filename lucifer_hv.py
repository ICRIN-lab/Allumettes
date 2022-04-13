import random
from PIL import Image, ImageDraw, ImageFont
from screeninfo import get_monitors
from random import randint

L=[]
J=[]
def check_distance_x (L,x):
    for element in L:
        if abs(x-element)<50:
            return False
    return True

def check_distance_y(J,y):
    for coordinate in J:
        if abs(y-coordinate)<50:
            return False
    return True


nb_allumettes=randint(3,10)
nb_img=1

for i in range (nb_img):
    img = Image.new(mode="RGB", size=(get_monitors()[0].width, get_monitors()[0].height), color=(0, 0, 0))
    for j in range(nb_allumettes):
        foreground = Image.open("allumette.png").rotate(90, expand=True)
        x = randint(100,900)
        while not check_distance_x(L,x):
            x = randint(100, 900)
        L.append(x)
        y = 100
        img.paste(foreground, (x, y), foreground)
        foreground = Image.open("allumette.png").rotate(90, expand=True)
        x = randint(1000,1500)
        while not check_distance_x(L, x):
            x = randint(1000,1500)
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
img.save(f'img/lucifer_hv_{i}.png')
print(f"Image n°{i}")


