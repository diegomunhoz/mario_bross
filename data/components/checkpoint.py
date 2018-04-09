__author__ = 'Diego Vinicius de Mello Munhoz'

import pygame as pg
from .. import constants as c


class Checkpoint(pg.sprite.Sprite):
    """Sprite invisível, usado para adicionar inimigos, caixas especiais 
e gatilho deslizar pela aste de bandeira"""
    def __init__(self, x, name, y=0, width=10, height=600):
        super(Checkpoint, self).__init__()
        self.image = pg.Surface((width, height))
        self.image.fill(c.BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.name = name




