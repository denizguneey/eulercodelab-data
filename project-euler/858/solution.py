import math

kMod = 1000000007

def mod_norm(x):
    x %= kMod
    if x < 0:
        x += kMod
    return x

def mod_mul(a, b):
    return (mod_norm(a) * mod_norm(b)) % kMod

def primes_up_to(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(math.isqrt(n)) + 1):
        if is_prime[p]:
            for q in range(p * p, n + 1, p):
                is_prime[q] = False
    return [i for i, prime in enumerate(is_prime) if prime]

class Engine:
    def __init__(self, n):
        self.N = n
        primes = primes_up_to(n)
        root = 1
        while (root + 1) ** 2 <= n:
            root += 1

        self.small_primes = [p for p in primes if p <= root]
        self.large_primes = [p for p in primes if p > root]

        k = len(self.small_primes)
        self.max_exp = [0] * k
        self.radix = [0] * k
        self.states = 1

        for i in range(k):
            p = self.small_primes[i]
            e = 0
            v = 1
            while v * p <= self.N:
                v *= p
                e += 1
            self.max_exp[i] = e
            self.radix[i] = e + 1
            self.states *= self.radix[i]

        self.stride = [1] * k
        for i in range(k - 2, -1, -1):
            self.stride[i] = self.stride[i + 1] * self.radix[i + 1]

        self.p_pow = []
        for i in range(k):
            emax = self.max_exp[i]
            pw = [1] * (emax + 1)
            for e in range(1, emax + 1):
                pw[e] = mod_mul(pw[e - 1], self.small_primes[i])
            self.p_pow.append(pw)

        self.small_numbers = []
        exps = [0] * k
        self.gen_small_numbers(0, 1, 0, exps)
        self.small_numbers.sort()

    def gen_small_numbers(self, i, value, idx, exps):
        if i == len(self.small_primes):
            self.small_numbers.append((value, idx))
            return

        v = value
        p = self.small_primes[i]
        base_idx = idx * self.radix[i]
        for e in range(self.max_exp[i] + 1):
            exps[i] = e
            self.gen_small_numbers(i + 1, v, base_idx + e, exps)
            if e == self.max_exp[i]:
                break
            if v > self.N // p:
                break
            v *= p

    def prefix_transform(self, arr):
        k = len(self.small_primes)
        for d in range(k):
            st = self.stride[d]
            block = self.radix[d] * st
            for base in range(0, self.states, block):
                for off in range(st):
                    idx = base + off
                    for e in range(1, self.radix[d]):
                        idx += st
                        arr[idx] += arr[idx - st]

    def counts_for_limit(self, limit):
        arr = [0] * self.states
        for val, idx in self.small_numbers:
            if val > limit:
                break
            arr[idx] = 1
        
        self.prefix_transform(arr)
        return arr

    def solve_mod(self):
        needed_limits = [self.N]
        groups = {}
        for p in self.large_primes:
            L = self.N // p
            if L not in groups:
                groups[L] = []
            groups[L].append(p)
            
        for L in groups.keys():
            needed_limits.append(L)

        needed_limits = sorted(list(set(needed_limits)))

        counts = {}
        for L in needed_limits:
            counts[L] = self.counts_for_limit(L)

        pow2 = [1] * (self.N + 1)
        for i in range(1, self.N + 1):
            pow2[i] = (pow2[i - 1] * 2) % kMod

        group_value = {}
        for L, primes in groups.items():
            table = [1] * (self.N + 1)
            for t in range(self.N + 1):
                v = 1
                for p in primes:
                    term = mod_norm(1 - p + mod_mul(p, pow2[t]))
                    v = mod_mul(v, term)
                table[t] = v
            group_value[L] = table

        ans = 0
        k = len(self.small_primes)

        for idx in range(self.states):
            x = idx
            d = 1
            cut = 1

            for i in range(k - 1, -1, -1):
                e = x % self.radix[i]
                x //= self.radix[i]

                d = mod_mul(d, self.p_pow[i][e])
                if e < self.max_exp[i]:
                    cut = mod_mul(cut, mod_norm(1 - self.small_primes[i]))

            term = mod_mul(d, cut)
            t0 = counts[self.N][idx]
            term = mod_mul(term, pow2[t0])

            for L, table in group_value.items():
                t = counts[L][idx]
                term = mod_mul(term, table[t])

            ans += term
            if ans >= kMod:
                ans -= kMod

        return ans

def solve():
    engine = Engine(800)
    ans = engine.solve_mod()
    return str(ans)

if __name__ == "__main__":
    print(solve())
