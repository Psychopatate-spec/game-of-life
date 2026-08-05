import random

def dead_state(width, height):
    board_state = [[0 for _ in range(width)] for _ in range(height)]
    return board_state

def random_state(width, height):
    board_state = [[random.random() for _ in range(width)] for _ in range(height)]
    for i in range(height):
        for j in range(width):
            if board_state[i][j] >= 0.5:
                board_state[i][j] = 1
            else:
                board_state[i][j] = 0
    return board_state

def render(board_state):
    line = ""
    for i in range(len(board_state)):
        line = line + "|"
        for j in range(len(board_state[i])):
            if board_state[i][j] == 1:
                line = line + "#"
            else:
                line = line + " "
        line = line + "|\n"
    print(line)

def next_board_state(initial_board_state):
    height = len(initial_board_state)
    width = len(initial_board_state[0])
    next_board = dead_state(width, height)
    for i in range(height):
        for j in range(width):
            neighbor_cells = 0
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if x == 0 and y == 0:
                        continue
                    neighbor_i = i + x
                    neighbor_j = j + y
                    if 0 <= neighbor_i < height and 0 <= neighbor_j < width:
                        if initial_board_state[neighbor_i][neighbor_j] == 1:
                            neighbor_cells += 1
            if initial_board_state[i][j] == 1:
                if neighbor_cells == 2 or neighbor_cells == 3:
                    next_board[i][j] = 1
                else:
                    next_board[i][j] = 0
            else:
                if neighbor_cells == 3:
                    next_board[i][j] = 1
    return next_board

current_state = random_state(100, 50)
while True:
    render(current_state)
    current_state = next_board_state(current_state)