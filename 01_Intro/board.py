import pygame
from settings import * 
from boardtile import * 
from piece import *
from spritesheet import * 

class Board:

    def __init__(self) -> None:
        
        self.display = pygame.display.get_surface()
        self.background = pygame.image.load(DEFAULT_BOARD).convert()
        self.background_rect = self.background.get_rect(
            center=(
                (
                    (self.display.get_width() // 2),
                    (self.display.get_height() // 2)
                )
            )
        )

        self.board_tiles = dict()
        self.pieces = dict()
        self.draw_sprites = pygame.sprite.Group()
        self.piece_map = PIECE_MAP
        self.spritesheet = SpriteSheet()
        self.has_init=False
        self.reverse_it = False
        self.draw_board()
    
    def draw_board(self):

        if self.reverse_it:
            if len(self.board_tiles) > 0:
                for k in self.board_tiles:
                    bt = self.board_tiles[k]
                    del bt
                self.board_tiles = dict()
            
            if len(self.pieces) > 0:
                for k in self.pieces:
                    pec = self.pieces[k]
                    self.draw_sprites.remove(pec)
                    del pec
                self.pieces = dict()
            self.piece_map.reverse()
            
        if not self.has_init or (self.has_init and self.reverse_it):
            pos = (0,0)
            buffer = (30,30)
            
            for row_index,row in enumerate(INITIAL_BOARD):
                for col_index,col in enumerate(row):
                    
                    x = (col_index * TILE[0]) + buffer[0]
                    y = (row_index * TILE[1]) + buffer[1]
                    
                    pos = (x,y)
                    b = BoardTile(pos,TILE[0],TILE[1])
                    self.board_tiles[(x,y)]=b
            
            for row_index,row in enumerate(self.piece_map):
                for col_index,col in enumerate(row):
                    
                    x = (col_index * TILE[0]) + buffer[0]
                    y = (row_index * TILE[1]) + buffer[1]
                    
                    # Find Piece Match:
                    clr = ''
                    pc=''
    
                    if col != NOKEY:
                        nptup = NAMED_PIECES[col]
                        pc = nptup[0]
                        clr = nptup[1]
                            
                        if clr != '' and pc != '':
                            bd = self.board_tiles[(x,y)]
                            p = Piece(pc,clr,bd,self.spritesheet.sprite_images[pc+clr],self.draw_sprites)
                            self.pieces[(x,y)]=p
                    
            self.has_init = True
            self.reverse_it = False
        
    
    def run(self):

        # update and draw chess board, and pieces:
        self.display.fill((0,0,0))
        self.display.blit(self.background,self.background_rect)
        self.draw_board()
        self.draw_sprites.draw(self.display)
        self.draw_sprites.update()