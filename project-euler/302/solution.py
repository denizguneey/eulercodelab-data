import sys

sys.setrecursionlimit(20000)

class Solver:
    def __init__(self):
        self.kPrimeSieveN = 6 * 105000
        self.primes = []
        
        erat = [0] * (self.kPrimeSieveN + 1)
        erat[1] = 1
        
        self.primes.append(2)
        self.primes.append(3)
        
        sq = int(self.kPrimeSieveN ** 0.5)
        for i in range(0, sq + 1, 6):
            if not erat[i + 1]:
                p = i + 1
                step = p * 6
                for j in range(p * p, self.kPrimeSieveN + 1, step): erat[j] = 1
                for j in range(p * (p + 4), self.kPrimeSieveN + 1, step): erat[j] = 1
                self.primes.append(p)
            if not erat[i + 5]:
                p = i + 5
                step = p * 6
                for j in range(p * p, self.kPrimeSieveN + 1, step): erat[j] = 1
                for j in range(p * (p + 2), self.kPrimeSieveN + 1, step): erat[j] = 1
                self.primes.append(p)
                
        start = sq - (sq % 6) + 6
        for i in range(start, self.kPrimeSieveN, 6):
            if not erat[i + 1]: self.primes.append(i + 1)
            if not erat[i + 5]: self.primes.append(i + 5)
            
        self.prime_count = len(self.primes)
        
        self.divisors = [[] for _ in range(self.kPrimeSieveN + 1)]
        for i, p in enumerate(self.primes):
            deg = p
            while deg <= self.kPrimeSieveN:
                for j in range(deg, self.kPrimeSieveN + 1, deg):
                    self.divisors[j].append(i)
                if deg <= self.kPrimeSieveN // p:
                    deg *= p
                else:
                    break
                    
        self.answer = 0

    def gcd_small(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def cube_root_floor(self, n):
        if n <= 1: return int(n)
        r = int(n ** (1.0 / 3.0))
        while (r + 1) * (r + 1) * (r + 1) <= n: r += 1
        while r * r * r > n: r -= 1
        return r

    def count_recursive(self, max_prime_idx, active_factors, active_count, gcd_exp_n, gcd_exp_phi, lim):
        if lim == 0: return

        if gcd_exp_n == 1:
            g = gcd_exp_phi
            i = 0
            while i < active_count:
                j = i + 1
                while j < active_count and active_factors[j] == active_factors[i]:
                    j += 1
                cnt = j - i
                if cnt < 2:
                    g = 0
                    break
                g = self.gcd_small(g, cnt)
                i = j
            if g == 1:
                self.answer += 1

        min_idx = 0
        if active_count >= 2:
            if active_factors[active_count - 1] != active_factors[active_count - 2]:
                min_idx = active_factors[active_count - 1]
            else:
                for k in range(active_count - 2, 0, -1):
                    if active_factors[k] != active_factors[k + 1] and active_factors[k] != active_factors[k - 1]:
                        min_idx = active_factors[k]
                        break
        elif active_count == 1:
            min_idx = active_factors[0]

        max_idx = self.cube_root_floor(lim)
        if self.primes[max_prime_idx - 1] > max_idx:
            a = 0
            b = self.prime_count - 1
            while a < b - 1:
                c = (a + b) // 2
                if self.primes[c] > max_idx:
                    b = c
                else:
                    a = c
            max_idx = a
        if max_idx > max_prime_idx - 1:
            max_idx = max_prime_idx - 1

        merged = [0] * 70
        j = active_count - 1
        while j >= 0:
            overdeg = 0
            y = j
            while y >= 0 and active_factors[y] == active_factors[j]:
                overdeg += 1
                y -= 1

            if active_factors[j] < max_prime_idx:
                k1 = 0
                k2 = 0
                merged_count = 0
                idx = active_factors[j]
                p_minus_one = self.primes[idx] - 1
                divs = self.divisors[p_minus_one]
                div_cnt = len(divs)

                while k1 < active_count and k2 < div_cnt:
                    if active_factors[k1] < divs[k2]:
                        merged[merged_count] = active_factors[k1]
                        k1 += 1
                    else:
                        merged[merged_count] = divs[k2]
                        k2 += 1
                    merged_count += 1
                while k2 < div_cnt:
                    merged[merged_count] = divs[k2]
                    k2 += 1
                    merged_count += 1
                while k1 < active_count:
                    merged[merged_count] = active_factors[k1]
                    k1 += 1
                    merged_count += 1

                g2 = gcd_exp_phi
                while merged_count > 0 and merged[merged_count - 1] > active_factors[j]:
                    y = merged_count - 1
                    while y >= 0 and merged[y] == merged[merged_count - 1]:
                        y -= 1
                    g2 = self.gcd_small(g2, merged_count - y - 1)
                    merged_count = y + 1
                if merged_count > 0 and merged[merged_count - 1] == active_factors[j]:
                    merged_count -= overdeg

                p = self.primes[idx]
                pow_val = p
                deg = 2
                while pow_val <= lim // p:
                    new_g1 = self.gcd_small(gcd_exp_n, deg)
                    new_g2 = self.gcd_small(g2, deg - 1 + overdeg)
                    self.count_recursive(idx, merged, merged_count, new_g1, new_g2, lim // pow_val // p)

                    pow_val *= p
                    deg += 1

            j -= overdeg
            if overdeg == 1: break

        now = 0
        while now < active_count and active_factors[now] < min_idx:
            now += 1

        for idx in range(min_idx, max_idx + 1):
            if now < active_count and idx == active_factors[now]:
                while now < active_count and active_factors[now] == idx:
                    now += 1
                continue

            k1 = 0
            k2 = 0
            merged_count = 0
            p_minus_one = self.primes[idx] - 1
            divs = self.divisors[p_minus_one]
            div_cnt = len(divs)

            while k1 < active_count and k2 < div_cnt:
                if active_factors[k1] < divs[k2]:
                    merged[merged_count] = active_factors[k1]
                    k1 += 1
                else:
                    merged[merged_count] = divs[k2]
                    k2 += 1
                merged_count += 1
            while k2 < div_cnt:
                merged[merged_count] = divs[k2]
                k2 += 1
                merged_count += 1
            while k1 < active_count:
                merged[merged_count] = active_factors[k1]
                k1 += 1
                merged_count += 1

            g2 = gcd_exp_phi
            while merged_count > 0 and merged[merged_count - 1] > idx:
                y = merged_count - 1
                while y >= 0 and merged[y] == merged[merged_count - 1]:
                    y -= 1
                g2 = self.gcd_small(g2, merged_count - y - 1)
                merged_count = y + 1

            p = self.primes[idx]
            pow_val = p * p
            deg = 3
            while pow_val <= lim // p:
                new_g1 = self.gcd_small(gcd_exp_n, deg)
                new_g2 = self.gcd_small(g2, deg - 1)
                self.count_recursive(idx, merged, merged_count, new_g1, new_g2, lim // pow_val // p)

                pow_val *= p
                deg += 1

    def solve_main(self, limit):
        self.answer = 0
        root_factors = [0] * 70
        self.count_recursive(self.prime_count, root_factors, 0, 0, 0, limit)
        return self.answer

def solve(limit=10**18):
    solver = Solver()
    return str(solver.solve_main(limit))

if __name__ == '__main__':
    print(solve())
