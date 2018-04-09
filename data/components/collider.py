__author__ = 'Diego Vinicius de Mello Munhoz'

import pygame as pg
from .. import constants as c

# Sprites invisíveis colocados por cima de peças de fundo
# que pode ser colidiu com (tubos, passos, chão, etc.
class Collider(pg.sprite.Sprite):
    def __init__(self, x, y, width, height, name='collider'):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((width, height)).convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.state = None

