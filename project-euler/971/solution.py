def solve():
    MOD = 1000000007
    n = 100000000

    is_prime = bytearray(b'\x01'*(n+1)); is_prime[0] = is_prime[1] = 0
    for p in range(2, int(n**0.5)+1):
        if is_prime[p]:
            for j in range(p*p, n+1, p): is_prime[j] = 0
    primes = [i for i in range(2, n+1) if is_prime[i]]

    def mod_pow(base, exp, mod):
        r = 1; base %= mod
        while exp > 0:
            if exp & 1: r = r * base % mod
            base = base * base % mod; exp >>= 1
        return r

    def count_cycle(nxt):
        state = [0]*5; cn = 0
        for start in range(5):
            if state[start]: continue
            stack = []; pos = [-1]*5
            cur = start
            while state[cur] == 0:
                state[cur] = 2; pos[cur] = len(stack)
                stack.append(cur); cur = nxt[cur]
            if state[cur] == 2: cn += len(stack) - pos[cur]
            for v in stack: state[v] = 1
        return cn

    total = 0
    for p in primes:
        if p % 5 != 1: continue
        t = (p - 1) // 5
        omega = 1
        for a in range(2, p):
            omega = mod_pow(a, t, p)
            if omega != 1: break
        po = [1]*5
        for i in range(1, 5): po[i] = po[i-1] * omega % p
        nxt = [0]*5
        ok = True
        for r in range(5):
            val = mod_pow((1 + po[r]) % p, t, p)
            shift = -1
            for i in range(5):
                if po[i] == val: shift = i; break
            if shift < 0: ok = False; break
            nxt[r] = (r + shift) % 5
        if not ok: continue
        total += 1 + t * count_cycle(nxt)

    return str(total)

if __name__ == '__main__':
    print(solve())
