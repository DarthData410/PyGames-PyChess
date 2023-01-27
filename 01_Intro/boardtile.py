import pygame
from settings import * 

class BoardTile(object):

    def __init__(self, pos, width, height):

        self.pos = pos
        self.width = width
        self.height = height

        self.rect = pygame.Rect(pos+(width,height))
