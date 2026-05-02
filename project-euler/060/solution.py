import sys
from typing import List

def mod_mul(a: int, b: int, mod: int) -> int:
    return (a * b) % mod

def mod_pow(base: int, exp: int, mod: int) -> int:
    result = 1
    base %= mod
    while exp > 0:
        if exp & 1:
            result = mod_mul(result, base, mod)
        base = mod_mul(base, base, mod)
        exp >>= 1
    return result

def is_prime_u64(n: int) -> bool:
    if n < 2:
        return False
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for p in small_primes:
        if n == p:
            return True
        if n % p == 0:
            return False
    
    d = n - 1
    s = 0
    while (d & 1) == 0:
        d >>= 1
        s += 1
    
    # Deterministic bases for 64-bit integers
    bases = [2, 325, 9375, 28178, 450775, 9780504, 1795265022]
    for a in bases:
        if a % n == 0:
            continue
        x = mod_pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        witness = True
        for r in range(1, s):
            x = mod_mul(x, x, n)
            if x == n - 1:
                witness = False
                break
        if witness:
            return False
    
    return True

def sieve_primes(limit: int) -> List[int]:
    is_prime = [True] * (limit + 1)
    is_prime[0] = False
    is_prime[1] = False
    
    p = 2
    while p * p <= limit:
        if is_prime[p]:
            for q in range(p * p, limit + 1, p):
                is_prime[q] = False
        p += 1
    
    primes = []
    for p in range(2, limit + 1):
        if is_prime[p] and p != 2 and p != 5:
            primes.append(p)
    
    return primes

def concat_numbers(a: int, b: int) -> int:
    pow10 = 10
    t = b
    while t >= 10:
        t //= 10
        pow10 *= 10
    return a * pow10 + b

def solve(set_size: int, prime_limit: int) -> int:
    primes = sieve_primes(prime_limit)
    n = len(primes)
    
    compatible = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(i + 1, n):
            ab = concat_numbers(primes[i], primes[j])
            ba = concat_numbers(primes[j], primes[i])
            if is_prime_u64(ab) and is_prime_u64(ba):
                compatible[i][j] = 1
                compatible[j][i] = 1
    
    best_sum = float('inf')
    
    chosen = []
    all_indices = list(range(n))
    
    def dfs(candidates: List[int], current_sum: int):
        nonlocal best_sum
        
        if len(chosen) == set_size:
            if current_sum < best_sum:
                best_sum = current_sum
            return
        
        need = set_size - len(chosen)
        if len(candidates) < need:
            return
        
        for idx in range(len(candidates)):
            p_index = candidates[idx]
            next_sum = current_sum + primes[p_index]
            if next_sum >= best_sum:
                continue
            
            chosen.append(p_index)
            
            next_candidates = []
            for j in range(idx + 1, len(candidates)):
                q_index = candidates[j]
                ok = True
                for c_index in chosen:
                    if c_index == q_index:
                        continue
                    if not compatible[c_index][q_index]:
                        ok = False
                        break
                if ok:
                    next_candidates.append(q_index)
            
            dfs(next_candidates, next_sum)
            chosen.pop()
    
    dfs(all_indices, 0)
    return best_sum

def run_checkpoints() -> bool:
    if solve(4, 1000) != 792:
        return False
    return True

def main():
    args = sys.argv[1:]
    
    set_size = 5
    prime_limit = 10000
    run_checkpoints_flag = True
    
    i = 0
    while i < len(args):
        arg = args[i]
        if arg == "--skip-checkpoints":
            run_checkpoints_flag = False
        elif arg.startswith("--set-size="):
            try:
                set_size = int(arg[len("--set-size="):])
            except ValueError:
                print(f"Invalid argument: {arg}", file=sys.stderr)
                sys.exit(1)
        elif arg.startswith("--prime-limit="):
            try:
                prime_limit = int(arg[len("--prime-limit="):])
            except ValueError:
                print(f"Invalid argument: {arg}", file=sys.stderr)
                sys.exit(1)
        else:
            print(f"Unknown argument: {arg}", file=sys.stderr)
            sys.exit(1)
        i += 1
    
    if set_size < 2 or prime_limit < 100:
        print("Invalid parameters", file=sys.stderr)
        sys.exit(1)
    
    if run_checkpoints_flag and not run_checkpoints():
        print("Checkpoint failed for set_size=4", file=sys.stderr)
        sys.exit(2)
    
    print(solve(set_size, prime_limit))

if __name__ == "__main__":
    main()
