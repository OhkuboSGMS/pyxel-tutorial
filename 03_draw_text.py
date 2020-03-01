import pyxel
def update():
    pass
def draw():
    pyxel.cls(7)
    pyxel.text(0, 0, "(^ ^)", 1)
    # pyxel.text(0, 0, "!#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHI", 0)
    # pyxel.text(0,6,"JKLMNOPQRSTUVWXYZ[\]^_`",0)
    # pyxel.text(0,13,"abcdefghijklmnopqrstuvwxyz{|}~",0)
    # pyxel.text(0,8,"あいうえお",8)
    pyxel.text(140, 110, "(^ ^)", 1)


pyxel.init(160, 120)
pyxel.run(update, draw)
