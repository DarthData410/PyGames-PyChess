import pygame
from settings import * 

class Piece(pygame.sprite.Sprite):

    def __init__(self, piecetype, side, board_tile, image, highlight_image, board_key, *groups) -> None:
        super().__init__(*groups)

        self.piece_type = piecetype
        self.side = side
        self.board_key = board_key
        
        self.image = image
        self.rect = self.image.get_rect(
                center=(
                    board_tile.rect.centerx,
                    board_tile.rect.centery
                )
            )

        self.highlight_image = highlight_image
        self.vector = pygame.math.Vector2(self.rect.x,self.rect.y)
        self.starting_board_tile = board_tile
        self.current_board_tile = board_tile
        self.previous_board_tile = board_tile
        self.has_moved = False
    
    def move_to_tile(self,bt):

        self.rect = self.image.get_rect(
            center=(
                bt.rect.centerx,
                bt.rect.centery
            )

        )
        
        self.vector = pygame.math.Vector2(self.rect.x,self.rect.y)
        self.previous_board_tile = self.current_board_tile
        self.current_board_tile = bt
        if not self.has_moved:
            self.has_moved = True
        

        

