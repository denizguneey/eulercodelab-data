def next_turn_after(t, mod_val):
    candidate = t + 1
    r = candidate % 3
    if r == mod_val:
        return candidate
    add = (mod_val + 3 - r) % 3
    return candidate + add

def compute_F(A, B, C):
    role_mod = [1, 2, 0]
    role_base = [1, 2, 3]
    roles = []
    base_role = -1

    while True:
        if A == B + C:
            roles.append(0)
            if B == C:
                base_role = 0
                break
            A = (B - C) if B >= C else (C - B)
        elif B == A + C:
            roles.append(1)
            if A == C:
                base_role = 1
                break
            B = (A - C) if A >= C else (C - A)
        else:
            roles.append(2)
            if A == B:
                base_role = 2
                break
            C = (A - B) if A >= B else (B - A)

    turns = role_base[base_role]
    roles.pop()
    for role in reversed(roles):
        turns = next_turn_after(turns, role_mod[role])
    return turns

def solve():
    total = 0
    for a in range(1, 8):
        for b in range(1, 20):
            A = pow(a, b)
            B = pow(b, a)
            C = A + B
            total += compute_F(A, B, C)
    return str(total)

if __name__ == "__main__":
    print(solve())
