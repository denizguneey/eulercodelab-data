def tri(n):
    return n * (n + 1) // 2

def sum_range(a, b):
    if b < a: return 0
    return (a + b) * (b - a + 1) // 2

class Precomputed:
    def __init__(self, max_n):
        self.fib = [1, 1, 2]
        while self.fib[-1] <= max_n:
            self.fib.append(self.fib[-1] + self.fib[-2])
            
        kmax = len(self.fib) - 2
        
        self.prefix_len = [0] * len(self.fib)
        self.tail_sum = [0] * len(self.fib)
        self.interval_sum = [0] * len(self.fib)
        self.interval_prefix_sum = [0] * len(self.fib)
        
        self.prefix_len[1] = 1
        self.prefix_len[2] = 1
        self.prefix_len[3] = 2
        self.prefix_len[4] = 3
        if len(self.prefix_len) > 5:
            self.prefix_len[5] = 4
            
        for k in range(6, kmax + 1):
            self.prefix_len[k] = self.fib[k - 2] + self.prefix_len[k - 3]
            
        if len(self.tail_sum) > 5: self.tail_sum[5] = 1
        if len(self.tail_sum) > 6: self.tail_sum[6] = 2
        for k in range(7, kmax + 1):
            a = self.prefix_len[k - 3]
            b = self.prefix_len[k - 2] - 1
            self.tail_sum[k] = self.tail_sum[k - 2] + sum_range(a, b)
            
        self.interval_sum[1] = 0
        self.interval_sum[2] = 0
        for k in range(3, kmax + 1):
            p = self.prefix_len[k]
            self.interval_sum[k] = tri(p - 1) + self.tail_sum[k]
            
        for k in range(1, kmax + 1):
            self.interval_prefix_sum[k] = self.interval_prefix_sum[k - 1] + self.interval_sum[k]

def prefix_tail(data, k, j):
    if j < 0: return 0
    if k <= 4: return 0
    if k == 5: return 1
    if k == 6: return 2
    
    start = data.prefix_len[k - 3]
    end = data.prefix_len[k - 2] - 1
    block_len = end - start + 1
    
    if j < block_len:
        return sum_range(start, start + j)
    return sum_range(start, end) + prefix_tail(data, k - 2, j - block_len)

def prefix_interval(data, k, idx):
    interval_len = data.fib[k - 1]
    if idx >= interval_len - 1:
        return data.interval_sum[k]
    if k <= 2: return 0
    
    p = data.prefix_len[k]
    if idx < p:
        return tri(idx)
        
    tail_idx = idx - p
    return tri(p - 1) + prefix_tail(data, k, tail_idx)

def fast_sum_M(n, data):
    if n == 0: return 0
    k = 1
    while k + 1 < len(data.fib) and data.fib[k + 1] <= n:
        k += 1
        
    full_before = data.interval_prefix_sum[k - 1]
    idx = n - data.fib[k]
    return full_before + prefix_interval(data, k, idx)

def solve():
    kLimit = 1000000000000000000
    kMod = 100000000
    data = Precomputed(kLimit)
    total = fast_sum_M(kLimit, data)
    ans = total % kMod
    return str(ans)

if __name__ == '__main__':
    print(solve())
