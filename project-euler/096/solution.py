# Problem 96: Su Doku
# Solve all 50 Sudoku puzzles and sum the 3-digit numbers from the top-left corners.

import os

def solve_sudoku(grid):
    empty = [(i, j) for i in range(9) for j in range(9) if grid[i][j] == 0]
    
    def is_valid(r, c, num):
        for i in range(9):
            if grid[r][i] == num or grid[i][c] == num:
                return False
        br, bc = 3*(r//3), 3*(c//3)
        for i in range(br, br+3):
            for j in range(bc, bc+3):
                if grid[i][j] == num:
                    return False
        return True
    
    def backtrack(idx):
        if idx == len(empty):
            return True
        r, c = empty[idx]
        for num in range(1, 10):
            if is_valid(r, c, num):
                grid[r][c] = num
                if backtrack(idx + 1):
                    return True
                grid[r][c] = 0
        return False
    
    backtrack(0)
    return grid

def solve():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, '..', 'resources', 'documents', '0096_sudoku.txt')
    with open(file_path) as f:
        lines = [line.strip() for line in f]
    
    total = 0
    for i in range(50):
        start = i * 10 + 1
        grid = [[int(c) for c in lines[start + r]] for r in range(9)]
        solve_sudoku(grid)
        total += grid[0][0] * 100 + grid[0][1] * 10 + grid[0][2]
    print(total)

solve()
