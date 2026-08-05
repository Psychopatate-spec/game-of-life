import random
import time

def empty_board(width, height):
    board = [[0 for _ in range(width)] for _ in range(height)]
    return board

def random_board(width, height):
    board = [[random.random() for _ in range(width)] for _ in range(height)]
    for row_index in range(height):
        for col_index in range(width):
            if board[row_index][col_index] >= 0.5:
                board[row_index][col_index] = 1
            else:
                board[row_index][col_index] = 0
    return board

def render_board(board):
    output = ""
    for row_index in range(len(board)):
        output += "|"
        for col_index in range(len(board[row_index])):
            if board[row_index][col_index] == 1:
                output += "#"
            else:
                output += " "
        output += "|\n"
    print(output)

def compute_next_board(current_board):
    height = len(current_board)
    width = len(current_board[0])
    next_board = empty_board(width, height)
    for row_index in range(height):
        for col_index in range(width):
            live_neighbors = 0
            for row_offset in range(-1, 2):
                for col_offset in range(-1, 2):
                    if row_offset == 0 and col_offset == 0:
                        continue
                    neighbor_row = row_index + row_offset
                    neighbor_col = col_index + col_offset
                    if 0 <= neighbor_row < height and 0 <= neighbor_col < width:
                        if current_board[neighbor_row][neighbor_col] == 1:
                            live_neighbors += 1
            if current_board[row_index][col_index] == 1:
                if live_neighbors == 2 or live_neighbors == 3:
                    next_board[row_index][col_index] = 1
                else:
                    next_board[row_index][col_index] = 0
            else:
                if live_neighbors == 3:
                    next_board[row_index][col_index] = 1
    return next_board

current_board = random_board(100, 40)

while True:
    render_board(current_board)
    time.sleep(0.05)
    current_board = compute_next_board(current_board)