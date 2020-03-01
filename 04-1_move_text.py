import pyxel

x, y = 0, 0
def update():
    global x, y
    x += 1
    y += 2


def draw():
    pyxel.cls(7)
    pyxel.text(x, y, "(^ ^)", 1)
pyxel.init(160, 120)
pyxel.run(update, draw)
