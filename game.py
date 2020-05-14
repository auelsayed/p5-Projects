from pprint import pprint
from random import randint
from copy import deepcopy
from p5 import *


def createBoard(rows, cols):
    """Return a board with dimensions rows by cols initialized with values randomly as 0 or 1."""
    board = [[randint(0, 1) for j in range(cols)] for i in range(rows)]
    return board


def loadBoard(file):
    with open(file) as f:
        data = f.read()
    return [list(map(int, list(line))) for line in data.split()]


def neighbours_sum(board, row, col):
    """Return the sum of surrounding 8 neighbours of provided cell."""
    sum = 0
    for col_offset in [-1, 0, 1]:
        for row_offset in [-1, 0, 1]:
            # If provided cell is on an edge, loop around
            sum += board[(col_offset + col + cols) % cols][
                (row_offset + row + rows) % rows
            ]
    sum -= board[col][row]
    return sum


def updateBoard(board):
    """Return an updated state board using the rules of the game."""
    # Create a copy of the state board that will not modify original state
    next_board = deepcopy(board)

    for col in range(cols):
        for row in range(rows):
            total = neighbours_sum(board, row, col)
            if board[col][row] == 0 and total == 3:
                next_board[col][row] = 1
            elif board[col][row] == 1 and (total < 2 or total > 3):
                next_board[col][row] = 0

    return next_board


# p5 setup function (runs once)
def setup():
    size(cols * box_size, rows * box_size)


# p5 draw function (runs indefinitely)
def draw():
    global curr_board
    background(0)
    for col in range(cols):
        for row in range(rows):
            if curr_board[col][row] == 1:
                no_stroke()
                fill(255)
                rect((col * box_size, row * box_size), box_size - 1, box_size - 1)

    # no_loop()
    next_board = updateBoard(curr_board)
    curr_board = next_board
    # sleep(3)


if __name__ == "__main__":
    global box_size, rows, cols, curr_board
    # Use this size to create cell images
    box_size = 30
    # Create game board with following number of rows and columns
    rows = 30
    cols = 30
    curr_board = createBoard(rows, cols)

    # Load game board from textfile
    # curr_board = loadBoard("./GGG.txt")
    # rows = len(curr_board[0])
    # cols = len(curr_board)

    # Begin p5 drawing process
    run()
