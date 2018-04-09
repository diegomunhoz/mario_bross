__author__ = 'Diego Vinicius de Mello Munhoz'

import sys
import cProfile
import pygame as pg
from data.main import main

if __name__ == '__main__':
    main()
    pg.quit()
    sys.exit()