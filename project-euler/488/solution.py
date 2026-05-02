import multiprocessing

MOD = 1000000000

def add_mod(a, b):
    return (a + b) % MOD

def sub_mod(a, b):
    return (a - b) % MOD if a >= b else (a + MOD - b) % MOD

def mul_mod(a, b):
    return (a * b) % MOD

def sum_linear_mod(m):
    if m == 0: return 0
    a, b = m, m + 1
    if a % 2 == 0:
        a //= 2
    else:
        b //= 2
    return mul_mod(a, b)

def sum_square_mod(m):
    if m == 0: return 0
    a, b, c = m, m + 1, 2 * m + 1
    if a % 2 == 0: a //= 2
    elif b % 2 == 0: b //= 2
    else: c //= 2
        
    if a % 3 == 0: a //= 3
    elif b % 3 == 0: b //= 3
    else: c //= 3
        
    return mul_mod(mul_mod(a, b), c)

def sum_choose2_mod(m):
    if m <= 1: return 0
    a, b, c = m, m + 1, m - 1
    if a % 2 == 0: a //= 2
    elif b % 2 == 0: b //= 2
    else: c //= 2
        
    if a % 3 == 0: a //= 3
    elif b % 3 == 0: b //= 3
    else: c //= 3
        
    return mul_mod(mul_mod(a, b), c)

class Solver488:
    def __init__(self):
        self.s_pow2_mod = [0] * 63
        self.c_mod = [0] * 63
        self.precompute_prefix_xor_sums()

    def precompute_prefix_xor_sums(self):
        for m in range(63):
            p = 1 << m
            x, y = p, 3 * p - 1
            if x % 2 == 0: x //= 2
            else: y //= 2
            self.c_mod[m] = mul_mod(x % MOD, y % MOD)
            
        for m in range(62):
            p = (1 << m) % MOD
            term = mul_mod(p, self.c_mod[m])
            self.s_pow2_mod[m + 1] = add_mod(add_mod(self.s_pow2_mod[m], self.s_pow2_mod[m]), term)

    def prefix_sum_x_mod(self, n):
        if n <= 1: return 0
        msb = n.bit_length() - 1
        p = 1 << msb
        if n == p: return self.s_pow2_mod[msb]
        r = n - p
        term = mul_mod(r % MOD, self.c_mod[msb])
        return add_mod(add_mod(self.s_pow2_mod[msb], term), self.prefix_sum_x_mod(r))

    def block_sum_mod(self, p, m):
        s_x = self.prefix_sum_x_mod(m + 1)
        s1 = sum_linear_mod(m)
        s2 = sum_square_mod(m)
        sC2 = sum_choose2_mod(m)

        two_p_minus_one = (2 * (p % MOD) - 1) % MOD
        total = add_mod(add_mod(add_mod(s_x, s2), sC2), mul_mod(two_p_minus_one, s1))

        odd_cnt = (m + 1) // 2
        odd_sq = mul_mod(odd_cnt % MOD, odd_cnt % MOD)
        correction = add_mod(mul_mod(odd_cnt % MOD, two_p_minus_one), mul_mod(2, odd_sq))
        
        return sub_mod(total, correction)

def worker_func(start_idx, end_idx, blocks, solver):
    local_sum = 0
    for i in range(start_idx, end_idx):
        local_sum = add_mod(local_sum, solver.block_sum_mod(blocks[i][0], blocks[i][1]))
    return local_sum

def solve_multiprocessing(N):
    solver = Solver488()
    blocks = []
    for k in range(1, 63):
        p = (1 << k) - 1
        if p + 1 >= N: break
        m = min(p, N - 1 - p)
        blocks.append((p, m))
        
    if not blocks:
        return 0

    threads = multiprocessing.cpu_count()
    if threads == 0: threads = 1
    threads = min(threads, len(blocks))
    if len(blocks) < 8: threads = 1

    if threads == 1:
        ans = 0
        for p, m in blocks:
            ans = add_mod(ans, solver.block_sum_mod(p, m))
        return ans

    chunk_size = (len(blocks) + threads - 1) // threads
    tasks = []
    for i in range(threads):
        start = i * chunk_size
        end = min(len(blocks), start + chunk_size)
        tasks.append((start, end, blocks, solver))

    with multiprocessing.Pool(threads) as pool:
        results = pool.starmap(worker_func, tasks)

    ans = 0
    for res in results:
        ans = add_mod(ans, res)
    return ans

def solve():
    N = 1000000000000000000
    ans = solve_multiprocessing(N)
    return f"{ans:09d}"

if __name__ == '__main__':
    print(solve())
