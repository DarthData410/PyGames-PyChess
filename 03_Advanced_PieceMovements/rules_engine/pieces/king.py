from rules_engine.pieces.piecebase import * 
from settings import * 

class King(PieceBase):

    def is_checkbase(self,piece_types) -> bool:
        ret = False
        for k in self.__valmoves__:
            tc = self.rules.board.get_tile_by_key(k)
            tp = self.rules.board.get_tile_piece(tc)
            if tp != None:
                if tp.side != self.piece.side:
                    
                    # Based on piece type:
                    if piece_types.__contains__(tp.piece_type):
                        self.checked_keys.append(k)
                        ret = True
                        break
        return ret
    
    def is_check(self,args) -> bool:
        ret = False

        self.__valmoves__.clear()
        # rook and queen
        self.columns()
        self.rows()

        ret = self.is_checkbase([QUEEN,ROOK])
        self.__valmoves__.clear()
        
        # bishop and queen:
        if not ret:
            self.__valmoves__.clear()

            self.diags()
            ret = self.is_checkbase([QUEEN,BISHOP])

        # pawn and single diagonal bishop and queen:
        if not ret:
            self.__valmoves__.clear()

            def pawn_check(c,r) -> bool:
                pcret = False
                colc = self.piece.current_board_tile.col+c
                rowc = self.piece.current_board_tile.row_key+r
                tc = self.rules.board.get_tile_by_colrow(colc,rowc)
                if tc != None:
                    self.__valmoves__.append(tc.get_key())
                    pcret = True
                return pcret

            pawn_check(1,1)
            pawn_check(1,-1)
            pawn_check(-1,-1)
            pawn_check(-1,1)

            ret = self.is_checkbase([PAWN])
        
        # knight:
        if not ret:
            self.__valmoves__.clear()

            knight_moves = self.rules.knightmoves(self.piece)
            for k in knight_moves:
                knc = self.rules.board.get_tile_by_colrow(k[0],k[1])
                kncp = self.rules.board.get_tile_piece(knc)
                if kncp != None:
                    if kncp.piece_type == KNIGHT:
                        if self.side_check(k[0],k[1]):
                            ret = True
                            self.checked_keys.append(knc.get_key())
                            break
        return ret

    def is_castle(self,args) -> bool:
        ret = False
        col = args[0]
        row_key = args[1]
        # King Side:
        if col == self.cbt.col+2 and row_key == self.cbt.row_key:
            ret = True
        # Queen Side:
        elif col == self.cbt.col-2 and row_key == self.cbt.row_key:
            ret = True
        else:
            ret = False
        return ret

    def incheck(self) -> bool:
        ret = False
        if self.piece.side == WHT:
            ret = self.rules.board.white_in_check
        else:
            ret = self.rules.board.black_in_check
        return ret

    def castle(self):

        if not self.piece.has_moved and not self.incheck():
            tcr = self.tile_check(self.cbt.col+2,self.cbt.row_key)
            # Castle King side:
            if tcr:
                rkt = self.rules.board.get_tile_by_colrow(
                        self.cbt.col+3,self.cbt.row_key
                    )
                rp = self.rules.board.get_tile_piece(rkt)
                if rp != None and not rp.has_moved:
                    br = self.rules.board.get_tile_by_colrow(
                        self.cbt.col+2,self.cbt.row_key
                    )
                    self.add_to_moves(br)

            tcl = self.tile_check(self.cbt.col-2,self.cbt.row_key)
            # Castle Queen side:
            if tcl:
                rkt = self.rules.board.get_tile_by_colrow(
                        self.cbt.col-4,self.cbt.row_key
                    )
                rp = self.rules.board.get_tile_piece(rkt)
                if rp != None and not rp.has_moved:
                    # Check Queen side for piece in Queen Side Knight Home.:
                    qsknc = self.rules.board.get_tile_by_colrow(
                        self.cbt.col-3,self.cbt.row_key
                    )
                    if not self.rules.board.resolve_movement(qsknc):
                        bl = self.rules.board.get_tile_by_colrow(
                            self.cbt.col-2,self.cbt.row_key
                        )
                        self.add_to_moves(bl)

    def generate_valid_moves(self) -> list:    
        
        ret = list()
        self.diags(limit=1)
        self.columns(limit=1)
        self.rows(limit=1)
        
        # Check for ability to castle:
        self.castle()
        
        ret = self.__valmoves__
        return ret