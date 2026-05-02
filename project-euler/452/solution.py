import math

def solve():
    MOD = 1234567891
    m, n_target = 1000000000, 1000000000

    degree = 0
    while (1 << (degree + 1)) <= m:
        degree += 1

    # Collect distinct floor(m/i) values
    values = []
    i = 1
    while i <= m:
        q = m // i
        j = m // q
        values.append(q)
        i = j + 1
    state_count = len(values)

    sqrt_m = math.isqrt(m)
    while (sqrt_m + 1) ** 2 <= m: sqrt_m += 1
    while sqrt_m * sqrt_m > m: sqrt_m -= 1

    def index_of(q):
        if q <= sqrt_m: return state_count - q
        return m // q - 1

    # Precompute floor division structure for each value
    offsets = []
    q_index = []
    count_mod = []
    for idx in range(state_count):
        v = values[idx]
        offsets.append(len(q_index))
        i = 1
        while i <= v:
            q = v // i
            j = v // q
            q_index.append(index_of(q))
            count_mod.append((j - i + 1) % MOD)
            i = j + 1
    offsets.append(len(q_index))

    prev = [1] * state_count  # F(v,0) = 1
    poly_values = [0] * (degree + 1)
    poly_values[0] = 1

    for t in range(1, degree + 1):
        curr = [0] * state_count
        for idx in range(state_count):
            s = 0
            for p in range(offsets[idx], offsets[idx + 1]):
                s += count_mod[p] * prev[q_index[p]]
            curr[idx] = s % MOD
        prev = curr
        poly_values[t] = prev[0]

    # Newton forward differences
    diff = list(poly_values)
    coeff = [0] * (degree + 1)
    for r in range(degree + 1):
        coeff[r] = diff[0]
        for i in range(degree - r):
            diff[i] = (diff[i + 1] - diff[i]) % MOD

    def choose_small_mod(n_, r):
        if r > n_: return 0
        if r == 0: return 1
        nums = list(range(n_ - r + 1, n_ + 1))
        for d in range(2, r + 1):
            x = d
            for i in range(r):
                if x <= 1: break
                g = math.gcd(nums[i], x)
                if g > 1:
                    nums[i] //= g
                    x //= g
        result = 1
        for v in nums:
            result = result * (v % MOD) % MOD
        return result

    answer = 0
    for r in range(degree + 1):
        c = coeff[r] % MOD
        b = choose_small_mod(n_target, r)
        answer = (answer + c * b) % MOD

    return str(answer)

if __name__ == '__main__':
    print(solve())
