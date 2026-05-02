def solve():
    # Euler 494: Collatz backward counting
    # The C++ uses a complex backward expansion of the Collatz tree
    # For a simpler approach, use the same algorithm
    steps = 90
    # Fibonacci for counting "straight" paths
    def fib(n):
        if n <= 0: return 0
        if n <= 2: return 1
        a, b = 1, 1
        for _ in range(n - 2):
            a, b = b, a + b
        return b

    def coll_length(n):
        length = 0
        while n & (n - 1):  # not a power of 2
            length += 1
            if n & 1: n = 3 * n + 1
            else: n >>= 1
        return length

    seeds = [9, 19, 37, 51, 155, 159]
    total = fib(steps)
    for s in seeds:
        cl = coll_length(s)
        rem = steps - cl
        if rem < 0: continue
        if s % 3 == 0: rem = 0
        # Expand backward rem steps
        states = [s]
        for _ in range(rem):
            nxt = []
            for a in states:
                nxt.append(a << 1)
                if a % 6 == 4:
                    nxt.append(a // 3)
            states = nxt
        total += len(states)
    return str(total)

if __name__ == '__main__':
    print(solve())
