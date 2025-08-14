import pytest
from chess_puzzle import *


def test_location2index1():
    assert location2index("e2") == (5,2)

# Check for a piece at the bottom left corner
def test_location2index2():
    assert location2index("a1") == (1, 1)

# Check for a piece at the top right corner of a 26x26 board
def test_location2index3():
    assert location2index("z26") == (26, 26)

# Check for a piece at the bottom right corner
def test_location2index4():
    assert location2index("z1") == (26, 1)

# Check for a piece at the top left corner
def test_location2index5():
    assert location2index("a26") == (1, 26)


def test_index2location1():
    assert index2location(5,2) == "e2"

# Check for a piece at the bottom left corner
def test_index2location2():
    assert index2location(1, 1) == "a1"

# Check for a piece at the top right corner of a 26x26 board
def test_index2location3():
    assert index2location(26, 26) == "z26"

# Check for a piece at the bottom right corner
def test_index2location4():
    assert index2location(26, 1) == "z1"

# Check for a piece at the top left corner of a 26x26 board
def test_index2location5():
    assert index2location(1, 26) == "a26"


wq1 = Queen(4,4,True)
wk1 = King(3,5,True)
wq2 = Queen(3,1,True)

bq1 = Queen(5,3,False)
bk1 = King(2,3,False)


B1 = (5, [wq1, wk1, wq2, bq1, bk1])

"""
  ♔  
   ♕ 
 ♚  ♛
     
  ♕  
"""

def test_is_piece_at1():
    assert is_piece_at(2,2, B1) == False

# Check for a piece being on a board
def test_is_piece_at2():
    assert is_piece_at(4, 4, B1) == True


# Check there isn't a piece on a location outside the board
def test_is_piece_at3():
    assert is_piece_at(6, 6, B1) == False


# Check there isn't a piece on a negative location
def test_is_piece_at4():
    assert is_piece_at(-2, -3, B1) == False

def test_piece_at1():
    assert piece_at(3,1, B1) == wq2

# Check for the white King
def test_piece_at2():
    assert piece_at(3, 5, B1) == wk1

# Check for the black Queen
def test_piece_at3():
    assert piece_at(5, 3, B1) == bq1

# Check for the black King
def test_piece_at4():
    assert piece_at(2, 3, B1) == bk1

# Check for the absence of a piece
def test_piece_at5():
    assert piece_at(1, 1, B1) == None

# Check outside the board
def test_piece_at6():
    assert piece_at(6, 6, B1) == None

def test_can_reach1():
    assert wq1.can_reach(5,4, B1) == True

# Check that the white Queen can reach the black Queen
def test_can_reach2():
    assert wq1.can_reach(5, 3, B1) == True


# Check that the black Queen can reach the white Queen
def test_can_reach3():
    assert bq1.can_reach(4, 4, B1) == True


# Check that the black Queen cannot reach the white King (blocked by white King)
def test_can_reach4():
    assert bq1.can_reach(3, 5, B1) == False

# Check that the black King can reach in all steps adjacent to it
def test_can_reach5():
    possible_moves = [(1, 1), (1, 0), (-1, 0), (-1, -1), (0, -1), (0, 1),
                      (-1, 1), (1, -1)]
    for move in possible_moves:
        x = move[0] + bk1.pos_x
        y = move[1] + bk1.pos_y
        assert bk1.can_reach(x, y, B1) == True


# Check that a King cannot move more than one space
def test_can_reach6():
    impossible_moves = [(2, 0), (0, 2), (5, 5), (-3, -3), (2, -2), (-2, 2)]
    for move in impossible_moves:
        x = move[0] + bk1.pos_x
        y = move[1] + bk1.pos_y
        assert bk1.can_reach(x, y, B1) == False

def test_can_move_to1():
    assert wq1.can_move_to(5,4, B1) == False

# Check that the black King cannot move right which would place it in check
def test_can_move_to2():
    assert wk1.can_move_to(3, 3, B1) == False


# Check that the black King can move down-left
def test_can_move_to3():
    assert bk1.can_move_to(1, 2, B1) == True

def test_move_to1():
    wk1a = King(4,5, True)

    Actual_B = wk1.move_to(4,5, B1)
    Expected_B = (5, [wq1, wk1a, wq2, bq1, bk1])
    #check if actual board has same contents as expected 
    assert Actual_B[0] == 5

    for piece1 in Actual_B[1]: #we check if every piece in Actual_B is also present in Expected_B; if not, the test will fail
        found = False
        for piece in Expected_B[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found


    for piece in Expected_B[1]:  #we check if every piece in Expected_B is also present in Actual_B; if not, the test will fail
        found = False
        for piece1 in Actual_B[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found


def test_is_check1():
    B2 = (5, [wk1, wq2, bq1, bk1])
    assert is_check(True, B2) == True

# Check that the King isn't in check when a piece on their side is blocking the checking path
def test_is_check2():
    assert is_check(True, B1) == False

wq3 = Queen(4, 2, True)
stalemate_board = (5, [bk1, wq1, wq2, wq3])

def test_is_checkmate1():
    B2 = (5, [wk1, wq2, bq1, bk1])
    assert is_checkmate(True, B2) == False

# Check that a stalemate does NOT result in a checkmate
def test_is_checkmate2():
    assert is_checkmate(False, stalemate_board) == False

# Check that an empty board is not a checkmate
def test_is_checkmate3():
    board = (5, [])
    assert is_checkmate(False, board) == False

# Check for a standard stalemate
def test_is_stalemate1():
    assert is_stalemate(False, stalemate_board) == True

# Check that a board with a checkmate does NOT return a stalemate as true
def test_is_stalemate2():
    B2 = (5, [wk1, wq2, bq1, bk1])
    assert is_stalemate(False, B2) == False

# Check that an empty board is not a stalemate
def test_is_stalemate3():
    board = (5, [])
    assert is_stalemate(False, board) == False

def test_read_board1():
    B = read_board("board_examp.txt")
    assert B[0] == 5

    for piece in B[1]:  #we check if every piece in B is also present in B1; if not, the test will fail
        found = False
        for piece1 in B1[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found

    for piece1 in B1[1]: #we check if every piece in B1 is also present in B; if not, the test will fail
        found = False
        for piece in B[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(piece) == type(piece1):
                found = True
        assert found

# Check that a text file board with spaces between the pieces reads correctly
def test_read_board2():
    B = read_board("board_examp_spaces.txt")
    assert B[0] == 5

    for piece in B[
            1]:  #we check if every piece in B is also present in B1; if not, the test will fail
        found = False
        for piece1 in B1[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(
                    piece) == type(piece1):
                found = True
        assert found

    for piece1 in B1[
            1]:  #we check if every piece in B1 is also present in B; if not, the test will fail
        found = False
        for piece in B[1]:
            if piece.pos_x == piece1.pos_x and piece.pos_y == piece1.pos_y and piece.side == piece1.side and type(
                    piece) == type(piece1):
                found = True
        assert found

def test_conf2unicode1():
    assert conf2unicode(B1).rstrip("\n") == "  ♔  \n   ♕ \n ♚  ♛\n     \n  ♕  "

# Check for an empty board
def test_conf2unicode2():
    empty_board = (5, [])
    assert conf2unicode(empty_board).rstrip(
        "\n") == "     \n     \n     \n     \n     "


# Check for boards full of pieces
def test_conf2unicode3():
    pieces = []

    for x in range(1, 6):
        for y in range(1, 6):
            piece = Queen(x, y, True)
            pieces.append(piece)

    board = (5, pieces)
    assert conf2unicode(board).rstrip(
        "\n") == "♕♕♕♕♕\n♕♕♕♕♕\n♕♕♕♕♕\n♕♕♕♕♕\n♕♕♕♕♕"