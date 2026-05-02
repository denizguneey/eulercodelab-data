import sys
import math

sys.setrecursionlimit(2000)

memo_F = {}

def floor_div(a, b):
    return a // b

def isqrt_floor(n):
    r = int(math.sqrt(n))
    while (r + 1) ** 2 <= n:
        r += 1
    while r * r > n:
        r -= 1
    return r

def points_in_trapezoid(slope, intercept, denominator, lower_domain, upper_domain, boundary):
    result = 0
    while True:
        if abs(upper_domain - lower_domain) <= 8:
            s = 0
            adjustment = 0 if boundary else 1
            if upper_domain > lower_domain:
                for x in range(lower_domain + 1, upper_domain + 1):
                    s += floor_div(slope * x + intercept - adjustment, denominator)
            else:
                for x in range(upper_domain + 1, lower_domain + 1):
                    s += floor_div(slope * x + intercept - adjustment, denominator)
                s = -s
            result += s
            break

        result += (upper_domain - lower_domain) * floor_div(intercept, denominator)
        intercept %= denominator
        
        result += ((upper_domain - lower_domain) * (upper_domain + lower_domain + 1) // 2) * floor_div(slope, denominator)
        slope %= denominator

        if slope != 0:
            upper_value = floor_div(slope * upper_domain + intercept, denominator)
            lower_value = floor_div(slope * lower_domain + intercept, denominator)
            result += upper_domain * upper_value - lower_domain * lower_value
            lower_domain, upper_domain = upper_value, lower_value
            slope, denominator = denominator, slope
            intercept = -intercept
            boundary = not boundary
        else:
            if intercept == 0 and not boundary:
                result -= upper_domain - lower_domain
            break
            
    return result

def points_in_trapezoid_mod2(slope, intercept, denominator, lower_domain, upper_domain, boundary, x_residue, y_residue):
    if (y_residue & 1) != 0:
        intercept += denominator
    if (x_residue & 1) != 0:
        intercept -= slope
        lower_domain += 1
        upper_domain += 1
        
    return points_in_trapezoid(2 * slope, intercept, 2 * denominator,
                               floor_div(lower_domain, 2), floor_div(upper_domain, 2), boundary)

def f_value(n):
    result = 0
    three_halves_n = n + n // 2
    root = isqrt_floor(three_halves_n)
    ij = [(0, 1), (1, 0), (1, 1)]
    
    for i, j in ij:
        max_t = 1
        for s in range(2, root):
            if 3 * (max_t + 1) ** 2 <= s * s:
                max_t += 1
            if i == j or (s & 1) == 0:
                start_t = ((s - 1) & 1) + 1
                for t in range(start_t, max_t + 1, 2):
                    v_mid = t * n // ((s - t) * (s + t))
                    v_max = n * (s + t) // (s * s + 2 * s * t - t * t)
                    result += points_in_trapezoid_mod2(s, 0, t, 0, v_mid, True, j, i)
                    result += points_in_trapezoid_mod2(t, n, s, v_mid, v_max, True, j, i)
                    result -= points_in_trapezoid_mod2(s + 3 * t, 0, s + t, 0, v_max, False, j, i)
                    
        u_max = three_halves_n // root
        start_u = 1 + ((i + 1) & 1)
        for u in range(start_u, u_max + 1, 2):
            v_max_outer = min(n // 2, u - 1)
            start_v = 1 + ((j + 1) & 1)
            for v in range(start_v, v_max_outer + 1, 2):
                mid_s = (v + n) // u
                residue_count = 2 if i == j else 1
                
                for sr in range(residue_count):
                    s_residue = sr if i == j else 0
                    
                    if u * u < 3 * v * v:
                        min_s = root
                        max_s = n * (3 * v - u) // (2 * u * v + v * v - u * u)
                        slope0 = u - v
                        slope1 = 3 * v - u
                    else:
                        min_s = max(root, floor_div(u + v - 1, v))
                        max_s = n * u // ((u - v) * (u + v))
                        slope0 = v
                        slope1 = u
                        
                    if max_s >= min_s:
                        result += points_in_trapezoid_mod2(slope0, 0, slope1,
                                                           min_s - 1, max_s, True,
                                                           s_residue, s_residue)
                        if mid_s < max_s:
                            result -= points_in_trapezoid_mod2(u, -n, v,
                                                               max(mid_s, min_s - 1), max_s,
                                                               False, s_residue, s_residue)
    return result

def F(n):
    if n <= 0: return 0
    if n in memo_F: return memo_F[n]
    
    result = f_value(n)
    k = 3
    n_over_k = n // k
    while k <= n_over_k:
        result -= F(n_over_k)
        k += 2
        n_over_k = n // k
        
    min_k = n // (n_over_k + 1) if n_over_k + 1 > 0 else n
        
    while n_over_k > 0:
        max_k = n // n_over_k
        left = (min_k + 1) + (min_k & 1)
        right = max_k - ((max_k + 1) & 1)
        count = 0
        if right >= left:
            count = (right - left) // 2 + 1
        result -= F(n_over_k) * count
        n_over_k -= 1
        min_k = max_k
        
    memo_F[n] = result
    return result

def solve():
    n = 100000
    ans = F(n)
    return str(ans)

if __name__ == '__main__':
    print(solve())
