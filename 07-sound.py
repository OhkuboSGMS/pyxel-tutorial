import pyxel
def update():
    pass
def draw():
    pyxel.cls(0)
pyxel.init(200,150)

pyxel.sound(0).set(
    "C2D2E2F2E2D2C2C2 E2F2G2A2G2F2E2E2 C2C2  C2C2  C2C2  C2D2E2F2E2D2C2C2 ",
    "S",
    "6",
    "NNNNNNNN NNNNNNNN NF NF NF  NNNNNNNF",
    60
)

pyxel.play(0,0,loop=True)
pyxel.run(update,draw)

