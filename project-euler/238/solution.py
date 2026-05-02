def solve():
    MODULUS = 20300713
    SEED = 14025256

    s = SEED
    seen = {}
    index = 0
    w_digits = []

    while s not in seen:
        seen[s] = index
        s_str = str(s)
        for c in s_str:
            w_digits.append(int(c))
        s = (s * s) % MODULUS
        index += 1

    L = len(w_digits)
    prefix_sum = [0] * (L + 1)
    for i in range(L):
        prefix_sum[i + 1] = prefix_sum[i] + w_digits[i]
    S = prefix_sum[L]

    R = bytearray(S + 1)
    for i in range(L + 1):
        R[prefix_sum[i] % S] = 1

    P_mod_S = [prefix_sum[i] % S for i in range(L)]

    p_vals = [0] * (S + 1)
    for k in range(1, S + 1):
        z = 1
        while True:
            start_residue = P_mod_S[(z - 1) % L]
            target = start_residue + k
            if target >= S:
                target -= S
            if R[target]:
                p_vals[k] = z
                break
            z += 1

    LIMIT = 2_000_000_000_000_000
    num_periods = LIMIT // S
    remainder = LIMIT % S

    sum_one = sum(p_vals[1:S+1])
    sum_rem = sum(p_vals[1:remainder+1])

    answer = num_periods * sum_one + sum_rem
    return str(answer)

if __name__ == '__main__':
    print(solve())
