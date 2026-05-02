from itertools import permutations
from math import gcd

def is_pandigital_0_to_9(s):
    return len(s) == 10 and sorted(s) == list('0123456789')

def collect_divisors(n):
    divs = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            divs.append(d)
            if d * d != n:
                divs.append(n // d)
        d += 1
    divs.sort(reverse=True)
    return divs

def output_has_valid_input(output):
    for split_mask in range(1, 1 << 9):
        products = []
        start = 0
        good_partition = True
        for bit in range(9):
            if not ((split_mask >> bit) & 1):
                continue
            end = bit + 1
            part = output[start:end]
            if len(part) > 1 and part[0] == '0':
                good_partition = False
                break
            products.append(int(part))
            start = end
        if not good_partition:
            continue
        last = output[start:]
        if len(last) > 1 and last[0] == '0':
            continue
        products.append(int(last))
        if len(products) < 2:
            continue
        g = products[0]
        for v in products[1:]:
            g = gcd(g, v)
        for multiplier in collect_divisors(g):
            if multiplier == 0:
                continue
            input_concat = str(multiplier)
            divisible = True
            for v in products:
                if v % multiplier != 0:
                    divisible = False
                    break
                input_concat += str(v // multiplier)
            if not divisible:
                continue
            if is_pandigital_0_to_9(input_concat):
                return True
    return False

def solve():
    digits = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    # Generate all permutations in descending order
    all_perms = sorted(permutations(range(10)), reverse=True)
    for perm in all_perms:
        if perm[0] == 0:
            continue
        output = ''.join(str(d) for d in perm)
        if output_has_valid_input(output):
            return output
    return '0'

if __name__ == '__main__':
    print(solve())
