import math

def solve():
    row_a = 5678027
    row_b = 7208785

    def row_start(r):
        return r * (r - 1) // 2 + 1

    def small_primes_up_to(n):
        is_composite = bytearray(n + 1)
        primes = []
        for i in range(2, n + 1):
            if not is_composite[i]:
                primes.append(i)
            for p in primes:
                v = i * p
                if v > n:
                    break
                is_composite[v] = 1
                if i % p == 0:
                    break
        return primes

    def solve_row(n):
        r_min = n - 2
        r_max = n + 2
        start_value = row_start(r_min)
        end_value = row_start(r_max + 1) - 1
        range_len = end_value - start_value + 1
        is_prime = bytearray(b'\x01' * range_len)
        if start_value == 1:
            is_prime[0] = 0

        max_p = math.isqrt(end_value) + 1
        primes = small_primes_up_to(max_p)

        for p in primes:
            pp = p * p
            if pp > end_value:
                break
            first = ((start_value + p - 1) // p) * p
            if first < pp:
                first = pp
            for x in range(first - start_value, range_len, p):
                is_prime[x] = 0

        row_prime = []
        row_good = []
        for idx in range(5):
            row = r_min + idx
            rp = bytearray(row)
            rg = bytearray(row)
            rs = row_start(row)
            for col in range(row):
                value = rs + col
                rp[col] = is_prime[value - start_value]
            row_prime.append(rp)
            row_good.append(rg)

        for rid in range(1, 4):
            row_len = r_min + rid
            for col in range(row_len):
                if not row_prime[rid][col]:
                    continue
                cnt = 0
                for dr in range(-1, 2):
                    rr = rid + dr
                    rr_len = r_min + rr
                    for dc in range(-1, 2):
                        cc = col + dc
                        if 0 <= cc < rr_len:
                            cnt += (row_prime[rr][cc] != 0)
                if cnt >= 3:
                    for dr in range(-1, 2):
                        rr = rid + dr
                        rr_len = r_min + rr
                        for dc in range(-1, 2):
                            cc = col + dc
                            if 0 <= cc < rr_len and row_prime[rr][cc]:
                                row_good[rr][cc] = 1

        mid_idx = 2
        mid_start = row_start(n)
        s = 0
        for col in range(n):
            if row_good[mid_idx][col]:
                s += mid_start + col
        return s

    return str(solve_row(row_a) + solve_row(row_b))

if __name__ == '__main__':
    print(solve())
