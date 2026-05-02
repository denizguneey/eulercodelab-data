def solve():
    FROM = 10000000
    TO = 20000000

    # Segment masks: T, M, B, TL, TR, BL, BR
    masks = [
        0b1111101,  # 0: T|B|TL|TR|BL|BR
        0b1010000,  # 1: TR|BR
        0b0110110,  # 2: T|M|B|TR|BL
        0b1110100,  # 3: T|M|B|TR|BR
        0b1011010,  # 4: M|TL|TR|BR
        0b1101100,  # 5: T|M|B|TL|BR
        0b1101110,  # 6: T|M|B|TL|BL|BR
        0b1011001,  # 7: T|TL|TR|BR (4-seg style)
        0b1111111,  # 8: all
        0b1111100,  # 9: T|M|B|TL|TR|BR
    ]

    # Wait, let me re-derive from the C++ code carefully
    T = 1; M = 2; B = 4; TL = 8; TR = 16; BL = 32; BR = 64
    masks = [
        T|B|TL|TR|BL|BR,       # 0
        TR|BR,                  # 1
        T|M|B|TR|BL,           # 2
        T|M|B|TR|BR,           # 3
        M|TL|TR|BR,            # 4
        T|M|B|TL|BR,           # 5
        T|M|B|TL|BL|BR,       # 6
        T|TL|TR|BR,            # 7
        T|M|B|TL|TR|BL|BR,    # 8
        T|M|B|TL|TR|BR,       # 9
    ]

    def popcount(x):
        return bin(x).count('1')

    def digit_sum(n):
        s = 0
        while n > 0:
            s += n % 10
            n //= 10
        return s

    def digital_root_chain(n):
        chain = []
        while True:
            chain.append(n)
            if n < 10:
                break
            n = digit_sum(n)
        return chain

    def seg_count(n):
        total = 0
        while n > 0:
            total += popcount(masks[n % 10])
            n //= 10
        return total

    def transition_cost(fr, to):
        cost = 0
        while fr > 0 or to > 0:
            a = masks[fr % 10] if fr > 0 else 0
            b = masks[to % 10] if to > 0 else 0
            cost += popcount(a ^ b)
            fr //= 10
            to //= 10
        return cost

    def sam_cost(chain):
        return sum(2 * seg_count(v) for v in chain)

    def max_cost(chain):
        cost = transition_cost(0, chain[0])
        for i in range(1, len(chain)):
            cost += transition_cost(chain[i-1], chain[i])
        cost += transition_cost(chain[-1], 0)
        return cost

    # Sieve primes
    is_prime = bytearray(b'\x01' * TO)
    is_prime[0] = 0
    is_prime[1] = 0
    p = 2
    while p * p < TO:
        if is_prime[p]:
            is_prime[p*p::p] = bytearray(len(is_prime[p*p::p]))
        p += 1

    total_diff = 0
    for p in range(FROM, TO):
        if not is_prime[p]:
            continue
        chain = digital_root_chain(p)
        total_diff += sam_cost(chain) - max_cost(chain)

    return str(total_diff)

if __name__ == '__main__':
    print(solve())
