#!/usr/bin/env python3
# coding: utf8
import pyxel, os
class App:
    def __init__(self):
        self.window = Window()
        Resource()
        self.pc = PlayerCharacter()
        print('DEFAULT_FPS:', pyxel.DEFAULT_FPS)
        pyxel.run(self.update, self.draw)
    def update(self):
        self.pc.update()
    def draw(self):
        self.window.draw()
        self.pc.draw()

class Resource:
    def __init__(self):
        pyxel.load(self.ResourcePath)
    def __this_dir(self): return os.path.dirname(__file__)
    def __parent_dir(self, path): return os.path.dirname(path)
    @property
    def RootDir(self): return self.__parent_dir(self.__this_dir())
    @property
    def ResourcePath(self): return os.path.join(self.RootDir, 'res/python.pyxres')

class Window:
    def __init__(self, width=64, height=48, border_width=0):
        pyxel.init(width, height, border_width=border_width)
    def draw(self): pyxel.cls(0)

class PlayerCharacter:
    def __init__(self, x=0, y=0, width=8, height=8, img=0, u=0, v=0, colkey=0):
        self.sprite = Python()
        self.x = (pyxel.width / 2) - (self.sprite.Sprite.W / 2)
        self.y = (pyxel.height/ 2) - (self.sprite.Sprite.H / 2)
    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT) and self.x > 0: self.x -= 1; self.sprite.Sprite.Left();
        if pyxel.btn(pyxel.KEY_RIGHT) and self.x < pyxel.width - self.sprite.Sprite.W: self.x += 1; self.sprite.Sprite.Right();
        if pyxel.btn(pyxel.KEY_UP) and self.y > 0: self.y -= 1
        if pyxel.btn(pyxel.KEY_DOWN) and self.y < pyxel.height - self.sprite.Sprite.H: self.y += 1
        self.sprite.Sprite.update()
    def draw(self):
        pyxel.blt(self.x, self.y, self.sprite.Sprite.Img, self.sprite.Sprite.U, self.sprite.Sprite.V, self.sprite.Sprite.W, self.sprite.Sprite.H, self.sprite.Sprite.ColKey)
        pyxel.text(self.x - 10, self.y - 10, "I'm Python!", 8)
#        pyxel.text(self.x - 10, self.y - 10, "私はヘビです！", 8)

class Python:
    def __init__(self):
        self.sprite = Sprite()
    @property
    def Sprite(self): return self.sprite

class Sprite:
    def __init__(self, img=0, w=8, h=8, bu=0, bv=0, colkey=0, frame=2, is_rev_h=False, is_rev_v=False):
        self.__img = img
        self.__dx = -1 if is_rev_h else 1
        self.__dy = -1 if is_rev_h else 1
        self.__w = w
        self.__h = h
        self.__bu = bu
        self.__bv = bv
        self.__colkey = colkey
        self.__frame = frame
    def update(self):
        if 0 == pyxel.frame_count % (pyxel.DEFAULT_FPS / 2):
            self.__frame += 1
            if self.__frame > 1: self.__frame = 0
    @property
    def Speed(self): return self.__speed
    @Speed.setter
    def Speed(self, value):
        if self.__speed <= pyxel.DEFAULT_FPS:
            self.__speed = value
    @property
    def Img(self): return self.__img
    @property
    def U(self): return self.__bu + (self.__frame * abs(self.W))
    @property
    def V(self): return self.__bv
    @property
    def W(self): return self.__w * self.__dx
    @property
    def H(self): return self.__h * self.__dy
    @property
    def ColKey(self): return self.__colkey
    def Left(self): self.__dx = -1; self.__dy = 1;
    def Right(self): self.__dx = 1; self.__dy = 1;

App()
