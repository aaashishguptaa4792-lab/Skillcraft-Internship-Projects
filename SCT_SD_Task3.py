# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 17:18:03 2026

@author: ASHISH
"""

import tkinter as tk

class SudokuSolver:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.entries = [[None for _ in range(9)] for _ in range(9)]

        # Create 9x9 grid of Entry widgets
        for i in range(9):
            for j in range(9):
                entry = tk.Entry(root, width=3, font=("Arial", 14), justify="center")
                entry.grid(row=i, column=j, padx=2, pady=2)
                self.entries[i][j] = entry

        # Buttons
        solve_button = tk.Button(root, text="Solve", command=self.solve, bg="#add8e6")
        solve_button.grid(row=9, column=0, columnspan=4, pady=10)

        clear_button = tk.Button(root, text="Clear Grid", command=self.clear_grid, bg="#ffcccb")
        clear_button.grid(row=9, column=5, columnspan=4, pady=10)

    def get_grid(self):
        grid = []
        for i in range(9):
            row = []
            for j in range(9):
                val = self.entries[i][j].get()
                row.append(int(val) if val.isdigit() else 0)
            grid.append(row)
        return grid

    def set_grid(self, grid):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
                if grid[i][j] != 0:
                    self.entries[i][j].insert(0, str(grid[i][j]))

    def is_valid(self, grid, row, col, num):
        if num in grid[row]:
            return False
        if num in [grid[i][col] for i in range(9)]:
            return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if grid[i][j] == num:
                    return False
        return True

    def solve_sudoku(self, grid):
        for row in range(9):
            for col in range(9):
                if grid[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid(grid, row, col, num):
                            grid[row][col] = num
                            if self.solve_sudoku(grid):
                                return True
                            grid[row][col] = 0
                    return False
        return True

    def solve(self):
        grid = self.get_grid()
        if self.solve_sudoku(grid):
            self.set_grid(grid)
        else:
            print("No solution exists.")

    def clear_grid(self):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)

# Run the app
root = tk.Tk()
app = SudokuSolver(root)
root.mainloop()
