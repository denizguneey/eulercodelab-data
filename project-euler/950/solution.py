import math

def solve():
    def ceil_div_sqrt(d, D):
        approx = d / math.sqrt(D); g = max(1, int(approx))
        dd = d*d
        while g*g*D < dd: g += 1
        while g > 1 and (g-1)*(g-1)*D >= dd: g -= 1
        return g

    def compute_T(N, C, D):
        groups = [(C, 1)]; s = 1; z = 0; current_c = C; total = C
        while s < N:
            lo = max(1, s - 2*C)
            g = ceil_div_sqrt(lo, D)
            found_d = s; found_b = 0; found_g = 1; found_cost = 0
            for d in range(lo, s+1):
                dd = d*d
                while g*g*D < dd: g += 1
                b = (s-d+1)//2
                if b == 0:
                    found_d = d; found_b = 0; found_g = g; found_cost = 0; break
                # prefix_smallest(b)
                ps = 0; rem = b
                if rem <= z: ps = 0; rem = 0
                else: rem -= z
                for val, cnt in sorted(groups):
                    if rem == 0: break
                    take = min(rem, cnt); ps += take*val; rem -= take
                    if ps > C: ps = C+1; break
                if rem > 0: ps = C+1
                if ps > C: continue
                cost128 = b*g + ps
                if cost128 <= C:
                    found_d = d; found_b = b; found_g = g; found_cost = cost128; break
            next_s = s + found_d
            if next_s > N:
                cnt = N-s; total += cnt*current_c + cnt*(cnt+1)//2; break
            cnt = next_s-s-1
            if cnt > 0: total += cnt*current_c + cnt*(cnt+1)//2
            # advance
            if found_b == 0:
                groups = [(C, 1)]; z = next_s-1; current_c = C
            else:
                z_sel = min(found_b, z); rem = found_b - z_sel
                selected = []
                for val, cnt2 in sorted(groups):
                    if rem == 0: break
                    take = min(rem, cnt2); selected.append((val, take)); rem -= take
                c_new = C - found_cost
                new_entries = []
                if c_new > 0: new_entries.append((c_new, 1))
                if z_sel > 0: new_entries.append((found_g, z_sel))
                for val, cnt2 in selected: new_entries.append((val+found_g, cnt2))
                # normalize
                from collections import defaultdict
                d2 = defaultdict(int)
                for v, c in new_entries:
                    if v > 0 and c > 0: d2[v] += c
                groups = sorted(d2.items())
                pos_count = sum(c for _, c in groups)
                z = next_s - pos_count; current_c = c_new
            total += current_c; s = next_s
        return total

    N = 10**16; ans = 0
    pow10 = 1
    for k in range(1, 7):
        pow10 *= 10; C = pow10+1
        ans += compute_T(N, C, C)
    return str(ans % 1000000000).zfill(9)

if __name__ == '__main__':
    print(solve())
