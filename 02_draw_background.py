import pyxel


def update():
    pass


def draw():
    pyxel.cls(8)


pyxel.init(160, 120)
pyxel.run(update, draw)
