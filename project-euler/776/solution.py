import decimal

def f_of_u64(N):
    decimal.getcontext().prec = 100
    s = str(N)
    L = len(s)
    max_sum = 9 * L
    
    tight = [{'count': 0, 'sum': 0} for _ in range(max_sum + 1)]
    loose = [{'count': 0, 'sum': 0} for _ in range(max_sum + 1)]
    
    tight[0]['count'] = 1
    
    for pos in range(L):
        limit = int(s[pos])
        ntight = [{'count': 0, 'sum': 0} for _ in range(max_sum + 1)]
        nloose = [{'count': 0, 'sum': 0} for _ in range(max_sum + 1)]
        
        for sum_val in range(max_sum + 1):
            t_cnt = tight[sum_val]['count']
            t_sum = tight[sum_val]['sum']
            if t_cnt != 0:
                for d in range(limit + 1):
                    ns = sum_val + d
                    if d == limit:
                        ntight[ns]['count'] += t_cnt
                        ntight[ns]['sum'] += t_sum * 10 + t_cnt * d
                    else:
                        nloose[ns]['count'] += t_cnt
                        nloose[ns]['sum'] += t_sum * 10 + t_cnt * d
                        
            l_cnt = loose[sum_val]['count']
            l_sum = loose[sum_val]['sum']
            if l_cnt != 0:
                for d in range(10):
                    ns = sum_val + d
                    nloose[ns]['count'] += l_cnt
                    nloose[ns]['sum'] += l_sum * 10 + l_cnt * d
                    
        tight = ntight
        loose = nloose
        
    ans = decimal.Decimal(0)
    for sum_val in range(1, max_sum + 1):
        total_sum = tight[sum_val]['sum'] + loose[sum_val]['sum']
        if total_sum == 0:
            continue
        ans += decimal.Decimal(total_sum) / decimal.Decimal(sum_val)
        
    # Return formatted as e.g. 4.855801996238e+06
    # Note that scientific format with 12 decimals exactly matches C++'s setprecision(12)
    s_val = f"{ans:.12e}"
    # Replace e+06 with e+06 so it looks natural, python does e+06, C++ does e+06 or e+006
    return s_val

def solve():
    return f_of_u64(1234567890123456789)

if __name__ == "__main__":
    print(solve())
