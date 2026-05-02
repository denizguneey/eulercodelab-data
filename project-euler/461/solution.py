import math

def solve():
    N = 10000
    pi = math.pi
    bound = int(math.floor(N * math.log(pi + 0.1)))
    values = [math.exp(a / N) - 1.0 for a in range(bound + 1)]

    delta = 0.001
    small_sums = []
    for a in range(bound + 1):
        ea = values[a]
        if 4.0 * ea > pi + delta: break
        for b in range(a, bound + 1):
            eb = values[b]
            if ea + 3.0 * eb > pi + delta: break
            small_sums.append(ea + eb)

    large_sums = []
    for d in range(bound, -1, -1):
        ed = values[d]
        if ed > pi + delta: continue
        if 4.0 * ed < pi - delta: break
        for c in range(d, -1, -1):
            ec = values[c]
            if ec + ed > pi + delta: continue
            if ed + 3.0 * ec < pi - delta: break
            large_sums.append(ec + ed)

    small_sums.sort()
    large_sums.sort()

    def closest_sum_two(x, y, target, delta_start=0.0001):
        best_i = best_j = -1
        best_delta = delta_start
        j = len(y) - 1
        for i in range(len(x)):
            if j < 0: break
            if x[i] + y[j] < target - best_delta: continue
            while j >= 0 and x[i] + y[j] > target and x[i] <= y[j]:
                j -= 1
            if j < 0 or x[i] > y[j]: break
            cand_j = j
            d = target - x[i] - y[j]
            if j < len(y) - 1 and x[i] + y[j+1] > target and x[i] + y[j+1] - target < d:
                cand_j = j + 1
                d = x[i] + y[cand_j] - target
            if d < best_delta:
                best_delta = d
                best_i = i
                best_j = cand_j
        return best_i, best_j

    i, j = closest_sum_two(small_sums, large_sums, pi)
    ai, bi = closest_sum_two(values, values, small_sums[i], 0.001)
    ci, di = closest_sum_two(values, values, large_sums[j], 0.001)
    idx = sorted([ai, bi, ci, di])
    return str(sum(x*x for x in idx))

if __name__ == '__main__':
    print(solve())
