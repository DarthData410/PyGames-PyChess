from rules_engine.pieces.piecebase import * 
from settings import * 

class Knight(PieceBase):

    def __init__(self, rules, piece) -> None:
        
        super().__init__(rules,piece)

    def generate_valid_moves(self) -> list:    
        
        ret = list()
        
        rk = self.piece.current_board_tile.row_key
        col = self.piece.current_board_tile.col

        opl = list()
        opl.append((col+1,rk+2)) # Down_Right
        opl.append((col-1,rk+2)) # Down_Left
        opl.append((col+1,rk-2)) # Up_Right
        opl.append((col-1,rk-2)) # Up_left
        
        opl.append((col+2,rk+1)) # Right_Down
        opl.append((col+2,rk-1)) # Right_Up
        opl.append((col-2,rk+1)) # Left_Down
        opl.append((col-2,rk-1)) # Left_Up
        
        def add_tile(col,row):
            tc = self.rules.board.get_tile_by_colrow(col,row)
            self.__valmoves__.append(tc.get_key())

        for t in opl:
            if self.tile_check(t[0],t[1]):
                add_tile(t[0],t[1])

        ret = self.__valmoves__
        return ret