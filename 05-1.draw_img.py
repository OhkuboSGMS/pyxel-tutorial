import pyxel

width, height = 160, 120
pyxel.init(width, height)
pyxel.image(0).load(0, 0, "asset/dvd-32.png")
def update():
    pass

def draw():
    pyxel.cls(7)
    pyxel.blt(0,0,0,0,0,32,32)

pyxel.run(update, draw)
