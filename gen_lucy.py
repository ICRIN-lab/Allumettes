# petit code qui génère un nombre aléatoire d'allumettes
from PIL import Image, ImageDraw, ImageFont
from screeninfo import get_monitors
from random import randint


def gen_allum(nb_img):
    choices = []
    for i in range(nb_img):
        nb_allumettes = randint(30, 80)
        choices.append([nb_allumettes, int(abs(100 - 1.1 * nb_allumettes))])  # calcul à refaire
        img = Image.new(mode="RGB", size=(get_monitors()[0].width, get_monitors()[0].height), color=(0, 0, 0))
        for j in range(nb_allumettes):
            angle = randint(0, 180)
            foreground = Image.open("allumette.png").rotate(angle, expand=True)
            x = randint(0, get_monitors()[0].width - 300)
            y = randint(0, get_monitors()[0].height - 300)
            img.paste(foreground, (x, y), foreground)
            img.save(f"img/allum_{i}.png")
        print(f"Image n°{i}")
    return choices


L_choices = gen_allum(50)
print(L_choices)