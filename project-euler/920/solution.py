def pow_capped(base, exp, cap):
    result = 1
    for _ in range(exp):
        if result > cap // base:
            return cap + 1
        result *= base
    return result

def mul_pow_capped(value, base, exp, cap):
    for _ in range(exp):
        if value > cap // base:
            return cap + 1
        value *= base
    return value

def sieve_primes(max_n):
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(max_n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_n + 1, i):
                is_prime[j] = False
    return [i for i, prime in enumerate(is_prime) if prime]

class TauSolver:
    def __init__(self, limit):
        self.limit = limit
        self.primes = sieve_primes(300000)
        self.factor_cache = {}
        self.best = {}

    def factorize(self, x):
        if x in self.factor_cache:
            return self.factor_cache[x]

        factors = []
        value = x
        for prime in self.primes:
            if prime * prime > value:
                break
            if value % prime == 0:
                exponent = 0
                while value % prime == 0:
                    value //= prime
                    exponent += 1
                factors.append({'prime': prime, 'need': exponent})
        if value > 1:
            factors.append({'prime': value, 'need': 1})

        self.factor_cache[x] = factors
        return factors

    def build_extra_primes(self, count, mandatory):
        blocked = {req['prime'] for req in mandatory}
        extras = []
        for prime in self.primes:
            if prime not in blocked:
                extras.append(prime)
                if len(extras) == count:
                    break
        return extras

    def minimal_value_for_vector(self, exponents, factors):
        r = len(exponents)
        t = len(factors)
        if t > r:
            return self.limit + 1

        mandatory = sorted(factors, key=lambda f: (-f['prime'], -f['need']))
        if mandatory and (not exponents or exponents[0] < mandatory[0]['need']):
            for req in mandatory:
                if not exponents or exponents[0] < req['need']:
                    return self.limit + 1

        extras = self.build_extra_primes(r - t, mandatory)
        used = [False] * r
        best = [self.limit + 1]

        def dfs_assign(idx, current):
            if current >= best[0]:
                return

            if idx == t:
                value = current
                extra_idx = 0
                for i in range(r):
                    if used[i]:
                        continue
                    value = mul_pow_capped(value, extras[extra_idx], exponents[i], self.limit)
                    if value > self.limit or value >= best[0]:
                        return
                    extra_idx += 1
                best[0] = min(best[0], value)
                return

            previous_exp = -1
            for i in range(r):
                if used[i]:
                    continue
                exp = exponents[i]
                if exp < mandatory[idx]['need']:
                    continue
                if exp == previous_exp:
                    continue
                previous_exp = exp

                multiplied = mul_pow_capped(current, mandatory[idx]['prime'], exp, self.limit)
                if multiplied > self.limit or multiplied >= best[0]:
                    continue
                used[i] = True
                dfs_assign(idx + 1, multiplied)
                used[i] = False

        dfs_assign(0, 1)
        return best[0]

    def dfs_vectors(self, prime_idx, max_exp, current_value, tau_value, exponents):
        factors = self.factorize(tau_value)
        candidate = self.minimal_value_for_vector(exponents, factors)
        if candidate <= self.limit:
            if tau_value not in self.best or candidate < self.best[tau_value]:
                self.best[tau_value] = candidate

        if prime_idx >= len(self.primes):
            return

        prime = self.primes[prime_idx]
        value = current_value
        for exp in range(1, max_exp + 1):
            if value > self.limit // prime:
                break
            value *= prime

            new_tau = tau_value * (exp + 1)

            exponents.append(exp)
            self.dfs_vectors(prime_idx + 1, exp, value, new_tau, exponents)
            exponents.pop()

    def compute_minimals(self):
        self.best.clear()
        self.factor_cache.clear()
        exponents = []
        self.dfs_vectors(0, 64, 1, 1, exponents)
        return self.best

def solve():
    kLimit = 10**16
    solver = TauSolver(kLimit)
    minima = solver.compute_minimals()
    ans = sum(minima.values())
    return str(ans)

if __name__ == "__main__":
    print(solve())
