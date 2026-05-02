def mod14(v):
    return v % 14

def to_base14(value):
    digits = "0123456789abcd"
    if value == 0:
        return "0"
    out = []
    while value > 0:
        out.append(digits[value % 14])
        value //= 14
    return "".join(reversed(out))

class SequenceState:
    def __init__(self, root):
        self.x = root
        self.mod = 14
        self.f = (self.x * self.x - self.x) // 14
        self.leading_digit = root
        self.digit_sum = root

    def step(self, inv_mod14):
        x_old = self.x
        mod_old = self.mod
        
        a = mod14(2 * x_old - 1)
        inv = inv_mod14[a]
        f_mod = mod14(self.f)
        t = ((14 - f_mod) % 14 * inv) % 14
        
        self.x = x_old + t * mod_old
        self.f = (self.f + (2 * x_old - 1) * t + t * t * mod_old) // 14
        self.mod = mod_old * 14
        
        self.leading_digit = t
        self.digit_sum += t

def solve_sum_of_digit_sums(n_max):
    inv_mod14 = [-1] * 14
    for a in range(1, 14):
        for b in range(1, 14):
            if (a * b) % 14 == 1:
                inv_mod14[a] = b
                break
                
    seq7 = SequenceState(7)
    seq8 = SequenceState(8)
    
    total = 1
    
    for n in range(1, n_max + 1):
        if seq7.leading_digit != 0:
            total += seq7.digit_sum
        if seq8.leading_digit != 0:
            total += seq8.digit_sum
            
        if n == n_max:
            break
            
        seq7.step(inv_mod14)
        seq8.step(inv_mod14)
        
    return total

def solve():
    ans = solve_sum_of_digit_sums(10000)
    return to_base14(ans)

if __name__ == '__main__':
    print(solve())
