
# 클릭된 위치들을 차례대로 따라가는 소년 (동영상 참고)
# 클릭한 위치에 손 화살표가 만들어짐 ( 2 점 )
# 소년이 차례대로 따라감( 1 점 )
# 소년이 도착한 손화살표는 사라짐 ( 1 점 )

from pico2d import *
import random
import math

TUK_WIDTH, TUK_HEIGHT = 800, 800

open_canvas(TUK_WIDTH, TUK_WIDTH)
tuk_ground = load_image('TUK_GROUND_FULL.png')
character = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')
#---------------------------------------------------------------------------

running = True
def event_key():
    global running
    global mouse_x, mouse_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            mouse_x, mouse_y = event.x, TUK_HEIGHT - 1 - event.y 

def Rendering():
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 5, TUK_HEIGHT // 5)
    boy_draw()
    arrow_draw()
    cursor_draw()
    update_canvas()
    pass

def Logic():
    global x1, y1, x2, y2
    t = 0.03 
    x1 += (x2 - x1) * t
    y1 += (y2 - y1) * t
    calculate_distance()
    set_direction()
    

def boy_draw():
    if x_dir < 0:
        character.clip_composite_draw(frame * 100, 100, 100, 100, 0, 'h', x1, y1, 100, 100)
    else:
        character.clip_draw(frame * 100, 100, 100, 100, x1, y1)

def arrow_draw():
    arrow.draw(x2,y2)

def cursor_draw():
    arrow.draw(mouse_x, mouse_y)

def set_direction():
    global x_dir
    if x2 - x1 >= 0:
        x_dir = 1
    elif x2 - x1 < 0:
        x_dir = -1

def calculate_distance():
    global x2, y2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    if distance <= 10:
        x2 = random.randint(0, TUK_WIDTH - 1)
        y2 = random.randint(0, TUK_HEIGHT - 1)


#===================================================  
frame = 0
x1, y1 = TUK_WIDTH, TUK_HEIGHT
x2 = random.randint(0, TUK_WIDTH - 1)
y2 = random.randint(0, TUK_HEIGHT - 1)
x_dir = 1
mouse_x, mouse_y = 0, 0
hide_cursor()

while running:
    event_key()
    if not running:
        break
    Rendering()
    Logic()
    frame = ( frame + 1 ) % 8
    delay(0.05)

close_canvas()