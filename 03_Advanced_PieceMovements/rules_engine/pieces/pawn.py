from rules_engine.pieces.piecebase import * 
from settings import * 

class Pawn(PieceBase):

    def generate_valid_moves(self) -> list:    
        
        ret = list()

        if not self.piece.has_moved:
            # Facing Down:
            if self.piece.current_board_tile.row == ROW_KEY[1]:
                for k in self.rules.board.board_tiles:
                    bt = self.rules.board.board_tiles[k]
                    if bt.row == ROW_KEY[2] and bt.col == self.piece.current_board_tile.col:
                        if not self.rules.board.resolve_movement(bt):
                            ret.append(k)
                    
                    elif not self.piece.has_moved and bt.row == ROW_KEY[3] and bt.col == self.piece.current_board_tile.col:
                        if not self.rules.board.resolve_movement(bt):
                            # Check for not jumping over a piece right in front.:
                            tc = self.rules.board.get_tile_by_colrow(bt.col,(bt.row_key-1))
                            if not self.rules.board.resolve_movement(tc):
                                ret.append(k)
            
            # Facing Up:
            elif self.piece.current_board_tile.row == ROW_KEY[6]:
                for k in self.rules.board.board_tiles:
                    bt = self.rules.board.board_tiles[k]
                    if bt.row == ROW_KEY[5] and bt.col == self.piece.current_board_tile.col:
                        if not self.rules.board.resolve_movement(bt):
                            ret.append(k)
                    
                    elif not self.piece.has_moved and bt.row == ROW_KEY[4] and bt.col == self.piece.current_board_tile.col:
                        if not self.rules.board.resolve_movement(bt):
                            # Check for not jumping over a piece right in front.:
                            tc = self.rules.board.get_tile_by_colrow(bt.col,(bt.row_key+1))
                            if not self.rules.board.resolve_movement(tc):
                                ret.append(k)
        
        # Has moved:
        else:
            # Facing Down
            if self.piece.starting_board_tile.row == ROW_KEY[1]:
                for k in self.rules.board.board_tiles:
                    bt = self.rules.board.board_tiles[k]
                    if bt.row_key == (self.piece.current_board_tile.row_key+1) and bt.col == self.piece.current_board_tile.col:
                        if not self.rules.board.resolve_movement(bt):
                            ret.append(k)
            
            # Facing Up
            elif self.piece.starting_board_tile.row == ROW_KEY[6]:
                for k in self.rules.board.board_tiles:
                    bt = self.rules.board.board_tiles[k]
                    if bt.row_key == (self.piece.current_board_tile.row_key-1) and bt.col == self.piece.current_board_tile.col:
                        if not self.rules.board.resolve_movement(bt):
                            ret.append(k)
        
        # Possible Jumps
        for k in self.rules.board.board_tiles:
            ct = self.rules.board.board_tiles[k]
            # Facing Down:
            if self.piece.starting_board_tile.row == ROW_KEY[1]:
                if ct.row_key == (self.piece.current_board_tile.row_key+1) and (
                    ct.col == (self.piece.current_board_tile.col-1) or ct.col == (self.piece.current_board_tile.col+1)
                ):
                    if self.rules.board.resolve_movement(ct):
                        pc = self.rules.board.get_tile_piece(ct)
                        if self.piece.side != pc.side:
                            ret.append(k)
            # Facing Up:
            elif self.piece.starting_board_tile.row == ROW_KEY[6]:
                if ct.row_key == (self.piece.current_board_tile.row_key-1) and (
                    ct.col == (self.piece.current_board_tile.col-1) or ct.col == (self.piece.current_board_tile.col+1)
                ):
                    if self.rules.board.resolve_movement(ct):
                        pc = self.rules.board.get_tile_piece(ct)
                        if self.piece.side != pc.side:
                            ret.append(k)

        return ret

