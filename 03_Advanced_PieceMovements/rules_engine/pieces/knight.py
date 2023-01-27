from rules_engine.pieces.piecebase import * 
from settings import * 

class Knight(PieceBase):

    def generate_valid_moves(self) -> list:    
        
        ret = list()
        
        opl = Knight.knight_moves(self.piece)
        
        def add_tile(col,row):
            tc = self.rules.board.get_tile_by_colrow(col,row)
            self.__valmoves__.append(tc.get_key())

        for t in opl:
            if self.tile_check(t[0],t[1]):
                add_tile(t[0],t[1])

        ret = self.__valmoves__
        return ret
    
    def knight_moves(piece) -> list:
        ret = None
        rk = piece.current_board_tile.row_key
        col = piece.current_board_tile.col

        opl = list()
        opl.append((col+1,rk+2)) # Down_Right
        opl.append((col-1,rk+2)) # Down_Left
        opl.append((col+1,rk-2)) # Up_Right
        opl.append((col-1,rk-2)) # Up_left
        
        opl.append((col+2,rk+1)) # Right_Down
        opl.append((col+2,rk-1)) # Right_Up
        opl.append((col-2,rk+1)) # Left_Down
        opl.append((col-2,rk-1)) # Left_Up
        ret = opl
        return ret