from pico2d import *
from math import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')


def render_frame(x, y):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    delay(0.01)

def run_circle():
    print('CIRCLE')

    # 그림 그리기
    cx, cy, r = 400, 300, 250

    for deg in range(0, 360, 1):
        x = r * cos(radians(deg)) + cx
        y = r * sin(radians(deg)) + cy
        render_frame(x, y)

def run_rectangle():

    for x in range(50, 750 + 1, 10):
        render_frame(x, 90)

    for y in range(90, 550, 10):
        render_frame(750, y)

    for x in range(750, 50, -10):
        render_frame(x, 550)

    for y in range(550, 90, -10):
        render_frame(50, y)

while True:
    run_circle()
    run_rectangle()

close_canvas()