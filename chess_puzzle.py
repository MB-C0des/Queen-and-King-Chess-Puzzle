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
        super().__init__(pos_X, pos_Y, side_)
	
    def can_reach(self, pos_X : int, pos_Y : int, B: Board) -> bool:
        '''implement according to specification'''
        x = self.pos_x
        y = self.pos_y

        dx = pos_X - x
        dy = pos_Y - y
        
        # Check if NOT vertical, horizontal or diagonal
        if not (x == pos_X or y == pos_Y or abs(dx) == abs(dy)):
            return False

        pointsInBetween = []
        
        # All the points between the path of the Queen and the target
        step_x = 0 if dx == 0 else dx // abs(dx)
        step_y = 0 if dy == 0 else dy // abs(dy)

        new_point = (x + step_x, y + step_y)
        target = (pos_X, pos_Y)

        while (new_point != target):
            pointsInBetween.append(new_point)
            new_point = (new_point[0] + step_x, new_point[1] + step_y)

        for place in pointsInBetween:
            if is_piece_at(place[0], place[1], B):
                return False

        # Return False if the target position contains a piece of the same type
        if is_piece_at(pos_X, pos_Y, B):
            if piece_at(pos_X, pos_Y, B).side == self.side:
                return False
            
        return True

    def can_move_to(self, pos_X : int, pos_Y : int, B: Board) -> bool:
        '''implement according to specification'''
        # Check if can move to the position
        if not self.can_reach(pos_X, pos_Y, B):
            return False

        # Make the move on a new board
        new_board = copy.deepcopy(B)
        
        # Check if side would be in check move is made
        piece = piece_at(self.pos_x, self.pos_y, new_board)
        piece.pos_x = pos_X
        piece.pos_y = pos_Y

        # Remove a piece in that place if it would have been captured
        captured_piece = piece_at(pos_X, pos_Y, new_board)
        if captured_piece != None:
            new_board[1].remove(captured_piece)

        # Return True/False if so or not
        if is_check(self.side, new_board):
            return False
        
        return True

    def move_to(self, pos_X : int, pos_Y : int, B: Board) -> Board:
        '''implement according to specification'''
        # Return a new board without affecting the original board by making a deepcopy 
        new_B = copy.deepcopy(B)
        new_piece = piece_at(self.pos_x, self.pos_y, new_B)

        # Check if the move is valid
        if new_piece.can_move_to(pos_X, pos_Y, new_B):
            # Remove a piece in that place if it would have been captured
            captured_piece = piece_at(pos_X, pos_Y, new_B)
            if captured_piece != None:
                new_B[1].remove(captured_piece)

            # Move this piece to the new position
            new_piece.pos_x = pos_X
            new_piece.pos_y = pos_Y
            pass

        return new_B

class King(Piece):
    def __init__(self, pos_X : int, pos_Y : int, side_ : bool):
        '''implement according to specification'''
        super().__init__(pos_X, pos_Y, side_)

    def can_reach(self, pos_X : int, pos_Y : int, B: Board) -> bool:
        '''implement according to specification'''
        possible_moves = [(1, 1), (1, 0), (-1, 0), (-1, -1), (0, -1), (0, 1),
                          (-1, 1), (1, -1)]

        dx = pos_X - self.pos_x
        dy = pos_Y - self.pos_y

        # Return False if the target move is not one of the possible moves
        if (dx, dy) not in possible_moves:
            return False

        # Return False if the target position contains a piece of the same type
        if is_piece_at(pos_X, pos_Y, B):
            if piece_at(pos_X, pos_Y, B).side == self.side:
                return False

        return True
    
    def can_move_to(self, pos_X : int, pos_Y : int, B: Board) -> bool:
        '''implement according to specification'''
        # Check if can move to the position
        if not self.can_reach(pos_X, pos_Y, B):
            return False
        
        # Move piece to the position and check if it results in a checkmate
        new_board = copy.deepcopy(B)
        new_piece = piece_at(self.pos_x, self.pos_y, new_board)
        new_piece.pos_x = pos_X
        new_piece.pos_y = pos_Y

        if is_check(self.side, new_board):
            return False

        return True

    def move_to(self, pos_X : int, pos_Y : int, B: Board) -> Board:
        '''implement according to specification'''
        new_B = copy.deepcopy(B)

        new_piece = piece_at(self.pos_x, self.pos_y, new_B)

        # Check if the move is valid
        if new_piece.can_move_to(pos_X, pos_Y, new_B):
            # Remove a piece in that place if it would have been captured
            captured_piece = piece_at(pos_X, pos_Y, new_B)
            if captured_piece != None:
                new_B[1].remove(captured_piece)

            # Move this piece to the new position
            new_piece.pos_x = pos_X
            new_piece.pos_y = pos_Y
            pass

        return new_B
    
    def is_unable_to_move(self, B: Board) -> bool:
        x = self.pos_x
        y = self.pos_y

        possible_moves = [(1, 1), (1, 0), (-1, 0), (-1, -1), (0, -1), (0, 1),
                          (-1, 1), (1, -1)]

        # Check that the King is unable to make moves in any direction
        can_move = False
        for move in possible_moves:
            new_x = move[1] + x
            new_y = move[1] + y
            if self.can_move_to(new_x, new_y, B):
                can_move = True
                break

        return not can_move

def is_check(side: bool, B: Board) -> bool:
    '''implement according to specification'''
    for piece in B[1]:
        # If the piece is a King on side
        if type(piece).__name__ == "King" and piece.side == side:
            x = piece.pos_x
            y = piece.pos_y
            # Iterate through all the Queens on the other side
            for queen in B[1]:
                if type(queen).__name__ == "Queen" and queen.side != side:
                    # If the other sides Queen can reach the King, return True
                    if queen.can_reach(x, y, B):
                        return True

    return False

def is_checkmate(side: bool, B: Board) -> bool:
    '''implement according to specification'''
    pieces = B[1]

    if not is_check(side, B):
        # Cannot be checkmate if not in check
        return False

    # Find the King on this side
    king = None

    for piece in pieces:
        piece_type = type(piece).__name__
        if piece_type == "King" and piece.side == side:
            king = piece
            break

    # Check if the King is unable to move, if so return True
    return king.is_unable_to_move(B)

def is_stalemate(side: bool, B: Board) -> bool:
    '''implement according to specification'''
    pieces = B[1]
    # Check that the King is NOT in check
    if is_check(side, B):
        # Cannot be a stalemate if the King is in check
        return False

    # Find the King on this side
    king = None

    for piece in pieces:
        piece_type = type(piece).__name__
        if piece_type == "King" and piece.side == side:
            king = piece
            break

    # Check if the King is unable to move, if so return True
    if king:
        return king.is_unable_to_move(B)
    else:
        return False

def read_board(filename: str) -> Board:
    '''implement according to specification'''
    try:
        file = open(filename, "r")
        board_width = int(file.readline())
        white_pieces = file.readline()
        black_pieces = file.readline()
        pieces = []

        for piece in black_pieces.split(", "):
            piece = piece.strip()
            type = piece[0]
            pos = location2index(piece[1:])
            if type == "K":
                pieces.append(King(pos[0], pos[1], False))
            elif type == "Q":
                pieces.append(Queen(pos[0], pos[1], False))
    
        board = Board((board_width, pieces))
        return board
    except:

        raise IOError

def save_board(filename: str, B: Board) -> None:
    '''implement according to specification'''
    lines = []

    # Add the first line which is the total number of pieces on the board
    lines.append(str(B[0]) + "\n")

    white_pieces = [repr(piece) for piece in B[1] if piece.side == True]
    black_pieces = [repr(piece) for piece in B[1] if piece.side == False]

    # Add the second line which contains the white pieces as their text representations
    lines.append(", ".join(white_pieces) + "\n")
    lines.append(", ".join(black_pieces))

    with open(filename, "w") as f:
        f.writelines(lines)

def find_black_move(B: Board) -> tuple[Piece, int, int]:
    '''implement according to specification'''

def conf2unicode(B: Board) -> str: 
    '''implement according to specification'''
    board = [["\u2001" for x in range(B[0])] for y in range(B[0])]

    for piece in B[1]:
        y = B[0] - piece.pos_y
        x = piece.pos_x - 1
        if type(piece).__name__ == "King":
            if piece.side == True:
                # White King
                board[y][x] = "\u2654"
            else:
                # Black King
                board[y][x] = "\u265A"
        else:
            if piece.side == True:
                # White Queen
                board[y][x] = "\u2655"
            else:
                # Black Queen
                board[y][x] = "\u265B"

    board = ["".join(row) for row in board]
    final_board = "\n".join(board)
    return final_board

def main() -> None:
    '''implement according to specification''' 
    board = None
    filename = input("File name for initial configuration: ")
    while board is None:
        if filename == "QUIT":
            exit()  
        try:
            board = read_board(filename)
        except IOError:
            filename = input("This is not a valid file. File name for initial configuration: ")

    # Once a valid board has been loaded, print the configuration as unicode
    board_text = conf2unicode(board)
    print("The initial configuration is: ")
    print(board_text)

if __name__ == '__main__': #keep this in
   main()
