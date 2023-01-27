from rules_engine.pieces.piecebase import * 
from settings import * 

class Queen(PieceBase):

    def generate_valid_moves(self) -> list:    
        
        ret = list()
        self.diags()
        self.columns()
        self.rows()
        ret = self.__valmoves__
        return ret