import pygame
from settings import * 

class BoardTile(object):

    def __init__(self, row_key, row, col, pos, width, height):

        self.row_key = row_key
        self.row = row
        self.col = col
        self.pos = pos
        self.width = width
        self.height = height

        self.rect = pygame.Rect(pos+(width,height))
        self.vector = pygame.math.Vector2(self.rect.x,self.rect.y)
    
    def tile_str(self):
        return f'{self.row}{self.col}'
    def get_key(self) -> tuple:
        return self.pos

