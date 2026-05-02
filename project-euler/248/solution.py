def solve():
    TARGET_PHI = 6_227_020_800  # 13!
    INDEX = 150_000

    def is_prime(n):
        if n < 2:
            return False
        if n < 4:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        d = n - 1
        s = 0
        while d % 2 == 0:
            d //= 2
            s += 1
        for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
            if a % n == 0:
                continue
            x = pow(a, d, n)
            if x == 1 or x == n - 1:
                continue
            witness = True
            for _ in range(s - 1):
                x = (x * x) % n
                if x == n - 1:
                    witness = False
                    break
            if witness:
                return False
        return True

    def factorize(n):
        fac = []
        p = 2
        while p * p <= n:
            if n % p == 0:
                e = 0
                while n % p == 0:
                    n //= p
                    e += 1
                fac.append((p, e))
            p += 1
        if n > 1:
            fac.append((n, 1))
        return fac

    def divisors_of(n):
        fac = factorize(n)
        divs = [1]
        for p, e in fac:
            new_divs = []
            pe = 1
            for _ in range(e + 1):
                for d in divs:
                    new_divs.append(d * pe)
                pe *= p
            divs = new_divs
        divs.sort()
        return divs

    def candidate_primes(phi_target):
        divs = divisors_of(phi_target)
        cands = sorted(set(d + 1 for d in divs if is_prime(d + 1)))
        return cands

    candidates = candidate_primes(TARGET_PHI)

    def dfs(rem_phi, start_index, current_n, out):
        if rem_phi == 1:
            out.append(current_n)
            return
        for i in range(start_index, len(candidates)):
            p = candidates[i]
            phi_piece = p - 1
            if rem_phi % phi_piece != 0:
                continue
            n_piece = p
            while rem_phi % phi_piece == 0:
                out_len_before = len(out)
                dfs(rem_phi // phi_piece, i + 1, current_n * n_piece, out)
                if phi_piece > rem_phi // p:
                    break
                phi_piece *= p
                n_piece *= p

    solutions = []
    dfs(TARGET_PHI, 0, 1, solutions)
    solutions.sort()
    # Remove duplicates
    solutions = sorted(set(solutions))

    return str(solutions[INDEX - 1])

if __name__ == '__main__':
    print(solve())
