from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def run_rectangle():
    print('CIRCLE')

    # 그림 그리기
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(400, 90)
    delay(1)

    pass

def run_circle():
    print('RECTANGLE')
    pass

while True:
    run_rectangle()
    run_circle()
    break

close_canvas()