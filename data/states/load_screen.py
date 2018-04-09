__author__ = 'Diego Vinicius de Mello Munhoz'

from .. import setup, tools
from .. import constants as c
from .. import game_sound
from ..components import info

class LoadScreen(tools._State):
    def __init__(self):
        tools._State.__init__(self)

    def startup(self, current_time, persist):
        self.start_time = current_time
        self.persist = persist
        self.game_info = self.persist
        self.next = self.set_next_state()

        info_state = self.set_overhead_info_state()

        self.overhead_info = info.OverheadInfo(self.game_info, info_state)
        self.sound_manager = game_sound.Sound(self.overhead_info)


    def set_next_state(self):
        """Configurando proximo estagio """
        return c.LEVEL1

    def set_overhead_info_state(self):
        """define o estado para enviar para o objeto que carrega as informações"""
        return c.LOAD_SCREEN


    def update(self, surface, keys, current_time):
        """Atualizando a tela"""
        if (current_time - self.start_time) < 2400:
            surface.fill(c.BLACK)
            self.overhead_info.update(self.game_info)
            self.overhead_info.draw(surface)

        elif (current_time - self.start_time) < 2600:
            surface.fill(c.BLACK)

        elif (current_time - self.start_time) < 2635:
            surface.fill((106, 150, 252))

        else:
            self.done = True




class GameOver(LoadScreen):
    """Carregamento da tela de game over"""
    def __init__(self):
        super(GameOver, self).__init__()


    def set_next_state(self):
        """Configurando proximo estado"""
        return c.MAIN_MENU

    def set_overhead_info_state(self):
        """Atualizando para fim do jogo"""
        return c.GAME_OVER

    def update(self, surface, keys, current_time):
        self.current_time = current_time
        self.sound_manager.update(self.persist, None)

        if (self.current_time - self.start_time) < 7000:
            surface.fill(c.BLACK)
            self.overhead_info.update(self.game_info)
            self.overhead_info.draw(surface)
        elif (self.current_time - self.start_time) < 7200:
            surface.fill(c.BLACK)
        elif (self.current_time - self.start_time) < 7235:
            surface.fill((106, 150, 252))
        else:
            self.done = True


class TimeOut(LoadScreen):
    """Carregando tela com fim do tempo"""
    def __init__(self):
        super(TimeOut, self).__init__()

    def set_next_state(self):
        """Passando para o proximo estagio"""
        if self.persist[c.LIVES] == 0:
            return c.GAME_OVER
        else:
            return c.LOAD_SCREEN

    def set_overhead_info_state(self):
        """Definindo o estágio com fim de tempo"""
        return c.TIME_OUT

    def update(self, surface, keys, current_time):
        self.current_time = current_time

        if (self.current_time - self.start_time) < 2400:
            surface.fill(c.BLACK)
            self.overhead_info.update(self.game_info)
            self.overhead_info.draw(surface)
        else:
            self.done = True