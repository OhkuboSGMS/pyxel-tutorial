import pyxel

x, y = 1, 1
w, h = 32, 32
vx, vy = 1, 1
width, height = 160, 120
pyxel.init(width, height)
pyxel.image(0).load(0, 0, "asset/dvd-32-black.png")

def update():
    global x, y, vx, vy
    if (x) < 0:
        vx = 1
    elif (x + w) > width:
        vx = -1
    if (y) < 0:
        vy = 1
    elif (y + h ) > height:
        vy = -1

    x += vx
    y += vy


def draw():
    pyxel.cls(0)
    pyxel.blt(x, y, 0, 0, 0, w, h,colkey=1)

pyxel.run(update, draw)
