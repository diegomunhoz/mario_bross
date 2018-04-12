__author__ = 'Diego Vinicius de Mello Munhoz'

#DEFINIÇÕES DE TELA
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

TITLE = "Super Mário Bross - desenvolved by Diego Vinicius de Mello Munhoz"

#CORES RGB
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GRAY = (100, 100, 100)
NAVYBLUE     = ( 60,  60, 100)
GREEN        = (  0, 255,   0)
FOREST_GREEN = ( 31, 162,  35)
BLUE         = (  0,   0, 255)
SKY_BLUE     = ( 39, 145, 251)
YELLOW       = (255, 255,   0)
ORANGE       = (255, 128,   0)
PURPLE       = (255,   0, 255)
CYAN         = (  0, 255, 255)
BLACK        = (  0,   0,   0)
NEAR_BLACK    = ( 19,  15,  48)
COMBLUE      = (233, 232, 255)
GOLD         = (255, 215,   0)

BGCOLOR = WHITE

SIZE_MULTIPLIER = 2.5
BRICK_SIZE_MULTIPLIER = 2.69
BACKGROUND_MULTIPLER = 2.679
GROUND_HEIGHT = SCREEN_HEIGHT - 62

#MARIO FORÇAS
WALK_ACCEL = .15
RUN_ACCEL = 20
SMALL_TURNAROUND = .35

GRAVITY = 1.01
JUMP_GRAVITY = .31
JUMP_VEL = -10
FAST_JUMP_VEL = -12.5
MAX_Y_VEL = 11

MAX_RUN_SPEED = 800
MAX_WALK_SPEED = 6


#MARIO ESTADOS
STAND = 'standing' 
WALK = 'walk'
JUMP = 'jump'
FALL = 'fall'
SMALL_TO_BIG = 'small to big'
BIG_TO_FIRE = 'big to fire'
BIG_TO_SMALL = 'big to small'
FLAGPOLE = 'flag pole'
WALKING_TO_CASTLE = 'walking to castle'
END_OF_LEVEL_FALL = 'end of level fall'

#ESTADOS DE POSIÇÃO
LEFT = 'left'
RIGHT = 'right'
JUMPED_ON = 'jumped on'
DEATH_JUMP = 'death jump'

SHELL_SLIDE = 'shell slide'

#ESTADO DOS TIJOLOS
RESTING = 'resting'
BUMPED = 'bumped'

#MOEDAS
OPENED = 'opened'

#ESTADOS DE COGUMELOS
REVEAL = 'reveal'
SLIDE = 'slide'

#ESTADOS DE MOEDAS
SPIN = 'spin'

#ESTADO ESTRELAS
BOUNCE = 'bounce'

#ESTADOS DE FOGO E EXPLOSÃO
FLYING = 'flying'
BOUNCING = 'bouncing'
EXPLODING = 'exploding'

#CONTEUDO DAS CAIXAS E MOEDAS
MUSHROOM = 'mushroom'
STAR = 'star'
FIREFLOWER = 'fireflower'
SIXCOINS = '6coins'
COIN = 'coin'
LIFE_MUSHROOM = '1up_mushroom'

FIREBALL = 'fireball'

#LISTA DE INIMIGOS
GOOMBA = 'goomba'
KOOPA = 'koopa'

#ESTADOS DOS NIVEIS
FROZEN = 'frozen'
NOT_FROZEN = 'not frozen'
IN_CASTLE = 'in castle'
FLAG_AND_FIREWORKS = 'flag and fireworks'

#ESTADO DA BANDEIRA
TOP_OF_POLE = 'top of pole'
SLIDE_DOWN = 'slide down'
BOTTOM_OF_POLE = 'bottom of pole'

#1UP PONTOS
ONEUP = '379'

#MAIN MENU ESTADOS DO CURSOR
PLAYER1 = '1 player'
PLAYER2 = '2 player'

#ESTADOS DE CARREGAMENTO DE INFORMAÇÕES
MAIN_MENU = 'main menu'
LOAD_SCREEN = 'loading screen'
LEVEL = 'level'
GAME_OVER = 'game over'
FAST_COUNT_DOWN = 'fast count down'
END_OF_LEVEL = 'end of level'

#INFORMAÇÕES DE TEXTOS DO JOGO
COIN_TOTAL = 'coin total'
SCORE = 'score'
TOP_SCORE = 'top score'
LIVES = 'lives'
CURRENT_TIME = 'current time'
LEVEL_STATE = 'level state'
CAMERA_START_X = 'camera start x'
MARIO_DEAD = 'mario dead'

#ESTADOS DA ENGINE DO JOGO
MAIN_MENU = 'main menu'
LOAD_SCREEN = 'load screen'
TIME_OUT = 'time out'
GAME_OVER = 'game over'
LEVEL1 = 'level1'

#ESTADOS DOS SONS
NORMAL = 'normal'
STAGE_CLEAR = 'stage clear'
WORLD_CLEAR = 'world clear'
TIME_WARNING = 'time warning'
SPED_UP_NORMAL = 'sped up normal'
MARIO_INVINCIBLE = 'mario invincible'