import random
from PIL import Image, ImageDraw, ImageFont
from screeninfo import get_monitors
from random import randint

#taille allumette 260x180


img = Image.new(mode="RGB", size=(get_monitors()[0].width, get_monitors()[0].height), color=(0, 0, 0))

x_0= 100
x_1 = 360
x_2 = 620
x_3 = 880
x_4 = 1140
x_5 = 1400
x_6 = 1660
y_0 = 150
y_1 = 310
y_2 = 450
y_3 = 560
y_4 = 700
y_5=960
epsilon = 50 #espace entre lettres

# borders :
foreground = Image.open("/Users/leilaelamine/PycharmProjects/lucifer/allumette.png").rotate(90, expand=True)
img.paste(foreground, (x_0, y_0), foreground)
img.paste(foreground, (x_0, y_2), foreground)
img.paste(foreground, (x_0, y_4), foreground)
img.paste(foreground, (x_6, y_0), foreground)
img.paste(foreground, (x_6, y_2), foreground)
img.paste(foreground, (x_6, y_4), foreground)

foreground = Image.open("/Users/leilaelamine/PycharmProjects/lucifer/allumette.png")
img.paste(foreground, (x_0, y_0), foreground)
img.paste(foreground, (x_1, y_0), foreground)
img.paste(foreground, (x_2, y_0), foreground)
img.paste(foreground, (x_3, y_0), foreground)
img.paste(foreground, (x_4, y_0), foreground)
img.paste(foreground, (x_5, y_0), foreground)
img.paste(foreground, (x_0, y_5), foreground)
img.paste(foreground, (x_1, y_5), foreground)
img.paste(foreground, (x_2, y_5), foreground)
img.paste(foreground, (x_3, y_5), foreground)
img.paste(foreground, (x_4, y_5), foreground)
img.paste(foreground, (x_5, y_5), foreground)


#Letters :
foreground = Image.open("/Users/leilaelamine/PycharmProjects/lucifer/allumette.png").rotate(-25, expand=True)
img.paste(foreground, (x_1, y_2+100), foreground)
img.paste(foreground, (x_2-30, y_3+100), foreground)
img.paste(foreground, (x_3-50, y_3+200), foreground)
foreground = Image.open("/Users/leilaelamine/PycharmProjects/lucifer/allumette.png").rotate(115, expand=True)
img.paste(foreground, (x_3+80, y_2+180), foreground)
img.paste(foreground, (x_3-20, y_2-50), foreground)
img.paste(foreground, (x_3-120, y_0+20), foreground)
foreground = Image.open("/Users/leilaelamine/PycharmProjects/lucifer/allumette.png").rotate(-115, expand=True)
img.paste(foreground, (x_2+20, y_0+20), foreground)
img.paste(foreground, (x_2-80, y_1+100), foreground)
img.paste(foreground, (x_1+80, y_3+80), foreground)
foreground = Image.open("/Users/leilaelamine/PycharmProjects/lucifer/allumette.png").rotate(25, expand=True)
img.paste(foreground, (x_1+100, y_3+180), foreground)
img.paste(foreground, (x_2+70, y_3+90), foreground)
img.paste(foreground, (x_3+20, y_2+110), foreground)



foreground = Image.open("/Users/leilaelamine/PycharmProjects/lucifer/allumette.png")
img.paste(foreground, (x_1, y_2+100), foreground)
img.paste(foreground, (x_2, y_2+100), foreground)
img.paste(foreground, (x_3, y_2+100), foreground)

print(f'[33,{33+random.randint(5,20)}]') #nb d'allumettes

img.save(f'/Users/leilaelamine/PycharmProjects/lucifer/img/img_48.png')


