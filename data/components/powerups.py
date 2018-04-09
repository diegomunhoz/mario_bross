__author__ = 'Diego Vinicius de Mello Munhoz'

import pygame as pg
from .. import constants as c
from .. import setup

class Powerup(pg.sprite.Sprite):
    """Classe base para todos os grupo powerup"""
    def __init__(self, x, y):
        super(Powerup, self).__init__()


    def setup_powerup(self, x, y, name, setup_frames):
        """Esta função de configuração separado me permite passar um diferentes 
setup_frames método dependendo o que é a ativação"""
        self.sprite_sheet = setup.GFX['item_objects']
        self.frames = []
        self.frame_index = 0
        setup_frames()
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = y
        self.state = c.REVEAL
        self.y_vel = -1
        self.x_vel = 0
        self.direction = c.RIGHT
        self.box_height = y
        self.gravity = 1
        self.max_y_vel = 8
        self.animate_timer = 0
        self.name = name


    def get_image(self, x, y, width, height):
        """Se os quadros de imagem da folha de sprite"""

        image = pg.Surface([width, height]).convert()
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(c.BLACK)


        image = pg.transform.scale(image,
                                   (int(rect.width*c.SIZE_MULTIPLIER),
                                    int(rect.height*c.SIZE_MULTIPLIER)))
        return image


    def update(self, game_info, *args):
        """Atualizações dos power-ups"""
        self.current_time = game_info[c.CURRENT_TIME]
        self.handle_state()


    def handle_state(self):
        pass


    def revealing(self, *args):
        """Ação quando powerup deixa a caixa de moeda ou tijolo"""
        self.rect.y += self.y_vel

        if self.rect.bottom <= self.box_height:
            self.rect.bottom = self.box_height
            self.y_vel = 0
            self.state = c.SLIDE


    def sliding(self):
        """Ação para quando powerup desliza ao longo do solo"""
        if self.direction == c.RIGHT:
            self.x_vel = 3
        else:
            self.x_vel = -3


    def falling(self):
        """Quando powerups caem de um precipício"""
        if self.y_vel < self.max_y_vel:
            self.y_vel += self.gravity


class Mushroom(Powerup):
    """Powerup que faz Mario se tornar maior"""
    def __init__(self, x, y, name='mushroom'):
        super(Mushroom, self).__init__(x, y)
        self.setup_powerup(x, y, name, self.setup_frames)


    def setup_frames(self):
        """Define lista de quadro"""
        self.frames.append(self.get_image(0, 0, 16, 16))


    def handle_state(self):
        """Manipula o comportamento com base no estado"""
        if self.state == c.REVEAL:
            self.revealing()
        elif self.state == c.SLIDE:
            self.sliding()
        elif self.state == c.FALL:
            self.falling()


class LifeMushroom(Mushroom):
    """1up cogumelo"""
    def __init__(self, x, y, name='1up_mushroom'):
        super(LifeMushroom, self).__init__(x, y)
        self.setup_powerup(x, y, name, self.setup_frames)

    def setup_frames(self):
        self.frames.append(self.get_image(16, 0, 16, 16))


class FireFlower(Powerup):
    """Powerup que permite que Mario jogar bolas de fogo"""
    def __init__(self, x, y, name=c.FIREFLOWER):
        super(FireFlower, self).__init__(x, y)
        self.setup_powerup(x, y, name, self.setup_frames)


    def setup_frames(self):
        """Define lista de quadro"""
        self.frames.append(
            self.get_image(0, 32, 16, 16))
        self.frames.append(
            self.get_image(16, 32, 16, 16))
        self.frames.append(
            self.get_image(32, 32, 16, 16))
        self.frames.append(
            self.get_image(48, 32, 16, 16))


    def handle_state(self):
        """Lidar com o comportamento com base no estado"""
        if self.state == c.REVEAL:
            self.revealing()
        elif self.state == c.RESTING:
            self.resting()


    def revealing(self):
        """Animação de flor saindo da caixa"""
        self.rect.y += self.y_vel

        if self.rect.bottom <= self.box_height:
            self.rect.bottom = self.box_height
            self.state = c.RESTING

        self.animation()


    def resting(self):
        """Flor de fogo, ficando ainda em aberto caixa"""
        self.animation()


    def animation(self):
        """Método para tornar o piscar da flor de fogo"""
        if (self.current_time - self.animate_timer) > 30:
            if self.frame_index < 3:
                self.frame_index += 1
            else:
                self.frame_index = 0

            self.image = self.frames[self.frame_index]
            self.animate_timer = self.current_time


class Star(Powerup):
    """Um powerup que dá invencibilidade do mario"""
    def __init__(self, x, y, name='star'):
        super(Star, self).__init__(x, y)
        self.setup_powerup(x, y, name, self.setup_frames)
        self.animate_timer = 0
        self.rect.y += 1  #Parece um deslocamento mais centrado do pixel
        self.gravity = .4


    def setup_frames(self):
        """Criando o self.frames lista onde as imagens para a animação 
são armazenados"""
        self.frames.append(self.get_image(1, 48, 15, 16))
        self.frames.append(self.get_image(17, 48, 15, 16))
        self.frames.append(self.get_image(33, 48, 15, 16))
        self.frames.append(self.get_image(49, 48, 15, 16))


    def handle_state(self):
        """Manipula o comportamento com base no estado"""
        if self.state == c.REVEAL:
            self.revealing()
        elif self.state == c.BOUNCE:
            self.bouncing()


    def revealing(self):
        """Quando a estrela sai da caixa"""
        self.rect.y += self.y_vel

        if self.rect.bottom <= self.box_height:
            self.rect.bottom = self.box_height
            self.start_bounce(-2)
            self.state = c.BOUNCE

        self.animation()


    def animation(self):
        """define a imagem para ver a animação"""
        if (self.current_time - self.animate_timer) > 30:
            if self.frame_index < 3:
                self.frame_index += 1
            else:
                self.frame_index = 0
            self.animate_timer = self.current_time
            self.image = self.frames[self.frame_index]


    def start_bounce(self, vel):
        """Transições em saltando de estado"""
        self.y_vel = vel


    def bouncing(self):
        """Ação, quando a estrela está saltando ao redor"""
        self.animation()

        if self.direction == c.LEFT:
            self.x_vel = -5
        else:
            self.x_vel = 5



class FireBall(pg.sprite.Sprite):
    """Tiro do fogo Mario"""
    def __init__(self, x, y, facing_right, name=c.FIREBALL):
        super(FireBall, self).__init__()
        self.sprite_sheet = setup.GFX['item_objects']
        self.setup_frames()
        if facing_right:
            self.direction = c.RIGHT
            self.x_vel = 12
        else:
            self.direction = c.LEFT
            self.x_vel = -12
        self.y_vel = 10
        self.gravity = .9
        self.frame_index = 0
        self.animation_timer = 0
        self.state = c.FLYING
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.right = x
        self.rect.y = y
        self.name = name


    def setup_frames(self):
        """Configura os quadros de animação"""
        self.frames = []

        self.frames.append(
            self.get_image(96, 144, 8, 8)) #Frame 1 of flying
        self.frames.append(
            self.get_image(104, 144, 8, 8))  #Frame 2 of Flying
        self.frames.append(
            self.get_image(96, 152, 8, 8))   #Frame 3 of Flying
        self.frames.append(
            self.get_image(104, 152, 8, 8))  #Frame 4 of flying
        self.frames.append(
            self.get_image(112, 144, 16, 16))   #frame 1 of exploding
        self.frames.append(
            self.get_image(112, 160, 16, 16))  #frame 2 of exploding
        self.frames.append(
            self.get_image(112, 176, 16, 16))  #frame 3 of exploding


    def get_image(self, x, y, width, height):
        """Se os quadros de imagem da folha de sprite"""

        image = pg.Surface([width, height]).convert()
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(c.BLACK)


        image = pg.transform.scale(image,
                                   (int(rect.width*c.SIZE_MULTIPLIER),
                                    int(rect.height*c.SIZE_MULTIPLIER)))
        return image


    def update(self, game_info, viewport):
        """Comportamento da bola de fogo de atualizações"""
        self.current_time = game_info[c.CURRENT_TIME]
        self.handle_state()
        self.check_if_off_screen(viewport)


    def handle_state(self):
        """Manipula o comportamento com base no estado"""
        if self.state == c.FLYING:
            self.animation()
        elif self.state == c.BOUNCING:
            self.animation()
        elif self.state == c.EXPLODING:
            self.animation()


    def animation(self):
        """ajusta o quadro de animação"""
        if self.state == c.FLYING or self.state == c.BOUNCING:
            if (self.current_time - self.animation_timer) > 200:
                if self.frame_index < 3:
                    self.frame_index += 1
                else:
                    self.frame_index = 0
                self.animation_timer = self.current_time
                self.image = self.frames[self.frame_index]


        elif self.state == c.EXPLODING:
            if (self.current_time - self.animation_timer) > 50:
                if self.frame_index < 6:
                    self.frame_index += 1
                    self.image = self.frames[self.frame_index]
                    self.animation_timer = self.current_time
                else:
                    self.kill()


    def explode_transition(self):
        """Bola de fogo de transições de estado e a explosão"""
        self.frame_index = 4
        centerx = self.rect.centerx
        self.image = self.frames[self.frame_index]
        self.rect.centerx = centerx
        self.state = c.EXPLODING


    def check_if_off_screen(self, viewport):
        """Remove o grupo de sprite se fora da tela"""
        if (self.rect.x > viewport.right) or (self.rect.y > viewport.bottom) \
            or (self.rect.right < viewport.x):
            self.kill()










