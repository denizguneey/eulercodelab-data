kOutMod = 1000000007

def solve(q):
    half = (q - 1) // 2
    is_residue = bytearray(q)
    r = 1
    for x in range(1, half + 1):
        is_residue[r] = 1
        r += 2 * x + 1
        if r >= q:
            r -= q
            
    pow2 = 1
    sum_nonres = 0
    signed_sum = 0
    
    for n in range(1, q):
        pow2 = (pow2 * 2) % kOutMod
        if is_residue[n]:
            signed_sum += pow2
            if signed_sum >= kOutMod:
                signed_sum -= kOutMod
        else:
            if signed_sum >= pow2:
                signed_sum -= pow2
            else:
                signed_sum += kOutMod - pow2
            sum_nonres += pow2
            if sum_nonres >= kOutMod:
                sum_nonres -= kOutMod
                
    if (q & 7) == 1:
        return (1 + 2 * sum_nonres) % kOutMod
    return signed_sum

if __name__ == "__main__":
    assert solve(5) == 6
    assert solve(17) == 47569
    print(solve(74207281))
