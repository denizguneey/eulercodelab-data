# Problem 209: Circular Logic
# 6-bit truth table with constraint tau(a,b,c,d,e,f) AND tau(b,c,d,e,f,a XOR (b AND c)) != 1
# The mapping x -> next_state decomposes 64 inputs into cycles.
# For each cycle of length L, count independent sets on a circular graph: F(L-1) + F(L+1).

def solve():
    def next_state(x):
        a = (x >> 5) & 1
        b = (x >> 4) & 1
        c = (x >> 3) & 1
        g = a ^ (b & c)
        return ((x & 31) << 1) | g

    visited = [False] * 64
    cycle_lengths = []
    for s in range(64):
        if visited[s]: continue
        length = 0
        cur = s
        while not visited[cur]:
            visited[cur] = True
            cur = next_state(cur)
            length += 1
        cycle_lengths.append(length)

    def count_cycle(L):
        # Independent sets on cycle of length L = F(L-1) + F(L+1)
        fib = [0] * (L + 2)
        fib[0] = 0
        fib[1] = 1
        for i in range(2, L + 2):
            fib[i] = fib[i-1] + fib[i-2]
        return fib[L-1] + fib[L+1]

    ans = 1
    for L in cycle_lengths:
        ans *= count_cycle(L)
    print(ans)

solve()
