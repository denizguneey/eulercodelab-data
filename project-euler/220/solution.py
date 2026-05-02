# Problem 220: Heighway Dragon
# D-string D50 after 10^12 steps of executing F instructions.
# Use segment precomputation: for each level, precompute the net effect
# (displacement + rotation) of executing all F's in a(level) and b(level).

def solve():
    order = 50
    steps = 10**12

    # Segment = (x, y, dir, steps) where dir is rotation (0-3)
    # combine(lhs, rhs): apply rhs after lhs
    def combine(lhs, rhs):
        x, y, d, s = rhs
        # Rotate rhs displacement by lhs.dir
        for _ in range(lhs[2]):
            x, y = y, -x
        return (lhs[0] + x, lhs[1] + y, (lhs[2] + d) & 3, lhs[3] + s)

    F = (1, 0, 0, 1)
    L = (0, 0, 3, 0)  # turn left = -90 degrees
    R = (0, 0, 1, 0)  # turn right = +90 degrees

    # Build a[i] and b[i] segments
    # a0 = aRbFR, b0 = LFaLb (using a1,b1 etc)
    # Base case: a[order] = b[order] = (0,0,0,0) (empty)
    a = [(0, 0, 0, 0)] * (order + 1)
    b = [(0, 0, 0, 0)] * (order + 1)

    for i in range(order - 1, -1, -1):
        a[i] = combine(combine(combine(combine(a[i+1], R), b[i+1]), F), R)
        b[i] = combine(combine(combine(combine(L, F), a[i+1]), L), b[i+1])

    # Walker state
    state = (0, 0, 3, 0)  # facing north
    remaining = steps

    def apply_seg(seg):
        nonlocal state
        state = combine(state, seg)

    def execute_a(level):
        nonlocal remaining
        if remaining == 0 or level >= order:
            return
        full = a[level]
        if remaining >= full[3]:
            remaining -= full[3]
            apply_seg(full)
            return
        execute_a(level + 1)
        if remaining == 0: return
        apply_seg(R)
        execute_b(level + 1)
        if remaining == 0: return
        remaining -= 1
        apply_seg(F)
        if remaining == 0: return
        apply_seg(R)

    def execute_b(level):
        nonlocal remaining
        if remaining == 0 or level >= order:
            return
        full = b[level]
        if remaining >= full[3]:
            remaining -= full[3]
            apply_seg(full)
            return
        apply_seg(L)
        if remaining == 0: return
        remaining -= 1
        apply_seg(F)
        if remaining == 0: return
        execute_a(level + 1)
        if remaining == 0: return
        apply_seg(L)
        execute_b(level + 1)

    # First F step
    if remaining > 0:
        remaining -= 1
        apply_seg(F)
    execute_a(0)

    print(f"{state[0]},{state[1]}")

import sys
sys.setrecursionlimit(200)
solve()
