__author__ = 'Diego Vinicius de Mello Munhoz'

import pygame as pg
from .. import setup
from .. import constants as c
from . import powerups
from . import coin

class Brick(pg.sprite.Sprite):
    """Tijolos que podem ser destruídos"""
    def __init__(self, x, y, contents=None, powerup_group=None, name='brick'):
        """Inicializando os objetos"""
        pg.sprite.Sprite.__init__(self)
        self.sprite_sheet = setup.GFX['tile_set']

        self.frames = []
        self.frame_index = 0
        self.setup_frames()
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = pg.mask.from_surface(self.image)
        self.bumped_up = False
        self.rest_height = y
        self.state = c.RESTING
        self.y_vel = 0
        self.gravity = 1.2
        self.name = name
        self.contents = contents
        self.setup_contents()
        self.group = powerup_group
        self.powerup_in_box = True


    def get_image(self, x, y, width, height):
        """Extrai a imagem do tijolo da lista de imagens"""
        image = pg.Surface([width, height]).convert()
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(c.BLACK)
        image = pg.transform.scale(image,
                                   (int(rect.width*c.BRICK_SIZE_MULTIPLIER),
                                    int(rect.height*c.BRICK_SIZE_MULTIPLIER)))
        return image

    def setup_frames(self):
        """Defina os quadros para uma lista"""
        self.frames.append(self.get_image(16, 0, 16, 16))
        self.frames.append(self.get_image(432, 0, 16, 16))

    def setup_contents(self):
        """Coloque 6 moedas em conteúdo, se necessário"""
        if self.contents == '6coins':
            self.coin_total = 6
        else:
            self.coin_total = 0

    def update(self):
        """Atualiza o tijolo"""
        self.handle_states()

    def handle_states(self):
        """Determina o comportamento de tijolo, com base no estado"""
        if self.state == c.RESTING:
            self.resting()
        elif self.state == c.BUMPED:
            self.bumped()
        elif self.state == c.OPENED:
            self.opened()

    def resting(self):
        """Estado, quando não se movendo"""
        if self.contents == '6coins':
            if self.coin_total == 0:
                self.state == c.OPENED

    def bumped(self):
        """Ação durante um estado BUMPED"""
        self.rect.y += self.y_vel
        self.y_vel += self.gravity

        if self.rect.y >= (self.rest_height + 5):
            self.rect.y = self.rest_height
            if self.contents == 'star':
                self.state = c.OPENED
            elif self.contents == '6coins':
                if self.coin_total == 0:
                    self.state = c.OPENED
                else:
                    self.state = c.RESTING
            else:
                self.state = c.RESTING


    def start_bump(self, score_group):
        """Tijolo de transições em BUMPED estado"""
        self.y_vel = -6

        if self.contents == '6coins':
            setup.SFX['coin'].play()

            if self.coin_total > 0:
                self.group.add(coin.Coin(self.rect.centerx, self.rect.y, score_group))
                self.coin_total -= 1
                if self.coin_total == 0:
                    self.frame_index = 1
                    self.image = self.frames[self.frame_index]
        elif self.contents == 'star':
            setup.SFX['powerup_appears'].play()
            self.frame_index = 1
            self.image = self.frames[self.frame_index]

        self.state = c.BUMPED


    def opened(self):
        """Ação durante estado aberto"""
        self.frame_index = 1
        self.image = self.frames[self.frame_index]

        if self.contents == 'star' and self.powerup_in_box:
            self.group.add(powerups.Star(self.rect.centerx, self.rest_height))
            self.powerup_in_box = False


class BrickPiece(pg.sprite.Sprite):
    """Peças que aparecem quando os tijolos estão quebrados"""
    def __init__(self, x, y, xvel, yvel):
        super(BrickPiece, self).__init__()
        self.sprite_sheet = setup.GFX['item_objects']
        self.setup_frames()
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x_vel = xvel
        self.y_vel = yvel
        self.gravity = .8


    def setup_frames(self):
        """criar a lista de quadro"""
        self.frames = []

        image = self.get_image(68, 20, 8, 8)
        reversed_image = pg.transform.flip(image, True, False)

        self.frames.append(image)
        self.frames.append(reversed_image)


    def get_image(self, x, y, width, height):
        """Extrair a imagem da lista das imagens"""
        image = pg.Surface([width, height]).convert()
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(c.BLACK)
        image = pg.transform.scale(image,
                                   (int(rect.width*c.BRICK_SIZE_MULTIPLIER),
                                    int(rect.height*c.BRICK_SIZE_MULTIPLIER)))
        return image


    def update(self):
        """atualizando pedaço do tijolo"""
        self.rect.x += self.x_vel
        self.rect.y += self.y_vel
        self.y_vel += self.gravity
        self.check_if_off_screen()

    def check_if_off_screen(self):
        """Remova grupos de sprite de fora da tela"""
        if self.rect.y > c.SCREEN_HEIGHT:
            self.kill()












