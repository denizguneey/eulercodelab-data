import math

def is_permutation(a, b):
    return sorted(str(a)) == sorted(str(b))

def solve():
    limit = 10000000
    phi = list(range(limit))
    for i in range(2, limit):
        if phi[i] == i:
            for j in range(i, limit, i):
                phi[j] -= phi[j] // i

    best_n = -1
    best_phi = 1
    for n in range(2, limit):
        ph = phi[n]
        if not is_permutation(n, ph):
            continue
        if best_n == -1 or n * best_phi < best_n * ph:
            best_n = n
            best_phi = ph
    return str(best_n)

if __name__ == '__main__':
    print(solve())
