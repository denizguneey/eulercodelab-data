kMod = 1000000007
kMaxBlock = 5

def solve():
    target = 10000000
    A = [0, 1, 2, 6, 18, 12]

    fact_small = [1] * (kMaxBlock + 1)
    inv_fact_small = [1] * (kMaxBlock + 1)
    coeff = [0] * (kMaxBlock + 1)

    for i in range(1, kMaxBlock + 1):
        fact_small[i] = (fact_small[i - 1] * i) % kMod
        inv_fact_small[i] = pow(fact_small[i], kMod - 2, kMod)
        coeff[i] = (A[i] * inv_fact_small[i]) % kMod

    H = [0] * (target + 1)
    H[0] = 1

    fact_n = 1

    for n in range(1, target + 1):
        total = 0
        limit = min(n, kMaxBlock)
        for j in range(1, limit + 1):
            total += coeff[j] * H[n - j]
            if total >= kMod:
                total %= kMod
        H[n] = total
        fact_n = (fact_n * n) % kMod

    result = (H[target] * fact_n) % kMod
    return str(result)

if __name__ == "__main__":
    print(solve())
