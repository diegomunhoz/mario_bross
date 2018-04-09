__author__ = 'Diego Vinicius de Mello Munhoz'

import pygame as pg
from .. import setup
from .. import constants as c


class Enemy(pg.sprite.Sprite):
    """Classe base para todos os inimigos (Goombas, Koopas, etc.)"""
    def __init__(self):
        pg.sprite.Sprite.__init__(self)


    def setup_enemy(self, x, y, direction, name, setup_frames):
        """Define vários valores para o inimigo"""
        self.sprite_sheet = setup.GFX['smb_enemies_sheet']
        self.frames = []
        self.frame_index = 0
        self.animate_timer = 0
        self.death_timer = 0
        self.gravity = 1.5
        self.state = c.WALK

        self.name = name
        self.direction = direction
        setup_frames()

        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.bottom = y
        self.set_velocity()


    def set_velocity(self):
        """Define o vetor velocidade com base na direção"""
        if self.direction == c.LEFT:
            self.x_vel = -2
        else:
            self.x_vel = 2

        self.y_vel = 0


    def get_image(self, x, y, width, height):
        """Se os quadros de imagem da folha de sprit"""
        image = pg.Surface([width, height]).convert()
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(c.BLACK)


        image = pg.transform.scale(image,
                                   (int(rect.width*c.SIZE_MULTIPLIER),
                                    int(rect.height*c.SIZE_MULTIPLIER)))
        return image


    def handle_state(self):
        """Comportamento inimigo com base no estado"""
        if self.state == c.WALK:
            self.walking()
        elif self.state == c.FALL:
            self.falling()
        elif self.state == c.JUMPED_ON:
            self.jumped_on()
        elif self.state == c.SHELL_SLIDE:
            self.shell_sliding()
        elif self.state == c.DEATH_JUMP:
            self.death_jumping()


    def walking(self):
        """Estado padrão de mover-se para o lado"""
        if (self.current_time - self.animate_timer) > 125:
            if self.frame_index == 0:
                self.frame_index += 1
            elif self.frame_index == 1:
                self.frame_index = 0

            self.animate_timer = self.current_time


    def falling(self):
        """Para quando ele cai de um precipício"""
        if self.y_vel < 10:
            self.y_vel += self.gravity


    def jumped_on(self):
        """Espaço reservado para quando o inimigo é pisoteado"""
        pass


    def death_jumping(self):
        """Animação de morte"""
        self.rect.y += self.y_vel
        self.rect.x += self.x_vel
        self.y_vel += self.gravity

        if self.rect.y > 600:
            self.kill()


    def start_death_jump(self, direction):
        """Inimigo de transições em um estado de morte saltar"""
        self.y_vel = -8
        if direction == c.RIGHT:
            self.x_vel = 2
        else:
            self.x_vel = -2
        self.gravity = .5
        self.frame_index = 3
        self.image = self.frames[self.frame_index]
        self.state = c.DEATH_JUMP


    def animation(self):
        """Animação básica, alternando entre dois quadros"""
        self.image = self.frames[self.frame_index]


    def update(self, game_info, *args):
        """Comportamento inimigo de atualizações"""
        self.current_time = game_info[c.CURRENT_TIME]
        self.handle_state()
        self.animation()




class Goomba(Enemy):

    def __init__(self, y=c.GROUND_HEIGHT, x=0, direction=c.LEFT, name='goomba'):
        Enemy.__init__(self)
        self.setup_enemy(x, y, direction, name, self.setup_frames)


    def setup_frames(self):
        """Colocar os quadros de imagem em uma lista para ser animado."""

        self.frames.append(
            self.get_image(0, 4, 16, 16))
        self.frames.append(
            self.get_image(30, 4, 16, 16))
        self.frames.append(
            self.get_image(61, 0, 16, 16))
        self.frames.append(pg.transform.flip(self.frames[1], False, True))


    def jumped_on(self):
        """Quando Mario espreme-lo"""
        self.frame_index = 2

        if (self.current_time - self.death_timer) > 500:
            self.kill()



class Koopa(Enemy):

    def __init__(self, y=c.GROUND_HEIGHT, x=0, direction=c.LEFT, name='koopa'):
        Enemy.__init__(self)
        self.setup_enemy(x, y, direction, name, self.setup_frames)


    def setup_frames(self):
        """Lista de quadro"""
        self.frames.append(
            self.get_image(150, 0, 16, 24))
        self.frames.append(
            self.get_image(180, 0, 16, 24))
        self.frames.append(
            self.get_image(360, 5, 16, 15))
        self.frames.append(pg.transform.flip(self.frames[2], False, True))


    def jumped_on(self):
        """Quando Mario salta sobre o Koopa e coloca-lo em sua concha"""
        self.x_vel = 0
        self.frame_index = 2
        shell_y = self.rect.bottom
        shell_x = self.rect.x
        self.rect = self.frames[self.frame_index].get_rect()
        self.rect.x = shell_x
        self.rect.bottom = shell_y


    def shell_sliding(self):
        """Quando o koopa está deslizando ao longo do solo em sua concha"""
        if self.direction == c.RIGHT:
            self.x_vel = 10
        elif self.direction == c.LEFT:
            self.x_vel = -10



















