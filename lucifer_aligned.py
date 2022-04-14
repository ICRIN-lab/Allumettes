import random
from PIL import Image, ImageDraw, ImageFont
from screeninfo import get_monitors
from random import randint

L=[]
def check_distance (L,x):
    for element in L:
        if abs(x-element)<50:
            return False
    return True

nb_allumettes=randint(5,30)
nb_img = 2
for i in range (nb_img):
    img = Image.new(mode="RGB", size=(get_monitors()[0].width, get_monitors()[0].height), color=(0, 0, 0))
    for j in range(nb_allumettes):
        foreground = Image.open("allumette.png").rotate(90, expand=True)
        x = randint(100, 1600)
        while not check_distance(L,x):
            x = randint(100, 1600)
        L.append(x)
        y = 550
        img.paste(foreground, (x, y), foreground)
    img.save(f'img/lucifer_line_{i}.png')
print(f"Image n°{i}")