from rules_engine.pieces.piecebase import * 
from settings import * 

class Bishop(PieceBase):

    def __init__(self, rules, piece) -> None:
        
        super().__init__(rules,piece)

    def generate_valid_moves(self) -> list:    
        
        ret = list()
        self.diags()
        ret = self.__valmoves__
        return ret