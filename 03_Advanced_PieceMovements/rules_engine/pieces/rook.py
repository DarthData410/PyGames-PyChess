from rules_engine.pieces.piecebase import * 
from settings import * 

class Rook(PieceBase):

    def generate_valid_moves(self) -> list:    
        
        ret = list()
        self.columns()
        self.rows()

        ret = self.__valmoves__
        return ret