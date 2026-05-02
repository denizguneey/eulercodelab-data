class DigitPrimeDP:
    def __init__(self):
        self.kMaxLen = 20
        self.kMaxSum = 9 * self.kMaxLen
        self.is_prime = [True] * (self.kMaxSum + 1)
        self.ways = [[0] * (self.kMaxSum + 1) for _ in range(self.kMaxLen + 1)]
        self.good = [[0] * (self.kMaxSum + 1) for _ in range(self.kMaxLen + 1)]
        
        self.sieve_primes()
        self.build_ways()
        self.build_good()
        
    def sieve_primes(self):
        self.is_prime[0] = False
        self.is_prime[1] = False
        for p in range(2, int(self.kMaxSum**0.5) + 1):
            if self.is_prime[p]:
                for x in range(p * p, self.kMaxSum + 1, p):
                    self.is_prime[x] = False
                    
    def build_ways(self):
        self.ways[0][0] = 1
        for length in range(1, self.kMaxLen + 1):
            for s in range(9 * (length - 1) + 1):
                cur = self.ways[length - 1][s]
                if cur == 0: continue
                for d in range(10):
                    self.ways[length][s + d] += cur
                    
    def build_good(self):
        for rem in range(self.kMaxLen + 1):
            for pref in range(self.kMaxSum + 1):
                cnt = 0
                for tail in range(9 * rem + 1):
                    if pref + tail <= self.kMaxSum and self.is_prime[pref + tail]:
                        cnt += self.ways[rem][tail]
                self.good[rem][pref] = cnt
                
    def count_upto(self, x):
        s = str(x)
        ans = 0
        total_sum = 0
        for i, char in enumerate(s):
            d = int(char)
            rem = len(s) - i - 1
            for dig in range(d):
                ans += self.good[rem][total_sum + dig]
            total_sum += d
            
        if self.is_prime[total_sum]:
            ans += 1
        return ans

def nth_value(n, dp):
    lo = 1
    hi = 1
    while dp.count_upto(hi) < n:
        hi <<= 1
        
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if dp.count_upto(mid) >= n:
            hi = mid
        else:
            lo = mid + 1
    return lo

def solve():
    dp = DigitPrimeDP()
    ans = nth_value(10000000000000000, dp)
    return str(ans)

if __name__ == "__main__":
    print(solve())
