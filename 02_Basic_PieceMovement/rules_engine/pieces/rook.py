from rules_engine.pieces.piecebase import * 
from settings import * 

class Rook(PieceBase):

    def __init__(self, rules, piece) -> None:
        
        super().__init__(rules,piece)

    def generate_valid_moves(self) -> list:    
        
        ret = list()
        self.columns()
        self.rows()

        ret = self.__valmoves__
        return ret