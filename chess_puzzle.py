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
        self.pos_x = pos_X
        self.pos_y = pos_Y
        self.side = side_

    def __str__(self):
        side = "White" if self.side else "Black"
        return f"{side} {type(self).__name__} at {(self.pos_x, self.pos_y)}/{index2location(self.pos_x, self.pos_y)}"

    def __repr__(self):
        side = "w" if self.side else "b"
        return f"{type(self).__name__[0]}{index2location(self.pos_x, self.pos_y)}{side}"

Board = tuple[int, list[Piece]]


def is_piece_at(pos_X : int, pos_Y : int, B: Board) -> bool:
    '''implement according to specification''' 
    for piece in B[1]:
        if piece.pos_x == pos_X and piece.pos_y == pos_Y:
            return True
    return False # Piece is not in that position so return False
	
def piece_at(pos_X : int, pos_Y : int, B: Board) -> Piece:
    '''implement according to specification'''
    for piece in B[1]:
        if piece.pos_x == pos_X and piece.pos_y == pos_Y:
            return piece 
    return None # Piece is not in that position so return None

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
