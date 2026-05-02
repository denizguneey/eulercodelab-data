import math

def solve():
    TARGET_PRODUCT = 71328803586048
    MOD = 100_000_000

    def isqrt(n):
        return math.isqrt(n)

    def person_in_room(floor, room):
        if floor == 1:
            first_person = 1
            first_sq_root = 2
        else:
            first_person = (floor * floor) // 2
            first_sq_root = floor if floor & 1 else floor + 1

        if room & 1:  # odd room
            k = (room + 1) // 2
            return first_person + (k - 1) * (2 * first_sq_root + 2 * k - 3)
        else:  # even room
            k = room // 2
            return first_sq_root * first_sq_root - first_person + (k - 1) * (2 * first_sq_root + 2 * k - 1)

    root = isqrt(TARGET_PRODUCT)
    total = 0
    for d in range(1, root + 1):
        if TARGET_PRODUCT % d != 0:
            continue
        q = TARGET_PRODUCT // d
        total += person_in_room(d, q)
        if d != q:
            total += person_in_room(q, d)

    return str(total % MOD)

if __name__ == '__main__':
    print(solve())
