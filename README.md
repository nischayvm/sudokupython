# Sudoku Python

## Overview

This repository contains a Python-based Sudoku application utilizing the Tkinter library for its Graphical User Interface (GUI). The application provides a fully functional Sudoku game environment where users can play generated puzzles, validate their inputs, and utilize an automated solver based on the backtracking algorithm.

## Features

-   **Interactive GUI**: A user-friendly 9x9 grid interface allowing for intuitive gameplay and navigation.
-   **Puzzle Generation**: Capability to generate valid, randomized Sudoku puzzles for continuous play.
-   **Solution Verification**: Instant feedback mechanism to verify user entries against the correct solution.
-   **Automated Solver**: Integrated backtracking algorithm to solve any valid puzzle instance instantly.
-   **Input Validation**: Strict input constraints ensuring only valid numerical digits (1-9) can be entered.

## Prerequisites

To execute this application, the following dependencies are required:

-   **Python 3.x**: Ensure a compatible version of Python 3 is installed on your system.
-   **Tkinter**: This standard Python interface to the Tk GUI toolkit is typically included with Python installations.

## Installation

1.  Clone the repository to your local machine:
    ```bash
    git clone https://github.com/nischayvm/sudokupython.git
    ```
2.  Navigate to the project directory:
    ```bash
    cd sudokupython
    ```

## Usage

Execute the main script to launch the application:

```bash
python sudoku.py
```

### Controls

-   **New Game**: Initializes a new game with a freshly generated board.
-   **Check**: Verifies the current numbers entered into the grid. Correct entries are highlighted in green, while incorrect entries are highlighted in red.
-   **Solve**: Automatically fills the board with the correct solution.

## Project Structure

-   `sudoku.py`: The primary source file containing the game logic, UI definition, and the `SudokuGame` class.

## License

This project is open-source and available for use and modification.
