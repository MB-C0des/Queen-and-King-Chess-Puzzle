import copy

def location2index(loc: str) -> tuple[int, int]:
    '''implement according to specification'''
    x = ord(loc[0]) - 96
    y = int(loc[1:])
    return ((x, y))
    
	
def index2location(x: int, y: int) -> str:
    '''converts  pair of coordinates to corresponding location'''
    loc = chr(x + 96) + str(y)
    return loc


class Piece:
    pos_x : int	
    pos_y : int
    side : bool #True for White and False for Black
    def __init__(self, pos_X : int, pos_Y : int, side_ : bool):
        '''implement according to specification'''


Board = tuple[int, list[Piece]]


def is_piece_at(pos_X : int, pos_Y : int, B: Board) -> bool:
    '''implement according to specification''' 
	
def piece_at(pos_X : int, pos_Y : int, B: Board) -> Piece:
    '''implement according to specification'''

class Queen(Piece):
    def __init__(self, pos_X : int, pos_Y : int, side_ : bool):
        '''implement according to specification'''
	
    def can_reach(self, pos_X : int, pos_Y : int, B: Board) -> bool:
        '''implement according to specification'''
    def can_move_to(self, pos_X : int, pos_Y : int, B: Board) -> bool:
        '''implement according to specification'''
    def move_to(self, pos_X : int, pos_Y : int, B: Board) -> Board:
        '''implement according to specification'''


class King(Piece):
    def __init__(self, pos_X : int, pos_Y : int, side_ : bool):
        '''implement according to specification'''
    def can_reach(self, pos_X : int, pos_Y : int, B: Board) -> bool:
        '''implement according to specification'''
    def can_move_to(self, pos_X : int, pos_Y : int, B: Board) -> bool:
        '''implement according to specification'''
    def move_to(self, pos_X : int, pos_Y : int, B: Board) -> Board:
        '''implement according to specification'''

def is_check(side: bool, B: Board) -> bool:
    '''implement according to specification'''

def is_checkmate(side: bool, B: Board) -> bool:
    '''implement according to specification'''

def is_stalemate(side: bool, B: Board) -> bool:
    '''implement according to specification'''

def read_board(filename: str) -> Board:
    '''implement according to specification'''

def save_board(filename: str, B: Board) -> None:
    '''implement according to specification'''


def find_black_move(B: Board) -> tuple[Piece, int, int]:
    '''implement according to specification'''

def conf2unicode(B: Board) -> str: 
    '''implement according to specification'''


def main() -> None:
    '''implement according to specification''' 

if __name__ == '__main__': #keep this in
   main()
