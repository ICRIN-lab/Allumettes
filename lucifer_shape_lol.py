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
foreground = Image.open("allumette.png").rotate(90, expand=True)
img.paste(foreground, (x_0, y_0), foreground)
img.paste(foreground, (x_0, y_2), foreground)
img.paste(foreground, (x_0, y_4), foreground)
img.paste(foreground, (x_6, y_0), foreground)
img.paste(foreground, (x_6, y_2), foreground)
img.paste(foreground, (x_6, y_4), foreground)

foreground = Image.open("allumette.png")
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
foreground = Image.open("allumette.png").rotate(90, expand=True)
img.paste(foreground, (x_1, y_1+100), foreground)
img.paste(foreground, (x_2+epsilon, y_1+100), foreground)
img.paste(foreground, (x_3+50, y_1+100), foreground)
img.paste(foreground, (x_3+200, y_1+100), foreground)



foreground = Image.open("allumette.png")
img.paste(foreground, (x_1, y_3+100), foreground)
img.paste(foreground, (x_2+epsilon, y_3+100), foreground)
img.paste(foreground, (x_3+200, y_3+100), foreground)
img.paste(foreground, (x_2+epsilon, y_1+100), foreground)



img.show()

img.save(f'img/shapes/lucifer_shape_lol.png')


