import pyxel
width, height = 160, 120
r = 1
x, y = 50, 50
def update():
    global x, y, r
    if pyxel.btnp(pyxel.KEY_Z, 30, 10):
        r += 1
    if pyxel.btnp(pyxel.KEY_X, 30, 10):
        r -= 1

    if pyxel.btn(pyxel.KEY_W):
        y -= 1
    elif pyxel.btn(pyxel.KEY_S):
        y += 1

    if pyxel.btn(pyxel.KEY_A):
        x -= 1
    elif pyxel.btn(pyxel.KEY_D):
        x += 1
def draw():
    pyxel.cls(0)
    pyxel.circb(pyxel.mouse_x, pyxel.mouse_y, r, 3)
    pyxel.rectb(x, y, 20, 20, 4)


pyxel.init(width, height)
print(pyxel.DEFAULT_FPS)
pyxel.run(update, draw)
