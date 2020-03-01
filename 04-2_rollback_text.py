import pyxel
width,height =160,120
x, y = 0, 0
def update():
    global x, y
    x = (x+1)%width
    y = (y+2)%height


def draw():
    pyxel.cls(7)
    pyxel.text(x, y, "(^ ^)", 1)
pyxel.init(width, height)
pyxel.run(update, draw)
