
# 클릭된 위치들을 차례대로 따라가는 소년 (동영상 참고)
# 클릭한 위치에 손 화살표가 만들어짐 ( 2 점 )
# 소년이 차례대로 따라감( 1 점 )
# 소년이 도착한 손화살표는 사라짐 ( 1 점 )

from pico2d import *


TUK_WIDTH, TUK_HEIGHT = 800, 800

open_canvas(TUK_WIDTH, TUK_WIDTH)
tuk_ground = load_image('TUK_GROUND_FULL.png')
character = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')
#---------------------------------------------------------------------------

running = True
def exit_key():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def Rendering():
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 5, TUK_HEIGHT // 5)
    update_canvas()
    pass

def Logic():
    pass


while running:
    exit_key()
    if not running:
        break
    Rendering()
    Logic()
    # frame = ( frame + 1 ) % 8
    delay(0.05)

close_canvas()