def solve():
    limit = 1000000
    sieve = bytearray(b'\x01')*(limit); sieve[0] = sieve[1] = 0
    for p in range(2, int(limit**0.5)+1):
        if sieve[p]:
            for q in range(p*p, limit, p): sieve[q] = 0
    total = 0.0; cnt = 0
    for p in range(3, limit):
        if sieve[p]:
            total += (7*p+15)/(18*(p+1)); cnt += 1
    return f"{total/cnt:.10f}"

if __name__ == '__main__':
    print(solve())
