import spyral
import sys
from spyral import Animation, easing

WIDTH = 1200
HEIGHT = 900
SIZE = (WIDTH, HEIGHT)

class Block(spyral.Sprite):
    def __init__(self, scene):
        spyral.Sprite.__init__(self, scene)
        self.image = spyral.Image(size=(64, 64)).fill((255, 0, 0))
        self.anchor = 'center'
        self.y = HEIGHT / 2
        
        animation = Animation('x', easing.Linear(0, WIDTH), duration = 1.5)
        self.animate(animation)

class Game(spyral.Scene):
    def __init__(self):
        spyral.Scene.__init__(self, SIZE)
        self.background = spyral.Image(size=SIZE).fill((0,0,0))
        
        spyral.event.register("system.quit", sys.exit)
        
        self.block = Block(self)