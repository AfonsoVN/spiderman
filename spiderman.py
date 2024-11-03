import pgzrun
from random import randint
TITLE = "spiderman"
WIDTH=500
HEIGHT=500
spiderman =Actor("spiderman")
spiderman.pos = 200,200
def draw():
    screen.clear()
    screen.fill(color = (128,0,0))
    spiderman.draw()
message= " "
def draw():
    screen.clear()
    screen.fill(color = (128,0,0))
    spiderman.draw()

    screen.draw.text(message,center = (400,10),fontsize= 30)

def place_spiderman():
    spiderman.x = randint(50,WIDTH-50)
    spiderman.y = randint(50,WIDTH-50)

def on_mouse_down(pos):

    global message
    if spiderman.collidepoint(pos):
        message = "Good Shot"
        place_spiderman()
    else:
        message = "You Missed!"
place_spiderman()
pgzrun.go()