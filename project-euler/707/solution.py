def solve():
    kMod = 1000000007
    kPhi = kMod - 1
    
    class Mat:
        def __init__(self, w):
            self.w = w
            self.words = (w + 63) // 64
            self.row = [[0] * self.words for _ in range(w)]
            
    def set_bit(r, c):
        r[c >> 6] |= (1 << (c & 63))
        
    def get_bit(r, c):
        return ((r[c >> 6] >> (c & 63)) & 1) != 0
        
    def identity(w):
        I = Mat(w)
        for i in range(w):
            set_bit(I.row[i], i)
        return I
        
    def zero_mat(w):
        return Mat(w)
        
    def build_H(w):
        H = Mat(w)
        for i in range(w):
            set_bit(H.row[i], i)
            if i > 0:
                set_bit(H.row[i], i - 1)
            if i + 1 < w:
                set_bit(H.row[i], i + 1)
        return H
        
    def add(A, B):
        C = Mat(A.w)
        for i in range(A.w):
            for k in range(A.words):
                C.row[i][k] = A.row[i][k] ^ B.row[i][k]
        return C
        
    def mul(A, B):
        C = Mat(A.w)
        for i in range(A.w):
            acc = [0] * A.words
            for wb in range(A.words):
                bits = A.row[i][wb]
                while bits != 0:
                    b = (bits & -bits).bit_length() - 1
                    col = (wb << 6) + b
                    if col < A.w:
                        brow = B.row[col]
                        for k in range(A.words):
                            acc[k] ^= brow[k]
                    bits &= bits - 1
            C.row[i] = acc
        return C
        
    def left_mul_H(P):
        R = Mat(P.w)
        for i in range(P.w):
            acc = list(P.row[i])
            if i > 0:
                pr = P.row[i - 1]
                for k in range(P.words):
                    acc[k] ^= pr[k]
            if i + 1 < P.w:
                nr = P.row[i + 1]
                for k in range(P.words):
                    acc[k] ^= nr[k]
            R.row[i] = acc
        return R
        
    def rank_gf2(A):
        r = 0
        for c in range(A.w):
            if r >= A.w: break
            piv = -1
            for i in range(r, A.w):
                if get_bit(A.row[i], c):
                    piv = i
                    break
            if piv == -1:
                continue
            if piv != r:
                A.row[piv], A.row[r] = A.row[r], A.row[piv]
            for i in range(r + 1, A.w):
                if get_bit(A.row[i], c):
                    rr = A.row[r]
                    ir = A.row[i]
                    for k in range(A.words):
                        ir[k] ^= rr[k]
            r += 1
        return r
        
    def mod_pow2(e):
        return pow(2, e, kMod)
        
    def S_value(w, n):
        H = build_H(w)
        A_prev = identity(w)
        B_prev = build_H(w)
        A_cur = identity(w)
        B_cur = build_H(w)
        
        fib_prev = 1
        fib_cur = 1
        
        def term_from_B(Bk, fib_k):
            Bk_copy = Mat(w)
            for i in range(w):
                Bk_copy.row[i] = list(Bk.row[i])
            rk = rank_gf2(Bk_copy)
            nullity = w - rk
            exp = ((w % kPhi) * (fib_k % kPhi)) % kPhi
            exp = (exp + kPhi - (nullity % kPhi)) % kPhi
            return mod_pow2(exp)
            
        total_sum = 0
        if n >= 1:
            total_sum = (total_sum + term_from_B(B_prev, fib_prev)) % kMod
        if n >= 2:
            total_sum = (total_sum + term_from_B(B_cur, fib_cur)) % kMod
            
        for k in range(3, n + 1):
            P = mul(A_cur, A_prev)
            Q = mul(A_cur, B_prev)
            R = mul(B_cur, A_prev)
            S = mul(B_cur, B_prev)
            HP = left_mul_H(P)
            
            A_next = add(add(Q, R), HP)
            B_next = add(S, P)
            
            fib_next = (fib_cur + fib_prev) % kPhi
            term = term_from_B(B_next, fib_next)
            total_sum = (total_sum + term) % kMod
            
            A_prev = A_cur
            B_prev = B_cur
            A_cur = A_next
            B_cur = B_next
            fib_prev = fib_cur
            fib_cur = fib_next
            
        return total_sum
        
    ans = S_value(199, 199)
    return str(ans)

if __name__ == "__main__":
    print(solve())
