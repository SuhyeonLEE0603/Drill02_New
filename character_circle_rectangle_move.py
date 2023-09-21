from pico2d import *
from math import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def run_rectangle():
    print('CIRCLE')

    # 그림 그리기
    cx, cy, r = 400, 300, 200

    for deg in range(0, 360, 1):
        x = r * cos(radians(deg)) + cx
        y = r * sin(radians(deg)) + cy
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        delay(0.01)

    pass

def run_circle():
    print('RECTANGLE')
    pass

while True:
    run_rectangle()
    run_circle()
    break

close_canvas()