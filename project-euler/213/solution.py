# Problem 213: Flea Circus
# 30x30 grid, 900 fleas, each jumps to random neighbor each bell ring.
# After 50 bells, expected number of empty squares.

def solve():
    size = 30
    steps = 50
    cells = size * size

    neighbors = [[] for _ in range(cells)]
    for r in range(size):
        for c in range(size):
            idx = r * size + c
            if r > 0: neighbors[idx].append((r-1)*size + c)
            if r < size-1: neighbors[idx].append((r+1)*size + c)
            if c > 0: neighbors[idx].append(r*size + c - 1)
            if c < size-1: neighbors[idx].append(r*size + c + 1)

    # For each starting cell, compute probability distribution after 50 steps
    # empty_prob[i] = product over all starting cells of (1 - prob[start][i])
    empty_prob = [1.0] * cells

    for start in range(cells):
        dist = [0.0] * cells
        dist[start] = 1.0
        for _ in range(steps):
            nxt = [0.0] * cells
            for i in range(cells):
                if dist[i] == 0.0:
                    continue
                share = dist[i] / len(neighbors[i])
                for nb in neighbors[i]:
                    nxt[nb] += share
            dist = nxt
        for i in range(cells):
            empty_prob[i] *= (1.0 - dist[i])

    print(f"{sum(empty_prob):.6f}")

solve()
