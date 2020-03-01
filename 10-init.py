import pyxel


def update():
    pass


def draw():
    pyxel.cls(0)


print(pyxel.COLOR_RED, pyxel.COLOR_LIME)
print("Palltte", [hex(i) for i in pyxel.DEFAULT_PALETTE])
palette = pyxel.DEFAULT_PALETTE.copy()
palette[0] = 0xFF0000
palette[1] = 0x00FF00
pyxel.init(256, 256, caption="Title", scale=2, palette=palette, border_width=1, border_color=palette[1],
           quit_key=pyxel.KEY_A)
pyxel.run(update, draw)
