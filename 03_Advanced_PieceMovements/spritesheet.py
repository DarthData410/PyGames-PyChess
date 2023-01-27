import pygame
from settings import *

class SpriteSheet:

    def __init__(self,file,map) -> None:
        
        self.spritesheet_filename = file
        self.image = pygame.image.load(self.spritesheet_filename).convert_alpha()
        self.map = map

        self.sprite_images = dict()
        for row_index,row in enumerate(self.map):
            for col_index,col in enumerate(row):
                x = col_index * SW
                y = row_index * SH

                self.sprite_images[col]=self.image.subsurface(
                    x,y,SW,SH
                )
        
