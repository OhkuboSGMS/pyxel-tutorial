import pyxel
import random

WIDTH = 256
HEIGHT = 256
ITEM_TYPES = [{"u": 0, "v": 64}, {"u": 32, "v": 64}]


# 円同士のあたり判定
def collision_detection(src, target):
    l = (src.x - target.x) ** 2 + (src.y - target.y) ** 2
    rr = (src.r + target.r) ** 2
    if l <= rr:
        return {"obj": target, "col": True}
    else:
        return {"obj": None, "col": False}


class Player:
    def __init__(self):
        self.tag = "Player"
        self.x, self.y = WIDTH // 2, HEIGHT // 2
        self.w = 32
        self.h = 64
        self.r = 10
        self.hp = 5
        self.alive = True

    def update(self):
        if self.hp <= 0:
            return

        if pyxel.btn(pyxel.KEY_W):
            self.y -= self.hp
        elif pyxel.btn(pyxel.KEY_S):
            self.y += self.hp

        if pyxel.btn(pyxel.KEY_A):
            self.x -= self.hp
        elif pyxel.btn(pyxel.KEY_D):
            self.x += self.hp

    def draw(self):
        pyxel.blt(self.x - self.w // 2, self.y - self.h // 2,
                  0, 16, 0, self.w, self.h, colkey=pyxel.COLOR_WHITE)
        # pyxel.circb(self.x, self.y, 10, pyxel.COLOR_RED)
        pyxel.text(self.x - 10, self.y - 10, f"HP:{self.hp}", pyxel.COLOR_BLACK)

    def collision(self, obj):
        print(obj.tag)
        if obj.tag == "Enemy":
            obj.alive = False
            self.hp -= 1
        elif obj.tag == "Item":
            obj.alive = False
            self.hp += 1


class Enemy:
    def __init__(self):
        self.tag = "Enemy"
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.w = 32
        self.h = 32
        self.r = 10
        self.v = random.randint(-4,4)
        self.direction = random.randint(0, 1)
        self.alive = True

    def update(self):
        if self.direction == 0:
            self.x = (self.x + self.v) % WIDTH
        else:
            self.y = (self.y + self.v) % HEIGHT

    def draw(self):
        pyxel.blt(self.x - self.w // 2, self.y - self.h // 2, 0, 64, 64, 64 + 32, 64 + 32, colkey=pyxel.COLOR_WHITE)
        # pyxel.circb(self.x, self.y, 10, pyxel.COLOR_RED)


class Item:
    def __init__(self, item):
        self.tag = "Item"
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.u = item["u"]
        self.v = item["v"]
        self.w, self.h = 32, 32
        self.r = 10

        self.item = item
        self.alive = True

    def update(self):
        pass

    def draw(self):
        pyxel.blt(self.x - self.w // 2, self.y - self.h // 2, 0, self.u, self.v, 32, 32)
        # pyxel.circb(self.x, self.y, 10, pyxel.COLOR_RED)


class App:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, caption="CORONA INC")
        pyxel.load("asset/object-ori.pyxres")

        self.objects = []
        self.player = Player()
        self.enemies = [Enemy() for i in range(random.randint(15, 20))]
        self.items = [Item(ITEM_TYPES[random.randint(0, 1)]) for i in range(random.randint(2, 5))]

        self.objects.extend(self.items)
        self.objects.extend(self.enemies)

        self.objects.append(self.player)

        pyxel.run(self.update, self.draw)

    def update(self):
        for obj in self.objects:
            if obj.alive:
                obj.update()
        for obj in self.objects:
            if not obj.alive:
                continue

            if self.player.tag != obj.tag:
                col_result = collision_detection(self.player, obj)
                if col_result["col"]:
                    self.player.collision(col_result["obj"])

    def draw(self):
        pyxel.cls(pyxel.COLOR_WHITE)
        for obj in self.objects:
            if obj.alive:
                obj.draw()


App()
