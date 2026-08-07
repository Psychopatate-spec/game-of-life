# Game of Life

A terminal-based Conway's Game of Life simulator written in Python.

This project loads a pattern from an `.rle` file, renders it in the terminal, and evolves it according to Conway's rules frame by frame.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [CLI options](#cli-options)
- [How it works](#how-it-works)
- [Conway's Game of Life rules](#conways-game-of-life-rules)
- [Example](#example)
- [Project structure](#project-structure)
- [Future improvements](#future-improvements)

## Features

- Loads Game of Life patterns from `.rle` files
- Renders the board in the terminal using `#` for live cells and spaces for dead cells
- Supports custom width and height with `-W` and `-H`
- Works with public pattern collections such as LifeWiki
- No external dependencies required

## Requirements

- Python 3.x

## Usage

Run the script from the project folder:

```bash
python app.py -B boards/pattern.rle -W 100 -H 50
```

You can also use the default empty pattern:

```bash
python app.py
```

The script reads the `.rle` file, converts it into a 2D board, optionally pads it to the requested size, and displays the evolving board in the terminal.

## CLI options

- `-B`, `--board`: path to the `.rle` pattern file. Default: `./empty.rle`
- `-W`, `--width`: desired board width. Default: `0`
- `-H`, `--height`: desired board height. Default: `0`

Example with a public LifeWiki pattern:

```bash
python app.py -B /path/to/pattern.rle -W 120 -H 60
```

You can download free `.rle` patterns from the [LifeWiki pattern collection](https://conwaylife.com/wiki/Category:Patterns). LifeWiki hosts a large collection of Game of Life patterns.

## How it works

The implementation in `app.py` includes the following functions:

- `empty_board(width, height)`: creates a rectangular board full of dead cells (`0`)
- `random_board(width, height)`: creates a random board of `0` and `1` values
- `render_board(board)`: prints the board to the terminal
- `compute_next_board(current_board)`: applies Conway's Game of Life rules to compute the next generation
- `resize_board(board, wanted_width, wanted_height)`: pads the board with dead cells when the requested dimensions are larger than the pattern.
- `rle_to_arr(imported_rle)`: parses an `.rle` pattern into a 2D list of rows and columns

The main loop does this repeatedly:

1. load the pattern from the `.rle` file
2. resize it if width or height are specified
3. render the current board
4. wait briefly with `time.sleep(0.05)`
5. compute the next board with `compute_next_board`

## Conway's Game of Life rules

Each cell has up to 8 neighbors. The next state of a cell depends on the number of living neighbors:

- A live cell with fewer than 2 neighbors dies from underpopulation
- A live cell with 2 or 3 neighbors stays alive
- A live cell with more than 3 neighbors dies from overpopulation
- A dead cell with exactly 3 neighbors becomes alive

## Example

This is a common pattern called a glider:

```text
|          #             |
|            #           |
|          ###           |
```

It moves across the board over time as the simulation advances.

## Project structure

- `app.py` — main simulation logic and CLI parser
- `empty.rle` — default empty board pattern
- `README.md` — project documentation

## Future improvements

Possible enhancements include:

- better terminal clearing and redraw behavior
- pause/resume controls
- configurable simulation speed
- support for toroidal wraparound edges
- more robust RLE parsing for advanced pattern files
- a pattern browser from the command line

---

Built as a small Python terminal project inspired by Conway's Game of Life.
