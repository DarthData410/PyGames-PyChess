from settings import *

class PieceBase:

    def __init__(self,rules=None,piece=None) -> None:
        
        self.piece = piece
        if self.piece != None:
            self.cbt = self.piece.current_board_tile
        self.rules = rules
        self.__valmoves__ = list()
        self.__opl__ = list()
        self.valid_moves = list()
        self.checked_keys = list()
    
    def get_checked_keys(self) -> list:
        return self.checked_keys
    def set_piece(self,piece):
        self.piece = piece
        self.cbt = self.piece.current_board_tile
    def set_rules(self,rules):
        self.rules = rules
    def get_moves(self) -> list:
        self.valid_moves = self.generate_valid_moves()
        return self.valid_moves
    def generate_valid_moves(self) -> list:
        return list()
    
    def base_check(self,col,row_key) -> tuple:
        ll = list()
        bret = False
        tc = self.rules.board.get_tile_by_colrow(col,row_key)             
        if not self.rules.board.resolve_movement(tc):
            ll.append(tc.get_key())
        else:
            if self.piece.side != self.rules.board.get_tile_piece(tc).side:
                ll.append(tc.get_key())
            bret = True
        ret = (bret,ll)    
        return ret
    
    def tile_check(self,col,row_key) -> bool:
        ret = False
        tc = self.rules.board.get_tile_by_colrow(col,row_key)
        if tc != None:              
            if not self.rules.board.resolve_movement(tc) or self.side_check(col,row_key):
                ret = True
        return ret
    
    def side_check(self,col,row) -> bool:
        ret = False
        tile_check = self.rules.board.get_tile_by_colrow(col,row)
        if tile_check != None:
            tp = self.rules.board.get_tile_piece(tile_check)
            if tp != None:
                if self.piece.side != tp.side:
                    ret = True
        return ret
    
    def column_check(self,start_key) -> bool:
        cret = False
        bktup = self.base_check(self.piece.current_board_tile.col,start_key)
        cret = bktup[0]
        l = bktup[1]
        for x in l:
            self.__valmoves__.append(x)
        return cret
        
    def row_check(self,start_col) -> bool:
        rret = False
        bktup = self.base_check(start_col,self.piece.current_board_tile.row_key)
        rret = bktup[0]
        l = bktup[1]
        for x in l:
            self.__valmoves__.append(x)
        return rret
    
    def diags(self,limit=0):
        rk = self.piece.current_board_tile.row_key
        col = self.piece.current_board_tile.col
        
        def build_opl(t) -> bool:
            ret = False
            if self.tile_check(tup[0],tup[1]):
                self.__opl__.append(tup)
                if self.side_check(tup[0],tup[1]):
                    ret = True
            else:
                ret = True
            return ret

        bounds = len(ROW_KEY) if limit == 0 else limit
        # Down Right:
        x=0
        while x < bounds:
            tup = ((col+1)+(x),(rk+1)+(x))
            if build_opl(tup):
                break
            x += 1
        
        # Up Left:
        x=0
        while x < bounds:
            tup = ((col-1)-(x),(rk-1)-(x))
            if build_opl(tup):
                break
            x += 1
        
        # Down Left:
        x=0
        while x < bounds:
            tup = ((col-1)-(x),(rk+1)+(x))
            if build_opl(tup):
                break
            x += 1
        
        # Up Right:
        x=0
        while x < bounds:
            tup = ((col+1)+(x),(rk-1)-(x))
            if build_opl(tup):
                break
            x += 1

        for t in self.__opl__:
            tc = self.rules.board.get_tile_by_colrow(t[0],t[1])
            self.__valmoves__.append(tc.get_key())
    
    def columns(self,limit=0):
        
        i = self.piece.current_board_tile.row_key+1
        bounds = len(ROW_KEY)
        
        if limit == 0:    
            while i < bounds:
                if self.column_check(i):
                    break
                i += 1
        else:
            if i < bounds:
                self.column_check(i)

        # UP:
        i = self.piece.current_board_tile.row_key-1
        c = 0
        while i >= 0:
            if self.column_check(i):
                break
            c += 1
            if limit > 0 and c >= limit:
                break
            i -= 1
        
    def rows(self,limit=0):
        i = self.piece.current_board_tile.col+1
        bounds = len(ROW_KEY)
        # RIGHT
        if limit == 0:
            while i < bounds:
                if self.row_check(i):
                    break
                i += 1
        else:
            if i < bounds:
                self.row_check(i)

        # LEFT
        i = self.piece.current_board_tile.col-1
        if limit == 0:
            while i >= 0:
                if self.row_check(i):
                    break
                i -= 1
        else:
            if i >= 0:
                self.row_check(i)
    
    def first_move(self,col,row) -> bool:
        fmret = False
        tc = self.rules.board.get_tile_by_colrow(col,row)
        if self.rules.board.resolve_movement(tc):
            fmret = True
        return fmret

    def add_to_moves(self,t):
        self.__valmoves__.append(t.get_key())
    
