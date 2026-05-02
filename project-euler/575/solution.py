def solve():
    N = 1000
    NN = N * N
    corners = 4
    edges = 4 * (N - 2)
    interior = (N - 2) * (N - 2)
    total_deg = 2 * corners + 3 * edges + 4 * interior
    total_deg_plus1 = total_deg + NN

    sum_deg_sq = 0
    sum_deg_plus1_sq = 0
    for k in range(1, N + 1):
        x = k * k
        r = (x - 1) // N + 1
        c = (x - 1) % N + 1
        top = r == 1; bottom = r == N; left = c == 1; right = c == N
        is_corner = (top or bottom) and (left or right)
        is_edge = top or bottom or left or right
        d = 2 if is_corner else (3 if is_edge else 4)
        sum_deg_sq += d
        sum_deg_plus1_sq += d + 1

    p_i = sum_deg_plus1_sq / total_deg_plus1
    p_ii = sum_deg_sq / total_deg
    return f'{0.5 * (p_i + p_ii):.12f}'

if __name__ == '__main__':
    print(solve())
