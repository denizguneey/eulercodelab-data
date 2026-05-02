import sys

class PatternEngine:
    def __init__(self, pattern):
        self.pattern = pattern
        self.L = len(pattern)
        self.next_state = [[0] * 10 for _ in range(self.L + 1)]
        self.out = [[0] * 10 for _ in range(self.L + 1)]
        self.build_automaton()
        
        self.ops = []
        self.op_to_id = {}
        
        self.id_identity = -1
        self.digit_op_id = [0] * 10
        self.build_digit_operators()
        
        self.compose_cache = {}
        self.append_cache = {}
        self.full_block_cache = {}
        
        self.pow10 = [1] * 21
        for i in range(1, 21):
            self.pow10[i] = self.pow10[i - 1] * 10

    def build_automaton(self):
        pi = [0] * self.L
        for i in range(1, self.L):
            j = pi[i - 1]
            while j > 0 and self.pattern[i] != self.pattern[j]:
                j = pi[j - 1]
            if self.pattern[i] == self.pattern[j]:
                j += 1
            pi[i] = j
            
        for st in range(self.L + 1):
            for d in range(10):
                c = str(d)
                j = st
                while j > 0 and (j == self.L or self.pattern[j] != c):
                    j = pi[j - 1]
                if j < self.L and self.pattern[j] == c:
                    j += 1
                if j == self.L:
                    self.out[st][d] = 1
                    j = pi[self.L - 1]
                self.next_state[st][d] = j

    def intern_op(self, end_state, add_count):
        key = (tuple(end_state), tuple(add_count))
        if key in self.op_to_id:
            return self.op_to_id[key]
        op_id = len(self.ops)
        self.ops.append((end_state, add_count))
        self.op_to_id[key] = op_id
        return op_id

    def build_digit_operators(self):
        end_state = list(range(self.L + 1))
        add_count = [0] * (self.L + 1)
        self.id_identity = self.intern_op(end_state, add_count)
        
        for d in range(10):
            es = [0] * (self.L + 1)
            ac = [0] * (self.L + 1)
            for s in range(self.L + 1):
                es[s] = self.next_state[s][d]
                ac[s] = self.out[s][d]
            self.digit_op_id[d] = self.intern_op(es, ac)

    def compose_ids(self, id_a, id_b):
        key = (id_a, id_b)
        if key in self.compose_cache:
            return self.compose_cache[key]
            
        A_es, A_ac = self.ops[id_a]
        B_es, B_ac = self.ops[id_b]
        
        C_es = [0] * (self.L + 1)
        C_ac = [0] * (self.L + 1)
        for s in range(self.L + 1):
            mid = A_es[s]
            C_es[s] = B_es[mid]
            C_ac[s] = A_ac[s] + B_ac[mid]
            
        res = self.intern_op(C_es, C_ac)
        self.compose_cache[key] = res
        return res

    def append_digit(self, op_id, d):
        key = (op_id, d)
        if key in self.append_cache:
            return self.append_cache[key]
        res = self.compose_ids(op_id, self.digit_op_id[d])
        self.append_cache[key] = res
        return res

    def full_block(self, prefix_op, rem_digits):
        key = (prefix_op, rem_digits)
        if key in self.full_block_cache:
            return self.full_block_cache[key]
            
        if rem_digits == 0:
            res = prefix_op
        else:
            res = self.id_identity
            for d in range(10):
                child = self.full_block(self.append_digit(prefix_op, d), rem_digits - 1)
                res = self.compose_ids(res, child)
                
        self.full_block_cache[key] = res
        return res

    def partial_block(self, prefix_op, rem_digits, upper_suffix):
        if rem_digits == 0:
            return prefix_op
            
        base = self.pow10[rem_digits - 1]
        first = int(upper_suffix // base)
        rest = int(upper_suffix % base)
        
        res = self.id_identity
        for d in range(first):
            child = self.full_block(self.append_digit(prefix_op, d), rem_digits - 1)
            res = self.compose_ids(res, child)
            
        last = self.partial_block(self.append_digit(prefix_op, first), rem_digits - 1, rest)
        res = self.compose_ids(res, last)
        return res

    def range_operator(self, N):
        if N == 0:
            return self.id_identity
            
        s = str(N)
        D = len(s)
        res = self.id_identity
        
        for d in range(1, D):
            rem = d - 1
            for a in range(1, 10):
                block = self.full_block(self.digit_op_id[a], rem)
                res = self.compose_ids(res, block)
                
        first = int(s[0])
        rem = D - 1
        for a in range(1, first):
            block = self.full_block(self.digit_op_id[a], rem)
            res = self.compose_ids(res, block)
            
        if rem == 0:
            res = self.compose_ids(res, self.digit_op_id[first])
        else:
            suffix = int(s[1:])
            part = self.partial_block(self.digit_op_id[first], rem, suffix)
            res = self.compose_ids(res, part)
            
        return res

    def occ_and_state(self, N):
        op_id = self.range_operator(N)
        es, ac = self.ops[op_id]
        return ac[0], es[0]

    def digits_before(self, N):
        if N == 0:
            return 0
            
        s = str(N)
        D = len(s)
        total = 0
        for d in range(1, D):
            total += 9 * self.pow10[d - 1] * d
            
        total += (N - self.pow10[D - 1] + 1) * D
        return total

    def nth_occurrence_position(self, target_occurrence):
        hi = 1
        while self.occ_and_state(hi)[0] < target_occurrence:
            hi *= 2
            
        lo = 1
        while lo < hi:
            mid = (lo + hi) // 2
            if self.occ_and_state(mid)[0] >= target_occurrence:
                hi = mid
            else:
                lo = mid + 1
                
        number = lo
        before_count, before_state = self.occ_and_state(number - 1)
        need_inside = target_occurrence - before_count
        
        prefix_digits = self.digits_before(number - 1)
        found_inside = 0
        state = before_state
        
        num_str = str(number)
        for i, ch in enumerate(num_str):
            d = int(ch)
            if self.out[state][d]:
                found_inside += 1
                if found_inside == need_inside:
                    end_pos = prefix_digits + i + 1
                    return end_pos - self.L + 1
            state = self.next_state[state][d]
            
        return 0

def solve(k_max=13):
    total = 0
    n = 1
    for k in range(1, k_max + 1):
        n *= 3
        engine = PatternEngine(str(n))
        total += engine.nth_occurrence_position(n)
        
    return str(total)

if __name__ == '__main__':
    print(solve())
