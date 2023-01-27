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
        self.current_checked_keys = list()
        self.current_checkmate = CheckMate.NONE
    
    def possible_moves(self,piece) -> list:
        
        ret = list()
        
        obj = eval(f'{piece.piece_type}()')
        obj.set_rules(self)
        obj.set_piece(piece)
        f = getattr(obj,'get_moves')
        ret = f()

        return ret
    
    def rule_check(self,piece,func,args)-> bool:
        ret = False
        
        obj = eval(f'{piece.piece_type}()')
        obj.set_rules(self)
        obj.set_piece(piece)
        f = getattr(obj,func)
        ret = f(args)
        f = getattr(obj,'get_checked_keys')
        self.current_checked_keys = f()

        return ret
    
    def get_kingpiece(self,same_side=False):

        ret = None
        for k in self.board.board_tiles:
            bt = self.board.board_tiles[k]
            kp = self.board.get_tile_piece(bt)
            if kp != None:
                if kp.piece_type == KING:
                    if same_side and kp.side == self.board.piece_to_move.side:
                        ret = kp
                    elif not same_side and kp.side != self.board.piece_to_move.side:
                        ret = kp
        return ret
        

    def is_check(self,same_side=False) -> bool:
        ret = False

        func = 'is_check'
        kp = self.get_kingpiece(same_side)
        ret = self.rule_check(kp,func,(0,0))

        if ret:
            print(f'King {kp.side} in check')
        return ret

    def valid_outofcheck_moves(self,piece) -> list:
        
        lpm = list()

        ret = self.possible_moves(piece)
        kp = self.get_kingpiece(same_side=True)
        if kp == piece:
            issame=True
        else:
            issame=False
        kptk = kp.current_board_tile.get_colrow_key()
        # Check to see if possible moves will remove king from check.:
        for k in ret:
            ct = self.board.get_tile_by_key(k)
            ct_crk = ct.get_colrow_key()
            ca = self.valid_outofcheck_isgood(ct_crk,kptk,issame)
            if ca: 
                lpm.append(k)

        return lpm
    
    def valid_outofcheck_isgood(self,k,kptk,isking=False) -> bool:
        ret = False
        same = False

        def val_comp(val,i) -> bool:
            ret = False
            # KeyCheck, Row_Key Greater than KingPiece Tile Row_Key:
            if val[i] > kptk[i]:
                if k[i] > kptk[i] and k[i] < val[i]:
                    ret = True
            # KeyCheck, Row_Key less than KingPiece Tile Row_Key:
            if val[i] < kptk[i]:
                if k[i] < kptk[i] and k[i] > val[i]:
                    ret = True
            # KeyCheck, Row_Key equal to KingPiece Tile Row_Key:
            if val[i] == kptk[i]:
                if k[i] == kptk[i]:
                    ret = True
            return ret

        for kc in self.current_checked_keys:
            kc_crt = self.board.get_tile_by_key(kc)
            kc_crp = self.board.get_tile_piece(kc_crt)
            if kc_crp.piece_type == KNIGHT:
                print("IS_KNIGHT")
            kc_crk = kc_crt.get_colrow_key()
            if k == kc_crk:
                ret = True
                same = True
            else:
                ret = val_comp(kc_crk,1) # Row
                ret = ret and val_comp(kc_crk,0) # Col
        
        if not same:
            if isking and ret:
                ret = False
            elif isking and not ret:
                ret = True

        return ret 

    def knightmoves(self,piece):
        return Knight.knight_moves(piece)
    
    def is_castle() -> str:
        return 'is_castle'
    def castle_rook(board,king_tile) -> tuple:
        ret = (0,0)
        
        if king_tile.col == KRCOL:
            p = board.get_tile_by_colrow(KRH,board.piece_to_move.current_board_tile.row_key)
            ret = (KRS,0)
        elif king_tile.col == QRCOL:
            p = board.get_tile_by_colrow(QRH,board.piece_to_move.current_board_tile.row_key)
            ret = (QRS,0)
        
        ret = (ret[0],board.get_tile_piece(p))

        return ret


