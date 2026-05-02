def compute_B(n):
    kMod = 50515093
    st = []
    
    s = 290797
    pref_init = 0
    sum_pref_init = 0
    
    for _ in range(n):
        v = s
        pref_init += v
        sum_pref_init += pref_init
        
        s = (s * s) % kMod
        
        st.append([v, 1])
        while len(st) >= 2:
            right = st[-1]
            left = st[-2]
            left_max = (left[0] + left[1] - 1) // left[1]
            right_min = right[0] // right[1]
            if left_max <= right_min:
                break
            left[0] += right[0]
            left[1] += right[1]
            st.pop()
            
    pref_final = 0
    sum_pref_final = 0
    
    for b_sum, b_len in st:
        q = b_sum // b_len
        r = b_sum % b_len
        
        cnt_q = b_len - r
        if cnt_q > 0:
            sum_pref_final += cnt_q * pref_final
            sum_pref_final += q * cnt_q * (cnt_q + 1) // 2
            pref_final += cnt_q * q
            
        cnt_q1 = r
        if cnt_q1 > 0:
            qp1 = q + 1
            sum_pref_final += cnt_q1 * pref_final
            sum_pref_final += qp1 * cnt_q1 * (cnt_q1 + 1) // 2
            pref_final += cnt_q1 * qp1
            
    return sum_pref_init - sum_pref_final

def solve():
    ans = compute_B(10000000)
    return str(ans)

if __name__ == "__main__":
    print(solve())
