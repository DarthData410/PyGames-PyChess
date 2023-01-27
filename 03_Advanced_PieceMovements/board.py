import pygame
from settings import * 
from boardtile import * 
from piece import *
from spritesheet import * 
from rules_engine.rules import *

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

        self.board_buffer = (
            (self.display.get_width()-self.background.get_width()) // 2,
            (self.display.get_height()-self.background.get_height()) // 2 
        )

        self.board_tiles = dict()
        self.pieces = dict()
        self.draw_sprites = pygame.sprite.Group()
        self.draw_highlight_sprites = pygame.sprite.Group()
        self.piece_map = PIECE_MAP
        self.spritesheet = SpriteSheet(PIECES_SPRITESHEET,SS_MAP)
        self.spritesheet_highlight = SpriteSheet(PIECES_HIGHLIGHT_SPRITESHEET,SSH_MAP)
        self.has_init=False
        self.reverse_it = False
        self.draw_possible_moves = True # NOTE: Add logic to turn off / on.
        self.draw_board()
        self.piece_to_move = None

        self.rules = Rules(self)
        self.current_possible_moves = list()
        self.pieces_jumped = list()

        self.current_turn=WHT
        self.black_in_check=False
        self.white_in_check=False
    
    def next_turn(self):
        
        if self.piece_to_move.side == WHT:
            self.current_turn = BLK
        else:
            self.current_turn = WHT
    
    def check_turn(self):
        ret = False

        if self.piece_to_move.side == self.current_turn:
            ret = True
        
        return ret
    
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
            buffer = self.board_buffer
            
            for row_index,row in enumerate(INITIAL_BOARD):
                for col_index,col in enumerate(row):
                    
                    x = (col_index * TILE[0]) + buffer[0]
                    y = (row_index * TILE[1]) + buffer[1]
                    
                    pos = (x,y)
                    b = BoardTile(row_index,ROW_KEY[row_index],col_index,pos,TILE[0],TILE[1])
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
                            bk = PIECE_BOARD_KEY[col]
                            
                            p = Piece(
                                pc,
                                clr,
                                bd,
                                self.spritesheet.sprite_images[pc+clr],
                                self.spritesheet_highlight.sprite_images[pc],
                                bk,
                                [self.draw_sprites]
                            )
                            
                            bk += 1
                            PIECE_BOARD_KEY[col] = bk
                            self.pieces[(x,y)]=p
                    
            self.has_init = True
            self.reverse_it = False
        
    def highlight_possible_moves(self):

        if self.draw_possible_moves:
            self.draw_highlight_sprites.empty()

            for k in self.current_possible_moves:
                bt = self.board_tiles[k]

                tpc = self.get_tile_piece(bt) 
                if tpc != None:
                    pygame.draw.rect(
                        surface=self.display,
                        color=HLCLR,
                        rect=bt.rect,
                        width=HLW
                    )
                else:
                    s = pygame.sprite.Sprite(self.draw_highlight_sprites)
                    s.image = self.piece_to_move.highlight_image
                    s.rect = s.image.get_rect(
                        center=(
                            bt.rect.centerx,
                            bt.rect.centery
                        )
                    )
            
            self.draw_highlight_sprites.draw(self.display)
    
    def resolve_movement(self,target_tile) -> bool:
        """ Returns True if target tile has a piece already on it, False if not """
        ret = False

        for s in self.draw_sprites:
            if s.current_board_tile == target_tile:
                ret = True
                break

        return ret
    
    def get_tile_piece(self,target_tile) -> Piece:
        
        ret = None
        
        for s in self.draw_sprites:
            if s.current_board_tile == target_tile:
                ret = s
                break
        
        return ret
    
    def get_tile_by_colrow(self,col,row_key) -> BoardTile:

        ret = None

        for b in self.board_tiles:
            bt = self.board_tiles[b]
            if bt.row_key == row_key and bt.col == col:
                ret = bt
                break

        return ret 
    
    def get_tile_by_key(self,key) -> BoardTile:

        ret = None
        ret = self.board_tiles[key]
        return ret

    def incheck(self,sc=None) -> bool:
        ret = False
        side = self.piece_to_move.side
        
        if sc==None:
            if side == WHT:
                if self.white_in_check:
                    ret = True
            else:
                if self.black_in_check:
                    ret = True
        else:
            if sc == WHT:
                self.white_in_check = False
            else:
                self.black_in_check = False
        
        return ret
    
    def set_check(self):
        # is_check after move, against opposing king:
            if self.rules.is_check():
                if self.piece_to_move.side == WHT:
                    self.black_in_check = True
                else:
                    self.white_in_check = True
            else:
                if self.piece_to_move.side == WHT and self.black_in_check:
                    self.black_in_check = False
                elif self.piece_to_move.side == BLK and self.white_in_check:
                    self.white_in_check = False
    
    def load_piece_tomove(self, mouse_pos):
        
        for s in self.draw_sprites:
            if s.rect.collidepoint(mouse_pos):
                self.piece_to_move = s
                if self.check_turn():
                    if self.incheck():
                        self.rules.is_check(True)
                        self.current_possible_moves = self.rules.valid_outofcheck_moves(self.piece_to_move)
                        if len(self.current_possible_moves)<=0:
                            self.piece_to_move = None
                            print('KING in CHECK. Must move out of check...')
                        #else:
                        #    print(f'Moving from {s.current_board_tile.tile_str()}')
                    else:
                        self.current_possible_moves = self.rules.possible_moves(self.piece_to_move)
                        if len(self.current_possible_moves)<=0:
                            self.piece_to_move = None
                            print('No possible moves...')
                        #else:
                        #    print(f'Moving from {s.current_board_tile.tile_str()}')
                else:
                    print(f"NOT YOUR TURN. Currently {self.current_turn} turn")
                    self.piece_to_move = None
                break

    def try_tomove(self,mouse_pos):
        
        for k in self.board_tiles:
            bt = self.board_tiles[k]
            if bt.rect.collidepoint(mouse_pos):
                    
                if self.current_possible_moves.__contains__(k):
                        
                    # Check for existing piece, and 'jump' it.:
                    if self.get_tile_piece(bt) != None:
                        p2r = self.get_tile_piece(bt)
                        self.draw_sprites.remove(p2r)
                        self.pieces_jumped.append(p2r)
                        print(f'Piece Jumped: {p2r.piece_type}-{p2r.side} @ ({p2r.current_board_tile.row},{p2r.current_board_tile.col})')
                        
                    if self.piece_to_move.piece_type == KING:
                        args = (bt.col,bt.row_key)
                        if self.rules.rule_check(self.piece_to_move,Rules.is_castle(),args) and not self.incheck():
                            #print("Is Castle...")
                            self.piece_to_move.move_to_tile(bt)
                            krtup = Rules.castle_rook(self,bt)
                            r = krtup[1]
                            r.move_to_tile(
                                self.get_tile_by_colrow(
                                    krtup[0],
                                    r.current_board_tile.row_key
                                )
                            )
                        else:
                            self.piece_to_move.move_to_tile(bt)
                            if self.incheck():
                                self.incheck(self.piece_to_move.side)
                    else:
                        self.piece_to_move.move_to_tile(bt)
                        #print(f'Moved to {self.piece_to_move.current_board_tile.tile_str()}')

                        if self.piece_to_move.piece_type != KING: 
                            self.set_check()
                        
                    if self.piece_to_move.piece_type == KING and self.incheck():
                        self.incheck(self.piece_to_move.side)
                        #print('Moving out of check...')

                    self.next_turn()

                else:
                    print("NOT A VALID MOVE")

                self.piece_to_move = None
                self.current_possible_moves = list()
                break

    def move_piece(self,mouse_pos):

        if self.piece_to_move == None:
            # Load a piece to move.:    
            self.load_piece_tomove(mouse_pos)
        else:
            # Check for tile to move to:
            self.try_tomove(mouse_pos)
                    
    def run(self):

        # update and draw chess board, and pieces:
        self.display.blit(self.background,self.background_rect)
        self.draw_board()
        self.highlight_possible_moves()
        self.draw_sprites.draw(self.display)
        self.draw_sprites.update()
        