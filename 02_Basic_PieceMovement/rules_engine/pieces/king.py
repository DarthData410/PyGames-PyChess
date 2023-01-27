from rules_engine.pieces.piecebase import * 
from settings import * 

class King(PieceBase):

    def __init__(self, rules, piece) -> None:
        
        super().__init__(rules,piece)

    def generate_valid_moves(self) -> list:    
        
        ret = list()
        self.diags(limit=1)
        self.columns(limit=1)
        self.rows(limit=1)
        ret = self.__valmoves__
        return ret