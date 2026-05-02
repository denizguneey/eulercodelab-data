import math
import os
from concurrent.futures import ProcessPoolExecutor


def extinct_for_k(c, d, k):
    if k == 0:
        return True

    s = c + d
    window = [0] * s
    window[s - 1] = k

    zero_count = s - 1
    head = 0
    tap = s - d
    steps = 0

    while True:
        old = window[head]
        nxt = (old + window[tap]) >> 1
        window[head] = nxt

        if old != 0:
            if nxt == 0:
                zero_count += 1
        elif nxt != 0:
            zero_count -= 1

        head += 1
        if head == s:
            head = 0

        tap += 1
        if tap == s:
            tap = 0

        steps += 1
        if (steps & 63) == 0:
            if zero_count == s:
                return True
            if zero_count == 0:
                return False


def extinct_for_k_c1(n, k):
    if k == 0:
        return True

    s = n + 1
    window = [0] * s
    window[s - 1] = k

    zero_count = s - 1
    while True:
        for i in range(s):
            j = i + 1
            if j == s:
                j = 0

            old = window[i]
            nxt = (old + window[j]) >> 1
            window[i] = nxt

            if old != 0:
                if nxt == 0:
                    zero_count += 1
            elif nxt != 0:
                zero_count -= 1

        if zero_count == s:
            return True
        if zero_count == 0:
            return False


def compute_k(c, d):
    lo = 0
    hi = 1

    while extinct_for_k(c, d, hi):
        lo = hi
        hi <<= 1

    while lo + 1 < hi:
        mid = lo + ((hi - lo) >> 1)
        if extinct_for_k(c, d, mid):
            lo = mid
        else:
            hi = mid

    return lo


COEF = [
    (0.17656501777829126, 0.35981185819773187, -9.093343254260652, 128.0591554042931),
    (0.17791093179771922, -0.02526258663290543, 17.778074509864577, -228.639325004742),
    (0.17688473006194433, 0.30195121097992167, -8.649989398001244, 159.32792700127638),
    (0.1774911030303856, 0.09144288721929997, 9.76665768770627, -161.46727161611716),
    (0.17665123701842447, 0.37639947984877686, -14.382073443985455, 264.68150347640244),
    (0.17652781023196232, 0.37645445228054497, -10.389054848768398, 121.34965708864206),
    (0.17725060801487988, 0.15363937288855242, 7.49278183636027, -167.17442628344003),
    (0.17658285799047665, 0.3729423126656912, -11.25711787747357, 179.7243004469314),
]


def estimate_k1(n):
    c0, c1, c2, c3 = COEF[n & 7]
    x = float(n)
    est = ((c0 * x + c1) * x + c2) * x + c3
    if est <= 0.0:
        return 0
    return int(round(est))


def compute_k1_from_estimate(n):
    guess = estimate_k1(n)
    lo = guess - 2048
    if lo < 0:
        lo = 0
    hi = guess + 2048

    while lo > 0 and not extinct_for_k_c1(n, lo):
        hi = lo
        lo >>= 1

    while extinct_for_k_c1(n, hi):
        lo = hi
        hi <<= 1

    while lo + 1 < hi:
        mid = lo + ((hi - lo) >> 1)
        if extinct_for_k_c1(n, mid):
            lo = mid
        else:
            hi = mid

    return lo


def compute_all_k1():
    k1 = [0] * 240
    n_values = list(range(1, 240))

    worker_count = min(64, max(1, (os.cpu_count() or 1) * 2))
    if worker_count == 1:
        for n in n_values:
            k1[n] = compute_k1_from_estimate(n)
        return k1

    try:
        with ProcessPoolExecutor(max_workers=worker_count) as executor:
            for n, value in zip(n_values, executor.map(compute_k1_from_estimate, n_values, chunksize=1)):
                k1[n] = value
    except Exception:
        for n in n_values:
            k1[n] = compute_k1_from_estimate(n)

    return k1


def solve():
    k1 = compute_all_k1()
    k_d1 = [0] * 161

    for c in range(1, 11):
        k_d1[c] = compute_k(c, 1)

    for c in range(11, 161):
        k_d1[c] = k1[(c + 1) // 2]

    def k_for_reduced(rc, rd):
        if rd == 1:
            return k_d1[rc]
        return k1[rd + (rc - 1) // 2]

    def g_value(c, d):
        g = math.gcd(c, d)
        rc = c // g
        rd = d // g
        return 2 * k_for_reduced(rc, rd) + 1

    assert g_value(2, 1) == 7
    assert g_value(1, 2) == 7
    assert g_value(3, 1) == 11
    assert g_value(2, 2) == 3
    assert g_value(1, 3) == 15
    assert k_d1[11] == compute_k(11, 1)
    assert k_d1[57] == compute_k(57, 1)
    assert k_d1[160] == compute_k(160, 1)

    total = 0
    for c in range(1, 161):
        for d in range(1, 161):
            total += g_value(c, d)

    return str(total)


if __name__ == "__main__":
    print(solve())
