import math

def isqrt(x):
    if x < 0:
        raise ValueError("isqrt of negative")
    if x == 0:
        return 0
    return int(math.isqrt(x))

def build_spf(limit):
    spf = [0] * (limit + 1)
    if limit >= 1:
        spf[1] = 1
    for i in range(2, limit + 1):
        if spf[i] == 0:
            spf[i] = i
            if i * i <= limit:
                for j in range(i * i, limit + 1, i):
                    if spf[j] == 0:
                        spf[j] = i
    return spf

class Counter:
    def __init__(self, limit):
        self.spf = build_spf(limit)
        self.alpha = 2.0 - math.sqrt(3.0)
        self.beta = 2.0 + math.sqrt(3.0)
        
        self.inv13 = [0] * 13
        for i in range(1, 13):
            for j in range(1, 13):
                if (i * j) % 13 == 1:
                    self.inv13[i] = j
                    break

    def build_squarefree_divs(self, q):
        divs = [1]
        mus = [1]
        x = q
        while x > 1:
            p = self.spf[x]
            while x % p == 0:
                x //= p
            current = len(divs)
            for i in range(current):
                divs.append(divs[i] * p)
                mus.append(-mus[i])
        return divs, mus

    def coprime_count(self, divs, mus, k_max):
        if k_max <= 0: return 0
        total = 0
        for d, mu in zip(divs, mus):
            total += mu * (k_max // d)
        return total

    def coprime_count_residue(self, divs, mus, k_max, residue):
        if k_max <= 0: return 0
        total = 0
        for d, mu in zip(divs, mus):
            d_mod = d % 13
            inv = self.inv13[d_mod]
            t0 = (residue * inv) % 13
            if t0 == 0: continue
            first = d * t0
            if first > k_max: continue
            total += mu * (1 + (k_max - first) // (13 * d))
        return total

    def compute(self, N):
        q_limit = isqrt(N)
        if q_limit == 0: return 0
        
        total = 0
        
        for q in range(1, q_limit + 1):
            divs, mus = self.build_squarefree_divs(q)
            q2 = q * q
            q_mod13 = q % 13
            residue = 0 if q_mod13 == 0 else (13 - (2 * q_mod13) % 13) % 13
            
            def count_with_residue(k_max):
                if k_max <= 0: return 0
                base = self.coprime_count(divs, mus, k_max)
                if q_mod13 != 0:
                    base -= self.coprime_count_residue(divs, mus, k_max, residue)
                return base
                
            def count_exclude13(k_max):
                if k_max <= 0: return 0
                base = self.coprime_count(divs, mus, k_max)
                if q_mod13 != 0:
                    base -= self.coprime_count(divs, mus, k_max // 13)
                return base
                
            def zA(k):
                return q2 + q * k - 3 * k * k
                
            def zC(k):
                return 13 * q2 + 13 * q * k + 3 * k * k
                
            def zD(k):
                return 3 * k * k - q * k - q2

            # Region A
            k_max = int(math.floor(self.alpha * q))
            if k_max > 0:
                while k_max > 0:
                    x_val = q2 - 4 * q * k_max + k_max * k_max
                    if x_val > 0: break
                    k_max -= 1
                    
                if k_max > 0:
                    base = count_with_residue(k_max)
                    disc = 13 * q2 - 12 * N
                    if disc > 0:
                        s = isqrt(disc)
                        L = (q - s + 5) // 6
                        R = (q + s) // 6
                        while L <= k_max and zA(L) <= N: L += 1
                        while R >= 1 and zA(R) <= N: R -= 1
                        
                        if L <= R and L <= k_max and R >= 1:
                            L2 = max(1, L)
                            R2 = min(k_max, R)
                            if L2 <= R2:
                                forbidden = count_with_residue(R2) - count_with_residue(L2 - 1)
                                base -= forbidden
                    total += base
                    
            disc_plus = 13 * q2 + 12 * N
            s_plus = isqrt(disc_plus)
            
            # Region C
            k_max_c = (s_plus - 13 * q) // 6
            if k_max_c > 0:
                while k_max_c > 0 and zC(k_max_c) > N:
                    k_max_c -= 1
                while zC(k_max_c + 1) <= N:
                    k_max_c += 1
                if k_max_c > 0:
                    total += count_exclude13(k_max_c)
                    
            # Region D
            k_min_d = int(math.floor(self.beta * q)) + 1
            if k_min_d < 1: k_min_d = 1
            while True:
                x_val = q2 - 4 * q * k_min_d + k_min_d * k_min_d
                if x_val > 0: break
                k_min_d += 1
                
            k_max_d = (s_plus + q) // 6
            while k_max_d > 0 and zD(k_max_d) > N:
                k_max_d -= 1
            while zD(k_max_d + 1) <= N:
                k_max_d += 1
                
            if k_min_d <= k_max_d:
                total += count_with_residue(k_max_d) - count_with_residue(k_min_d - 1)
                
        if N >= 3:
            total += 1
            
        return total

def solve():
    N = 100000000000000
    q_limit = isqrt(N)
    c = Counter(q_limit)
    ans = c.compute(N)
    return str(ans)

if __name__ == "__main__":
    print(solve())
