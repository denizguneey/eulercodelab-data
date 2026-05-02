import math

def isqrt(n):
    if n < 0:
        return 0
    return math.isqrt(n)

def solve(N):
    y_max = isqrt((4 * N) // 163)
    total = 0
    
    for y in range(-y_max, y_max + 1):
        yy = abs(y)
        rem = 4 * N - 163 * yy * yy
        if rem < 0:
            continue
        m = isqrt(rem)
        
        if y % 2 == 0:
            cnt = m + 1 if m % 2 == 0 else m
        else:
            cnt = m if m % 2 == 0 else m + 1
            
        total += cnt
        
    return total - 1

def get_ans():
    return str(solve(10000000000000000))

if __name__ == "__main__":
    print(get_ans())
