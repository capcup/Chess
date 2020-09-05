'''
Responsible all the information about the current state of a chess game
& determining the valid moves at the current state.
Keeps a move log.
'''

import pygame as p
from Chess import ChessEngine

WIDTH = HEIGHT = 512 # or 400
DIMENSION = 8 # 8x8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15 # for animation
IMAGES = {}

'''

'''

# https://youtu.be/EnYui0e73Rs?t=1166