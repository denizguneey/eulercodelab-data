# Problem 81: Path sum: two ways
# Find the minimal path sum from top-left to bottom-right moving only right and down.

import os

def solve():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, '..', 'resources', 'documents', '0081_matrix.txt')
    with open(file_path) as f:
        matrix = [list(map(int, line.strip().split(','))) for line in f if line.strip()]
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0: continue
            elif i == 0: matrix[i][j] += matrix[i][j-1]
            elif j == 0: matrix[i][j] += matrix[i-1][j]
            else: matrix[i][j] += min(matrix[i-1][j], matrix[i][j-1])
    print(matrix[-1][-1])

solve()
