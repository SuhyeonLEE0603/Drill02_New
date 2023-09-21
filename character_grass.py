from pico2d import *
from math import *
open_canvas()

# fill here

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
y = 90

while (x < 780):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x, y)
    x = x + 2
    delay(0.005)

while(y < 560):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    y = y + 2
    delay(0.005)

while (x > 20):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x, y)
    x = x - 2
    delay(0.005)

while(y > 90):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    y = y - 2
    delay(0.005)

while (x < 380):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x, y)
    x = x + 2
    delay(0.005)

angle = radians(1)


while (angle < radians(360)):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    x = x + cos(angle) * 4
    y = y + sin(angle) * 4
    angle = angle + radians(1)
    delay(0.005)

close_canvas()
