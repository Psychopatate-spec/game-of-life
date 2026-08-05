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

From the project folder, run:

```bash
python app.py
```

The simulation will start immediately and continue until interrupted.

## How it works

The implementation in `app.py` includes the following functions:

- `dead_state(width, height)`: returns a grid of dead cells (`0`) with the requested dimensions.
- `random_state(width, height)`: returns a randomized grid containing dead (`0`) and alive (`1`) cells.
- `render(board_state)`: prints the board to the terminal, using `#` for alive cells and a space for dead cells.
- `next_board_state(initial_board_state)`: computes the next generation according to Conway's Game of Life rules.

The main loop initializes a random board and then repeatedly renders the current state, waits a short time, and advances to the next generation.

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
