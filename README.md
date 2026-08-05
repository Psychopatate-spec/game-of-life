# Game of Life

A simple terminal implementation of Conway's Game of Life written in Python.

The program initializes a randomized board and continuously renders each generation in the terminal using `#` for alive cells and spaces for dead cells.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [How it works](#how-it-works)
- [Conway's Game of Life rules](#conways-game-of-life-rules)
- [Project structure](#project-structure)
- [Future improvements](#future-improvements)

## Features

- Terminal-based live simulation
- Random initial board state
- Standard Conway Game of Life rules
- Easy-to-read implementation with a minimal Python script

## Requirements

- Python 3.x
- No external dependencies

## Usage

From the project folder, run the script and provide a file containing a board (a Python literal list of lists of 0/1):

```bash
python app.py path/to/board_file.txt
```

The program reads the file, parses the contents as a Python literal (using `ast.literal_eval`), and uses that as the initial board. The simulation renders each generation until interrupted.

### Example board file

Save a file (for example `glider.txt`) containing a Python list of lists:

```text
[[0, 1, 0],
 [0, 0, 1],
 [1, 1, 1]]
```

Run:

```bash
python app.py glider.txt
```

## How it works

The implementation in `app.py` includes the following functions:

- `empty_board(width, height)`: returns a grid of dead cells (`0`) with the requested dimensions.
- `random_board(width, height)`: returns a randomized grid containing dead (`0`) and alive (`1`) cells.
- `render_board(board)`: prints the board to the terminal, using `#` for alive cells and a space for dead cells.
- `compute_next_board(current_board)`: computes the next generation according to Conway's Game of Life rules.

On startup the script parses a board file (via `argparse` and `ast.literal_eval`) into `current_board`. The main loop then repeatedly:

- renders `current_board` to the terminal
- sleeps briefly (`time.sleep(0.05)`) to control frame rate
- computes the next generation with `compute_next_board`

If you prefer to start from a randomized board, you can create a file using Python that calls `random_board(...)` and writes the result to disk, then pass that file to the script.

## Conway's Game of Life rules

Each cell has up to eight neighbors. The next state of a cell is determined by its current state and the number of alive neighbors:

- Alive cell with fewer than 2 neighbors: dies (underpopulation)
- Alive cell with 2 or 3 neighbors: stays alive
- Alive cell with more than 3 neighbors: dies (overpopulation)
- Dead cell with exactly 3 neighbors: becomes alive (reproduction)

## Project structure

- `app.py` — main simulation script and core logic
- `README.md` — project documentation

## Future improvements

Potential enhancements for this project include:

- configurable board size and speed via command-line arguments
- support for loading predefined patterns
- better terminal clearing and redraw handling
- pause/resume controls
- support for toroidal (wraparound) board edges

---

Built as a small Python terminal project for Conway's Game of Life.
