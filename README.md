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
- `.rle` board import support
- Adjustable board size using CLI flags
- Standard Conway Game of Life rules
- Minimal Python implementation with no external dependencies

## Requirements

- Python 3.x
- No external dependencies

## Usage

Run the script with a board file and optional size flags:

```bash
python app.py -B boards/pattern.rle -W 100 -H 50
```

If no `-B` / `--board` flag is provided, the script defaults to `./boards/empty.rle`.

The script reads the selected `.rle` board file, converts the pattern into a 2D board array, -W and -H optionally add dead-cell padding to reach the requested dimensions.

### CLI options

- `-B`, `--board`: path to an `.rle` board file (default: `./boards/empty.rle`)
- `-W`, `--width`: desired board width (default: `0` — no extra width padding)
- `-H`, `--height`: desired board height (default: `0` — no extra height padding)

## How it works

The implementation in `app.py` includes the following functions:

- `empty_board(width, height)`: returns a grid of dead cells (`0`) with the requested dimensions.
- `random_board(width, height)`: returns a randomized grid containing dead (`0`) and alive (`1`) cells.
- `render_board(board)`: prints the board to the terminal, using `#` for alive cells and a space for dead cells.
- `compute_next_board(current_board)`: computes the next generation according to Conway's Game of Life rules.
- `rle_to_arr(imported_rel)`: parses a Conway `.rle` pattern string into a 2D board array.
- `resize_board(board, wanted_width, wanted_height)`: pads the board with dead cells to reach the requested width and height.

On startup the script parses CLI arguments, loads the chosen `.rle` board file, converts it into `current_board`, resizes it if needed, and then enters the simulation loop.

The main loop then repeatedly:

- renders `current_board` to the terminal
- sleeps briefly (`time.sleep(0.05)`) to control frame rate
- computes the next generation with `compute_next_board`

If you want to use a custom `.rle` pattern, add it to the `boards/` folder and pass it via `-B`.

Many `.rle` patterns are available online. The [LifeWiki pattern collection](https://conwaylife.com/wiki/Category:Patterns) contains thousands of Conway's Game of Life patterns.

Download an `.rle` file and pass it to the program with:

```bash
python app.py -B path/to/pattern.rle
## Conway's Game of Life rules
```

Each cell has up to eight neighbors. The next state of a cell is determined by its current state and the number of alive neighbors:

- Alive cell with fewer than 2 neighbors: dies (underpopulation)
- Alive cell with 2 or 3 neighbors: stays alive
- Alive cell with more than 3 neighbors: dies (overpopulation)
- Dead cell with exactly 3 neighbors: becomes alive (reproduction)

## Example

```text
|          #             |
|            #           |
|          ###           |
```

## Project structure

- `app.py` — main simulation script and core logic
- `README.md` — project documentation

## Future improvements

Potential enhancements for this project include:

- better terminal clearing and redraw handling
- pause/resume controls
- configurable simulation speed
- support for toroidal (wraparound) board edges
- support for additional Life rules
- pattern browser / pattern selection from the CLI
- improved RLE parsing

---

Built as a small Python terminal project for Conway's Game of Life.
