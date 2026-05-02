def solve(exponent=30):
    bits = exponent + 1
    fib = [0] * (bits + 2)
    fib[1] = 1
    for i in range(2, bits + 2):
        fib[i] = fib[i - 1] + fib[i - 2]
    return str(fib[bits + 1])

if __name__ == '__main__':
    print(solve())
