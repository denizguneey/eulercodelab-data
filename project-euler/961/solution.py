class Solver:
    def __init__(self):
        self.memo = {}

    def W_pow10(self, exp):
        pow9 = [1] * 19
        for i in range(1, 19):
            pow9[i] = pow9[i - 1] * 9

        ans = 0
        for length in range(1, exp + 1):
            base = 1 << (length - 1)
            limit = 1 << (length - 1)
            for tail in range(limit):
                mask = base | tail
                if self.is_winning(mask, length):
                    ones = bin(mask).count('1')
                    ans += pow9[ones]
        return ans

    def is_winning(self, mask, length):
        if length == 0:
            return False
            
        state = (length, mask)
        if state in self.memo:
            return self.memo[state]

        for i in range(length):
            j = length - 1 - i
            high = mask >> (j + 1)
            low = mask & ((1 << j) - 1)
            next_mask = (high << j) | low
            next_len = length - 1
            
            while next_len > 0 and ((next_mask >> (next_len - 1)) & 1) == 0:
                next_len -= 1
                
            if not self.is_winning(next_mask, next_len):
                self.memo[state] = True
                return True
                
        self.memo[state] = False
        return False

def run_validations():
    solver = Solver()
    assert solver.W_pow10(2) == 18
    assert solver.W_pow10(4) == 1656

def solve():
    solver = Solver()
    return str(solver.W_pow10(18))

if __name__ == "__main__":
    run_validations()
    print(solve())
