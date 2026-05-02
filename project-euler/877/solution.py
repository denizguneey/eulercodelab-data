def x_fast(n):
    x = 0
    a = 0
    b = 3
    while b <= n:
        x ^= b
        next_val = (b << 1) ^ a
        a = b
        b = next_val
    return x

def solve():
    return str(x_fast(10**18))

if __name__ == "__main__":
    print(solve())
