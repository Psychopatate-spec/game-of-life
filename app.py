import random
import argparse
import time
import ast

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

def resize_board(board, wanted_width, wanted_height):
    wanted_board = board
    board_height = len(board)
    board_width = len(board[0])
    if wanted_height > board_height:
        height_offset = wanted_height - board_height
        for i in range(height_offset):
            wanted_board.append([0 for _ in range(board_width)])
    if wanted_width > board_width:
        width_offset = wanted_width - board_width

        for j in range(wanted_height):
            for i in range(width_offset):
                wanted_board[j].append(0)
    return wanted_board

def rel_to_arr(imported_rel):
    arr = [[]]
    row = 0
    numbers = ""
    lines = imported_rel.splitlines()
    for line in lines:
        if line.startswith("#") or line.startswith("x"):
            continue
        for i in range(len(line)):
            if line[i].isdigit():
                numbers = numbers + line[i]
            if line[i] == "o":
                if numbers == "":
                    arr[row].append(1)
                else:
                    arr[row].extend(1 for _ in range(int(numbers)))
                    numbers = ""
            if line[i] == "b":
                if numbers == "":
                    arr[row].append(0)
                else:
                    arr[row].extend(0 for _ in range(int(numbers)))
                    numbers = ""
            if line[i] == "$":
                row += 1
                arr.append([])
            if line[i] == "!":
                return arr

parser = argparse.ArgumentParser()
parser.add_argument("-B", "--board", type = argparse.FileType('r'), default = "./boards/empty.rle")
parser.add_argument("-W", "--width", type = int, default = 0)
parser.add_argument("-H", "--height", type = int, default = 0)
args = parser.parse_args()

imported_board = args.board.read()
args.board.close()
width = args.width
height = args.height

current_board = resize_board(rel_to_arr(imported_board), width, height)
print(current_board)

while True:
    render_board(current_board)
    time.sleep(0.05)
    current_board = compute_next_board(current_board)