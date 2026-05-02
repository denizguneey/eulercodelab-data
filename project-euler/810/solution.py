def solve():
    M = 27; N = 5000000
    size = 1 << M
    is_prime = bytearray(b'\x01' * size)
    count = 1
    if N == 1: return '2'

    for i in range(3, size, 2):
        if not is_prime[i]: continue
        count += 1
        if count == N: return str(i)
        l = i.bit_length()
        j_start = l - 1; j_end = M - l
        if j_start > j_end: continue
        for j in range(j_start, j_end + 1):
            k = i << j
            limit = 1 << j
            for n in range(1, limit + 1):
                is_prime[k] = 0
                k ^= i * (n & (~n + 1))

    return '0'

if __name__ == '__main__':
    print(solve())
