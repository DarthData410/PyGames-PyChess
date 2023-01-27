import pygame
from settings import * 

class Piece(pygame.sprite.Sprite):

    def __init__(self, piecetype, side, board_tile, image, *groups) -> None:
        super().__init__(*groups)

        self.piece_type = piecetype
        self.side = side
        
        self.image = image
        self.rect = self.image.get_rect(
                center=(
                    board_tile.rect.centerx,
                    board_tile.rect.centery
                )
            )
        
        self.vector = pygame.math.Vector2(self.rect.x,self.rect.y)
        

