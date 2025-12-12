import tkinter as tk
from tkinter import messagebox
import random

class SudokuGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku")
        self.root.geometry("380x450")
        
        # 2D list to hold the underlying data (0 means empty)
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.solution = [[0 for _ in range(9)] for _ in range(9)]
        
        # 2D list to hold the GUI Entry widgets
        self.cells = [[None for _ in range(9)] for _ in range(9)]
        
        self.create_grid()
        self.create_buttons()
        self.new_game()

    def create_grid(self):
        # Create a frame for the grid to handle 3x3 block visual separation
        grid_frame = tk.Frame(self.root, bg="black", bd=2)
        grid_frame.pack(pady=10)

        for row in range(9):
            for col in range(9):
                # Add extra padding to separate 3x3 blocks visually
                pady_top = 1 if row % 3 == 0 and row != 0 else 0
                padx_left = 1 if col % 3 == 0 and col != 0 else 0
                
                cell_frame = tk.Frame(grid_frame, bg="white", bd=0)
                cell_frame.grid(row=row, column=col, padx=(padx_left, 1), pady=(pady_top, 1))

                # Create the input cell
                cell = tk.Entry(cell_frame, width=2, font=("Arial", 18), justify="center", bd=0)
                cell.pack(padx=1, pady=1)
                
                # Validate input to ensure only numbers 1-9
                reg = self.root.register(self.validate_input)
                cell.config(validate="key", validatecommand=(reg, "%P"))
                
                self.cells[row][col] = cell

    def create_buttons(self):
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        check_btn = tk.Button(btn_frame, text="Check", command=self.check_solution, width=10, bg="#dddddd")
        check_btn.grid(row=0, column=0, padx=5)

        solve_btn = tk.Button(btn_frame, text="Solve", command=self.solve_game, width=10, bg="#dddddd")
        solve_btn.grid(row=0, column=1, padx=5)

        new_btn = tk.Button(btn_frame, text="New Game", command=self.new_game, width=10, bg="#dddddd")
        new_btn.grid(row=0, column=2, padx=5)

    def validate_input(self, val):
        # Allow empty or single digits 1-9
        if val == "" or (val.isdigit() and 1 <= int(val) <= 9 and len(val) == 1):
            return True
        return False

    def new_game(self):
        self.clear_board()
        self.generate_board()
        self.display_board()

    def clear_board(self):
        for row in range(9):
            for col in range(9):
                self.cells[row][col].delete(0, tk.END)
                self.cells[row][col].config(bg="white", fg="black", state="normal")

    def generate_board(self):
        # Generate a full valid board first
        self.board = [[0]*9 for _ in range(9)]
        self.fill_diagonal_boxes()
        self.solve_sudoku(self.board)  # Fill the rest
        
        # Save the solution
        self.solution = [row[:] for row in self.board]

        # Remove numbers to create the puzzle (adjust 40 for difficulty)
        attempts = 40 
        while attempts > 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                attempts -= 1

    def fill_diagonal_boxes(self):
        # Fill the three diagonal 3x3 boxes (independent of each other)
        for i in range(0, 9, 3):
            self.fill_box(i, i)

    def fill_box(self, row, col):
        num = 0
        for i in range(3):
            for j in range(3):
                while True:
                    num = random.randint(1, 9)
                    if self.is_safe_in_box(row, col, num):
                        break
                self.board[row + i][col + j] = num

    def is_safe_in_box(self, row_start, col_start, num):
        for i in range(3):
            for j in range(3):
                if self.board[row_start + i][col_start + j] == num:
                    return False
        return True

    def is_safe(self, grid, row, col, num):
        # Check row
        for x in range(9):
            if grid[row][x] == num:
                return False
        # Check column
        for x in range(9):
            if grid[x][col] == num:
                return False
        # Check 3x3 box
        start_row, start_col = row - row % 3, col - col % 3
        for i in range(3):
            for j in range(3):
                if grid[start_row + i][start_col + j] == num:
                    return False
        return True

    def solve_sudoku(self, grid):
        row, col = self.find_empty(grid)
        if row == -1:
            return True  # Board is full

        for num in range(1, 10):
            if self.is_safe(grid, row, col, num):
                grid[row][col] = num
                if self.solve_sudoku(grid):
                    return True
                grid[row][col] = 0  # Backtrack

        return False

    def find_empty(self, grid):
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    return i, j
        return -1, -1

    def display_board(self):
        for row in range(9):
            for col in range(9):
                val = self.board[row][col]
                if val != 0:
                    self.cells[row][col].insert(0, str(val))
                    self.cells[row][col].config(state="disabled", disabledforeground="blue")

    def check_solution(self):
        for row in range(9):
            for col in range(9):
                user_val = self.cells[row][col].get()
                if user_val:
                    if int(user_val) == self.solution[row][col]:
                        self.cells[row][col].config(bg="#ccffcc")  # Green for correct
                    else:
                        self.cells[row][col].config(bg="#ffcccc")  # Red for wrong
                else:
                     self.cells[row][col].config(bg="white")

    def solve_game(self):
        # Fill the GUI with the solution
        for row in range(9):
            for col in range(9):
                self.cells[row][col].config(state="normal")
                self.cells[row][col].delete(0, tk.END)
                self.cells[row][col].insert(0, str(self.solution[row][col]))
                self.cells[row][col].config(state="disabled", disabledforeground="black")


if __name__ == "__main__":
    root = tk.Tk()
    game = SudokuGame(root)
    root.mainloop()