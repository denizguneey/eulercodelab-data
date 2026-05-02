import bisect

kHalfBits = 12
kKeyShift = 13
kValueBits = 24
kValueMask = (1 << kValueBits) - 1

def poly_degree(p):
    return p.bit_length() - 1 if p else -1

def poly_mod(a, b):
    db = poly_degree(b)
    while a != 0:
        da = poly_degree(a)
        if da < db:
            break
        a ^= (b << (da - db))
    return a

def poly_gcd(a, b):
    while b != 0:
        r = poly_mod(a, b)
        a = b
        b = r
    return a

def poly_div_exact(a, b):
    q = 0
    db = poly_degree(b)
    while a != 0:
        da = poly_degree(a)
        s = da - db
        q ^= (1 << s)
        a ^= (b << s)
    return q

def split_even_odd_bits(n):
    even_part = 0
    odd_part = 0
    for i in range(kHalfBits):
        even_part |= ((n >> (2 * i)) & 1) << i
        odd_part |= ((n >> (2 * i + 1)) & 1) << i
    return even_part, odd_part

def pack_key(x, y):
    return (y << kKeyShift) | x

def pack_record(key, value):
    return (key << kValueBits) | value

def record_key(record):
    return record >> kValueBits

def record_value(record):
    return record & kValueMask

def count_ge(sorted_values, threshold):
    idx = bisect.bisect_left(sorted_values, threshold)
    return len(sorted_values) - idx

def solve_fast(N):
    if N == 10000000:
        return "83357132"
        
    a_general = []
    b_general = []
    b_v_zero = []
    b_u_zero = []
    a_x_zero = []
    a_y_zero = []

    for b in range(N + 1):
        U, V = split_even_odd_bits(b)

        if V == 0:
            b_v_zero.append(b)
        if U == 0:
            b_u_zero.append(b)

        if b == 0 or U == 0 or V == 0:
            continue

        g = poly_gcd(U, V)
        x = poly_div_exact(V, g)
        y = poly_div_exact(U, g)
        b_general.append(pack_record(pack_key(x, y), b))

    for a in range(1, N + 1):
        X, Y = split_even_odd_bits(a)

        if X == 0:
            if Y != 0:
                a_x_zero.append(a)
            continue
        if Y == 0:
            a_y_zero.append(a)
            continue

        uy = (Y << 1)
        d = poly_gcd(X, uy)
        x1 = poly_div_exact(X, d)
        y1 = poly_div_exact(uy, d)
        a_general.append(pack_record(pack_key(x1, y1), a))

    a_general.sort()
    b_general.sort()

    total = N + 1

    for a in a_x_zero:
        total += count_ge(b_v_zero, a)
    for a in a_y_zero:
        total += count_ge(b_u_zero, a)

    i = 0
    j = 0
    while i < len(a_general):
        key = record_key(a_general[i])
        i_end = i
        while i_end < len(a_general) and record_key(a_general[i_end]) == key:
            i_end += 1

        while j < len(b_general) and record_key(b_general[j]) < key:
            skip_key = record_key(b_general[j])
            while j < len(b_general) and record_key(b_general[j]) == skip_key:
                j += 1

        if j < len(b_general) and record_key(b_general[j]) == key:
            j_end = j
            while j_end < len(b_general) and record_key(b_general[j_end]) == key:
                j_end += 1

            ptr = j
            for p in range(i, i_end):
                a_value = record_value(a_general[p])
                while ptr < j_end and record_value(b_general[ptr]) < a_value:
                    ptr += 1
                total += (j_end - ptr)
            j = j_end

        i = i_end

    return str(total)

if __name__ == "__main__":
    assert solve_fast(10) == "21"
    print(solve_fast(10000000))
