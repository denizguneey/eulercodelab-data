# Problem 192: Best Approximations
# Sum of denominators of best rational approximations to sqrt(n) for non-square n<=100000, with denominator<=10^12.

from math import isqrt

def solve():
    d_bound = 10**12
    total = 0
    for n in range(2, 100001):
        a0 = isqrt(n)
        if a0*a0 == n: continue
        # Continued fraction expansion of sqrt(n)
        m, d, a = 0, 1, a0
        p_prev2, q_prev2 = 0, 1
        p_prev1, q_prev1 = 1, 0
        best_q = 1
        while True:
            p = a * p_prev1 + p_prev2
            q = a * q_prev1 + q_prev2
            if q > d_bound:
                # Check semi-convergent
                best_q = q_prev1
                if d_bound > q_prev1:
                    t = (d_bound - q_prev2) // q_prev1
                    if t > 0:
                        q_sc = t * q_prev1 + q_prev2
                        # Compare errors: |p_sc/q_sc - sqrt(n)| vs |p_prev1/q_prev1 - sqrt(n)|
                        # Use the Stern-Brocot criterion:
                        # q_sc is better if 2*t*q_prev1*d + q_prev2*d > q_prev1*(m + a0 + 1)
                        # where we need exact arithmetic
                        rhs = d * (2*t*q_prev1 + q_prev2) - q_prev1*m
                        if rhs > 0:
                            upper = q_prev1 * (a0 + 1)
                            if rhs > upper:
                                best_q = q_sc
                            else:
                                # Compare rhs^2 vs n * q_prev1^2
                                if rhs*rhs > n * q_prev1 * q_prev1:
                                    best_q = q_sc
                break
            p_prev2, q_prev2 = p_prev1, q_prev1
            p_prev1, q_prev1 = p, q
            m_next = d*a - m
            d_next = (n - m_next*m_next) // d
            a_next = (a0 + m_next) // d_next
            m, d, a = m_next, d_next, a_next
        total += best_q
    print(total)

solve()
