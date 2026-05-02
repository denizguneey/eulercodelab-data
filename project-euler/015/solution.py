from math import comb

def solve(grid_size=20):
    return comb(2 * grid_size, grid_size)

if __name__ == "__main__":
    assert solve(2) == 6, "Checkpoint failed for grid_size=2"
    assert solve(1) == 2, "Checkpoint failed for grid_size=1"
    print(solve())
