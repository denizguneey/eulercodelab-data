import sys
from typing import List

def parse_int_after_prefix(arg: str, prefix: str) -> (bool, int):
    if not arg.startswith(prefix):
        return False, 0
    tail = arg[len(prefix):]
    if not tail:
        return False, 0
    
    try:
        parsed = int(tail)
        return True, parsed
    except ValueError:
        return False, 0

def mul_mod(a: int, b: int, mod: int) -> int:
    return (a * b) % mod

def pow_mod(base: int, exp: int, mod: int) -> int:
    result = 1 % mod
    base %= mod
    while exp > 0:
        if exp & 1:
            result = mul_mod(result, base, mod)
        base = mul_mod(base, base, mod)
        exp >>= 1
    return result

def multiplicative_order_10(p: int) -> int:
    order = p - 1
    x = order
    
    factors = []
    f = 2
    while f * f <= x:
        if x % f == 0:
            factors.append(f)
            while x % f == 0:
                x //= f
        f += 1
    if x > 1:
        factors.append(x)
    
    for q in factors:
        while order % q == 0 and pow_mod(10, order // q, p) == 1:
            order //= q
    
    return order

def primes_below(limit: int) -> List[int]:
    if limit <= 2:
        return []
    
    sieve = [True] * limit
    sieve[0] = False
    sieve[1] = False
    
    i = 2
    while i * i < limit:
        if sieve[i]:
            j = i * i
            while j < limit:
                sieve[j] = False
                j += i
        i += 1
    
    return [i for i in range(2, limit) if sieve[i]]

def can_divide_some_R10n(p: int) -> bool:
    if p in (2, 3, 5):
        return False
    
    ord_val = multiplicative_order_10(p)
    
    while ord_val % 2 == 0:
        ord_val //= 2
    while ord_val % 5 == 0:
        ord_val //= 5
    
    return ord_val == 1

def solve(limit: int) -> int:
    primes = primes_below(limit)
    
    total = 0
    for p in primes:
        if not can_divide_some_R10n(p):
            total += p
    
    return total

def run_checkpoints() -> bool:
    if solve(100) != 918:
        return False
    if not can_divide_some_R10n(17) or can_divide_some_R10n(19) or can_divide_some_R10n(3):
        return False
    return True

def main():
    limit = 100000
    run_checkpoints_flag = True
    
    args = sys.argv[1:]
    for arg in args:
        if arg == "--skip-checkpoints":
            run_checkpoints_flag = False
        elif arg.startswith("--limit="):
            success, value = parse_int_after_prefix(arg, "--limit=")
            if success:
                limit = value
        else:
            print(f"Unknown argument: {arg}", file=sys.stderr)
            sys.exit(1)
    
    if limit < 2:
        print("Limit must be at least 2", file=sys.stderr)
        sys.exit(1)
    
    if run_checkpoints_flag and not run_checkpoints():
        print("Checkpoint failed", file=sys.stderr)
        sys.exit(2)
    
    print(solve(limit))

if __name__ == "__main__":
    main()
