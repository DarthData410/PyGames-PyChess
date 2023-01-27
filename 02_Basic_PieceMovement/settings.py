
CAP='Battle Chess | @PyFryDay'
WIDTH=900
HEIGHT=900
FPS=30

DEFAULT_BOARD='./graphics/backgrounds/center_board_840x840_blue.png'
GRAPHICS='./graphics'
PIECES='/pieces/'
PEXT='.png'
SW=64
SH=64
TILE=(105,105)
SMD_MAX=105
PIECES_SPRITESHEET=GRAPHICS+PIECES+'pieces_spritesheet_64x64.png'

# Named Pieces:
# Sides
NAMED_PIECES=dict()
NOKEY=-1
BLACK=100
BLK='_black_'
WHITE=200
WHT='_white_'
DWN='down'
UP='up'
# Numbered pieces
ROOKN=1
B_R=BLACK+ROOKN
W_R=WHITE+ROOKN
ROOK='rook'
NAMED_PIECES[B_R]=(ROOK,BLK)
NAMED_PIECES[W_R]=(ROOK,WHT)

KNIGHTN=2
B_KN=BLACK+KNIGHTN
W_KN=WHITE+KNIGHTN
KNIGHT='knight'
NAMED_PIECES[B_KN]=(KNIGHT,BLK)
NAMED_PIECES[W_KN]=(KNIGHT,WHT)

BISHOPN=3
B_B=BLACK+BISHOPN
W_B=WHITE+BISHOPN
BISHOP='bishop'
NAMED_PIECES[B_B]=(BISHOP,BLK)
NAMED_PIECES[W_B]=(BISHOP,WHT)

QUEENN=4
B_Q=BLACK+QUEENN
W_Q=WHITE+QUEENN
QUEEN='queen'
NAMED_PIECES[B_Q]=(QUEEN,BLK)
NAMED_PIECES[W_Q]=(QUEEN,WHT)

KINGN=5
B_K=BLACK+KINGN
W_K=WHITE+KINGN
KING='king'
NAMED_PIECES[B_K]=(KING,BLK)
NAMED_PIECES[W_K]=(KING,WHT)

PAWNN=6
B_P=BLACK+PAWNN
W_P=WHITE+PAWNN
PAWN='pawn'
NAMED_PIECES[B_P]=(PAWN,BLK)
NAMED_PIECES[W_P]=(PAWN,WHT)

BT=0 # Standard Board Tile
ROW_KEY=dict()
ROW_KEY[0]='A'
ROW_KEY[1]='B'
ROW_KEY[2]='C'
ROW_KEY[3]='D'
ROW_KEY[4]='E'
ROW_KEY[5]='F'
ROW_KEY[6]='G'
ROW_KEY[7]='H'

# Array Maps:
INITIAL_BOARD=[
    [BT,BT,BT,BT,BT,BT,BT,BT],
    [BT,BT,BT,BT,BT,BT,BT,BT],
    [BT,BT,BT,BT,BT,BT,BT,BT],
    [BT,BT,BT,BT,BT,BT,BT,BT],
    [BT,BT,BT,BT,BT,BT,BT,BT],
    [BT,BT,BT,BT,BT,BT,BT,BT],
    [BT,BT,BT,BT,BT,BT,BT,BT],
    [BT,BT,BT,BT,BT,BT,BT,BT],
]

PIECE_MAP=[
    [B_R,B_KN,B_B,B_Q,B_K,B_B,B_KN,B_R],
    [B_P,B_P,B_P,B_P,B_P,B_P,B_P,B_P],
    [-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1],
    [W_P,W_P,W_P,W_P,W_P,W_P,W_P,W_P],
    [W_R,W_KN,W_B,W_Q,W_K,W_B,W_KN,W_R]
]

# NOTE Sprite array, used to .subsurface() images from a single image represented in the piece sprite sheet.
SS_MAP=[
    [ROOK+WHT,KNIGHT+WHT,BISHOP+WHT,QUEEN+WHT,KING+WHT,PAWN+WHT],
    [ROOK+BLK,KNIGHT+BLK,BISHOP+BLK,QUEEN+BLK,KING+BLK,PAWN+BLK]
]

PIECE_BOARD_KEY=dict()
# Black:
PIECE_BOARD_KEY[B_R]=0
PIECE_BOARD_KEY[B_KN]=0
PIECE_BOARD_KEY[B_B]=0
PIECE_BOARD_KEY[B_Q]=0
PIECE_BOARD_KEY[B_K]=0
PIECE_BOARD_KEY[B_P]=0
# White:
PIECE_BOARD_KEY[W_R]=0
PIECE_BOARD_KEY[W_KN]=0
PIECE_BOARD_KEY[W_B]=0
PIECE_BOARD_KEY[W_Q]=0
PIECE_BOARD_KEY[W_K]=0
PIECE_BOARD_KEY[W_P]=0