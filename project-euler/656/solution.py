import math

MOD = 1000000000000000

class SqrtCfTail:
    def __init__(self, value):
        self.D = value
        self.a0 = 0
        while (self.a0 + 1) * (self.a0 + 1) <= self.D:
            self.a0 += 1
        self.m = 0
        self.d = 1
        self.a = self.a0

    def next(self):
        self.m = self.d * self.a - self.m
        self.d = (self.D - self.m * self.m) // self.d
        self.a = (self.a0 + self.m) // self.d
        return self.a

def H_mod(beta, g):
    cf = SqrtCfTail(beta)
    a_terms = []

    def ensure_a(idx):
        while len(a_terms) < idx:
            a_terms.append(cf.next())

    q = [0, 1]
    q_max_idx = 0

    def ensure_q(idx):
        nonlocal q_max_idx
        while q_max_idx < idx:
            next_idx = q_max_idx + 1
            ensure_a(next_idx)
            a_next = a_terms[next_idx - 1]
            q_next = (a_next * q[q_max_idx + 1] + q[q_max_idx]) % MOD
            q.append(q_next)
            q_max_idx += 1

    total_sum = 0
    produced = 0
    block = 0

    while produced < g:
        i = 2 * block + 1
        ensure_q(i - 1)
        ensure_a(i)

        ai = a_terms[i - 1]
        base = q[i - 1]
        step = q[i]

        take = min(ai, g - produced)
        term = base
        for _ in range(take):
            term += step
            if term >= MOD: term -= MOD
            total_sum += term
            if total_sum >= MOD: total_sum -= MOD

        produced += take
        block += 1

    return total_sum

def solve():
    total = 0
    for beta in range(2, 1001):
        r = 0
        while (r + 1) * (r + 1) <= beta:
            r += 1
        if r * r == beta:
            continue
        total = (total + H_mod(beta, 100)) % MOD

    return "{:015d}".format(total)

if __name__ == '__main__':
    print(solve())
