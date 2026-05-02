import bisect
import math

class LowState:
    def __init__(self, b, a, last):
        self.b = b
        self.a = a
        self.last = last

class HighState:
    def __init__(self, b, a, first):
        self.b = b
        self.a = a
        self.first = first

class Bucket:
    def __init__(self):
        self.values = []
        self.pref = []

def build_fib():
    f = [0] * 100
    f[0] = 0
    f[1] = 1
    for i in range(2, 100):
        f[i] = f[i - 1] + f[i - 2]
    return f

def build_pair_coefficients(fib, max_index):
    coeff_a = [0] * (max_index + 1)
    coeff_b = [0] * (max_index + 1)

    for i in range(max_index + 1):
        if i == 0:
            pos_a = 1
            pos_b = 0
        else:
            pos_a = fib[i - 1]
            pos_b = fib[i]

        m = i + 1
        sign = 1 if m % 2 == 0 else -1
        neg_a = sign * fib[m + 1]
        neg_b = -sign * fib[m]

        coeff_a[i] = pos_a + neg_a
        coeff_b[i] = pos_b + neg_b

    return coeff_a, coeff_b

def min_max_possible_a_for_length(n, coeff_a):
    kInf = 1 << 62
    min_dp = [[kInf, kInf] for _ in range(n + 1)]
    max_dp = [[-kInf, -kInf] for _ in range(n + 1)]
    min_dp[n] = [0, 0]
    max_dp[n] = [0, 0]

    for idx in range(n - 1, -1, -1):
        for prev in range(2):
            best_min = kInf
            best_max = -kInf

            def relax(bit):
                nonlocal best_min, best_max
                if prev == 1 and bit == 1:
                    return
                add = coeff_a[idx] if bit == 1 else 0
                child_min = min_dp[idx + 1][bit]
                child_max = max_dp[idx + 1][bit]
                if child_min >= kInf // 2 or child_max <= -kInf // 2:
                    return
                if add + child_min < best_min:
                    best_min = add + child_min
                if add + child_max > best_max:
                    best_max = add + child_max

            if idx == 0:
                relax(0)
            elif idx == n - 1:
                relax(1)
            else:
                relax(0)
                relax(1)

            min_dp[idx][prev] = best_min
            max_dp[idx][prev] = best_max

    return min_dp[0][0], max_dp[0][0]

def enumerate_low_states(end, coeff_a, coeff_b):
    out = []
    
    def dfs(idx, prev, sum_b, sum_a, last):
        if idx > end:
            out.append(LowState(sum_b, sum_a, last))
            return
        if idx == 0:
            dfs(1, 0, sum_b, sum_a, 0)
            return

        dfs(idx + 1, 0, sum_b, sum_a, 0)

        if prev == 0:
            dfs(idx + 1, 1, sum_b + coeff_b[idx], sum_a + coeff_a[idx], 1)

    if end < 0:
        out.append(LowState(0, 0, 0))
        return out
        
    dfs(0, 0, 0, 0, 0)
    return out

def enumerate_high_states(start, end, coeff_a, coeff_b):
    out = []
    
    def dfs(idx, prev, sum_b, sum_a, first):
        if idx > end:
            out.append(HighState(sum_b, sum_a, first))
            return

        def first_after(bit):
            return bit if idx == start else first

        if idx == end:
            if prev == 1:
                return
            dfs(idx + 1, 1, sum_b + coeff_b[idx], sum_a + coeff_a[idx], first_after(1))
            return

        dfs(idx + 1, 0, sum_b, sum_a, first_after(0))

        if prev == 0:
            dfs(idx + 1, 1, sum_b + coeff_b[idx], sum_a + coeff_a[idx], first_after(1))

    if start > end:
        out.append(HighState(0, 0, 0))
        return out
        
    dfs(start, 0, 0, 0, 0)
    return out

def solve_sum(limit):
    max_index = 64
    fib = build_fib()
    coeff_a, coeff_b = build_pair_coefficients(fib, max_index)

    total = 1

    for n in range(2, 65):
        min_a, max_a = min_max_possible_a_for_length(n, coeff_a)
        if max_a < 1 or min_a > limit:
            continue

        mid = n // 2
        low_states = enumerate_low_states(mid - 1, coeff_a, coeff_b)
        high_states = enumerate_high_states(mid, n - 1, coeff_a, coeff_b)

        high_maps = [{}, {}]

        for st in high_states:
            b_val = st.b
            if b_val not in high_maps[st.first]:
                high_maps[st.first][b_val] = Bucket()
            high_maps[st.first][b_val].values.append(st.a)

        for fb in range(2):
            for b_val, bucket in high_maps[fb].items():
                bucket.values.sort()
                vals = bucket.values
                pref = [0] * (len(vals) + 1)
                for i in range(len(vals)):
                    pref[i + 1] = pref[i] + vals[i]
                bucket.pref = pref

        for st in low_states:
            for fb in range(2):
                if st.last == 1 and fb == 1:
                    continue
                target_b = -st.b
                if target_b not in high_maps[fb]:
                    continue

                bucket = high_maps[fb][target_b]
                vals = bucket.values
                pref = bucket.pref
                
                low_needed = 1 - st.a
                high_needed = limit - st.a

                lo = bisect.bisect_left(vals, low_needed)
                hi = bisect.bisect_right(vals, high_needed)

                if lo == hi:
                    continue

                count = hi - lo
                sum_high = pref[hi] - pref[lo]
                total += count * st.a + sum_high

    return total

def solve():
    limit = 10_000_000_000
    ans = solve_sum(limit)
    return str(ans)

if __name__ == '__main__':
    print(solve())
