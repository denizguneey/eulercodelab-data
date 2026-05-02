A100 = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
B100 = "8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196"

def digit_at(A, B, n):
    lens = [0, len(A), len(B)]
    while lens[-1] < n:
        lens.append(lens[-2] + lens[-1])
        
    k = len(lens) - 1
    while k > 2:
        if n <= lens[k - 2]:
            k -= 2
        else:
            n -= lens[k - 2]
            k -= 1
            
    if k == 1:
        return int(A[n - 1])
    else:
        return int(B[n - 1])

def solve():
    answer = 0
    pow10 = 1
    
    for n in range(18):
        index = 127 + 19 * n
        for _ in range(n):
            index *= 7
            
        digit = digit_at(A100, B100, index)
        answer += pow10 * digit
        pow10 *= 10
        
    return str(answer)

if __name__ == '__main__':
    print(solve())
