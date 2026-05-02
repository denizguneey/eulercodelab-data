def solve():
    prime_limit = 5000
    modulo = 10**16

    sieve = bytearray(b'\x01' * prime_limit)
    sieve[0] = 0
    sieve[1] = 0
    for i in range(2, prime_limit):
        if i * i >= prime_limit:
            break
        if sieve[i]:
            for j in range(i * i, prime_limit, i):
                sieve[j] = 0
    primes = [i for i in range(2, prime_limit) if sieve[i]]

    max_sum = sum(primes)
    ways = [0] * (max_sum + 1)
    ways[0] = 1
    current_sum = 0
    for p in primes:
        for s in range(current_sum, -1, -1):
            add = ways[s]
            if add == 0:
                continue
            ways[s + p] = (ways[s + p] + add) % modulo
        current_sum += p

    is_prime_sum = bytearray(b'\x01' * (max_sum + 1))
    is_prime_sum[0] = 0
    is_prime_sum[1] = 0
    for i in range(2, max_sum + 1):
        if i * i > max_sum:
            break
        if is_prime_sum[i]:
            for j in range(i * i, max_sum + 1, i):
                is_prime_sum[j] = 0

    answer = 0
    for s in range(2, max_sum + 1):
        if is_prime_sum[s]:
            answer = (answer + ways[s]) % modulo
    return str(answer)

if __name__ == '__main__':
    print(solve())
