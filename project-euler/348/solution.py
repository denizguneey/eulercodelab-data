import math

def solve():
    target_count = 5

    def isqrt(n):
        return math.isqrt(n)

    def is_palindrome(v):
        s = str(v)
        return s == s[::-1]

    def make_palindrome(prefix, odd_length):
        s = str(prefix)
        if odd_length:
            return int(s + s[-2::-1])
        else:
            return int(s + s[::-1])

    cubes = []
    next_base = [2]

    def ensure_cubes(n):
        while True:
            cube = next_base[0] ** 3
            if cube + 4 > n:
                break
            cubes.append(cube)
            next_base[0] += 1

    def count_reps(n):
        count = 0
        for cube in cubes:
            if cube + 4 > n:
                break
            remaining = n - cube
            root = isqrt(remaining)
            if root >= 2 and root * root == remaining:
                count += 1
                if count > 4:
                    break
        return count

    found = []
    length = 1
    while len(found) < target_count:
        odd_length = (length % 2) == 1
        prefix_digits = (length + 1) // 2
        begin = 1 if length == 1 else 10 ** (prefix_digits - 1)
        end = 10 ** prefix_digits - 1

        for prefix in range(begin, end + 1):
            palindrome = make_palindrome(prefix, odd_length)
            if palindrome < 12:
                continue
            ensure_cubes(palindrome)
            if count_reps(palindrome) == 4:
                found.append(palindrome)
                if len(found) == target_count:
                    break
        length += 1

    return str(sum(found))

if __name__ == '__main__':
    print(solve())
