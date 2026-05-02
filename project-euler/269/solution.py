def pow10i(exp):
    return 10**exp

def count_subset_for_length(length, last_digit, roots):
    if not roots:
        return 0

    even_slots = (length + 1) // 2
    msd_pos = length - 1

    zero_state = tuple(0 for _ in roots)
    states = {zero_state: 1}

    for j in range(even_slots):
        even_pos = 2 * j
        odd_pos = 2 * j + 1

        if j == 0:
            even_digits = [last_digit]
        else:
            even_digits = list(range(10))

        if even_pos == msd_pos:
            even_digits = [d for d in even_digits if d != 0]

        if odd_pos >= length:
            odd_digits = [0]
        else:
            odd_digits = list(range(10))
            if odd_pos == msd_pos:
                odd_digits = [d for d in odd_digits if d != 0]

        next_states = {}
        for carry, ways in states.items():
            for ed in even_digits:
                for od in odd_digits:
                    next_carry = []
                    ok = True
                    for idx, t in enumerate(roots):
                        denom = t * t
                        num = t * od + carry[idx] - ed
                        if num % denom != 0:
                            ok = False
                            break
                        next_carry.append(num // denom)
                    
                    if not ok:
                        continue
                        
                    next_carry_tuple = tuple(next_carry)
                    next_states[next_carry_tuple] = next_states.get(next_carry_tuple, 0) + ways

        states = next_states
        if not states:
            return 0

    return states.get(zero_state, 0)

def count_for_length(length):
    total = 0
    if length >= 2:
        total += 9 * pow10i(length - 2)

    for d0 in range(1, 10):
        divisors = [t for t in range(1, 10) if d0 % t == 0]
        m = len(divisors)
        union_count = 0

        for mask in range(1, 1 << m):
            roots = []
            for i in range(m):
                if (mask >> i) & 1:
                    roots.append(divisors[i])

            cnt = count_subset_for_length(length, d0, roots)
            if mask.bit_count() & 1:
                union_count += cnt
            else:
                union_count -= cnt

        total += union_count

    return total

def solve_power(max_power):
    total = 0
    for length in range(1, max_power + 1):
        total += count_for_length(length)

    total += 1
    return total

def solve():
    ans = solve_power(16)
    return str(ans)

if __name__ == '__main__':
    print(solve())
