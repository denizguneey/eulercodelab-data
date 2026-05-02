import math
import heapq

kMod = 1234567891

class Node:
    def __init__(self, logv, modv, id):
        self.logv = logv
        self.modv = modv
        self.id = id
        
    def __lt__(self, other):
        if self.logv != other.logv:
            return self.logv < other.logv
        return self.id < other.id

def S(n, m):
    len_n = n - 1
    pq = []
    max_log = 0.0
    
    for i in range(len_n):
        v = i + 2
        logv = math.log(v)
        node = Node(logv, v % kMod, i)
        heapq.heappush(pq, node)
        if logv > max_log:
            max_log = logv
            
    steps = 0
    while steps < m:
        x = pq[0]
        if 2.0 * x.logv > max_log:
            break
        heapq.heappop(pq)
        x.logv *= 2.0
        x.modv = (x.modv * x.modv) % kMod
        heapq.heappush(pq, x)
        if x.logv > max_log:
            max_log = x.logv
        steps += 1
        
    if steps == m:
        ans = 0
        for x in pq:
            ans = (ans + x.modv) % kMod
        return ans
        
    arr = list(pq)
    arr.sort(key=lambda x: (x.logv, x.id))
    
    rem = m - steps
    q = rem // len_n
    r = rem % len_n
    
    exp_q = pow(2, q, kMod - 1)
    exp_q1 = (exp_q * 2) % (kMod - 1)
    
    ans = 0
    for i in range(len_n):
        e = exp_q1 if i < r else exp_q
        add = pow(arr[i].modv, e, kMod)
        ans = (ans + add) % kMod
        
    return ans

def solve():
    ans = S(10000, 10000000000000000)
    return str(ans)

if __name__ == "__main__":
    print(solve())
