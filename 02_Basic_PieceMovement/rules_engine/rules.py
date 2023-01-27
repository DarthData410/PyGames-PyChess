from settings import *
from piece import *
from rules_engine.pieces.pawn import * 
from rules_engine.pieces.rook import *
from rules_engine.pieces.knight import *
from rules_engine.pieces.bishop import *
from rules_engine.pieces.queen import *
from rules_engine.pieces.king import * 

class Rules:

    def __init__(self,board) -> None:
        
        self.board = board
        
        self.rulesmap = dict()
        self.single_move_dist=SMD_MAX
    
    def possible_moves(self,piece) -> list:
        
        ret = list()
        
        if piece.piece_type == PAWN:
            ret = Pawn(self,piece).get_moves()
        elif piece.piece_type == ROOK:
            ret = Rook(self,piece).get_moves()
        elif piece.piece_type == KNIGHT:
            ret = Knight(self,piece).get_moves()
        elif piece.piece_type == BISHOP:
            ret = Bishop(self,piece).get_moves()
        elif piece.piece_type == QUEEN:
            ret = Queen(self,piece).get_moves()
        elif piece.piece_type == KING:
            ret = King(self,piece).get_moves()
                  
        return ret
