from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def run_rectangle():
    print('CIRCLE')
    pass

def run_circle():
    print('RECTANGLE')
    pass

while True:
    run_rectangle()
    run_circle()

close_canvas()