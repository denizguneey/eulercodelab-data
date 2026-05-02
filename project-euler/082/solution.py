# Problem 82: Path sum: three ways
# Find the minimal sum from left column to right column (move up, down, right).

import os

def solve():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, '..', 'resources', 'documents', '0082_matrix.txt')
    with open(file_path) as f:
        matrix = [list(map(int, line.strip().split(','))) for line in f if line.strip()]
    n = len(matrix)
    # dp[i] = min path sum to reach column j, row i
    dp = [matrix[i][0] for i in range(n)]
    for j in range(1, n):
        # Start with going right
        new_dp = [dp[i] + matrix[i][j] for i in range(n)]
        # Top to bottom
        for i in range(1, n):
            new_dp[i] = min(new_dp[i], new_dp[i-1] + matrix[i][j])
        # Bottom to top
        for i in range(n-2, -1, -1):
            new_dp[i] = min(new_dp[i], new_dp[i+1] + matrix[i][j])
        dp = new_dp
    print(min(dp))

solve()
