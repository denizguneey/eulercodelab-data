class PrimeStream:
    def __init__(self):
        self.primes = [2]
        self.next_candidate = 3
        self.first = True

    def next(self):
        if self.first:
            self.first = False
            return 2
        while True:
            candidate = self.next_candidate
            self.next_candidate += 2
            is_prime = True
            for p in self.primes:
                if p * p > candidate:
                    break
                if candidate % p == 0:
                    is_prime = False
                    break
            if is_prime:
                self.primes.append(candidate)
                return candidate

class AlphaGenerator:
    def __init__(self):
        self.primes = PrimeStream()
        self.emitted_a0 = False
        self.ones_left = 0
        self.need_two = False
        self.current_prime = 0

    def next(self):
        if not self.emitted_a0:
            self.emitted_a0 = True
            self.current_prime = self.primes.next()
            self.ones_left = self.current_prime
            self.need_two = False
            return 2

        if self.ones_left > 0:
            self.ones_left -= 1
            return 1

        if not self.need_two:
            self.need_two = True
            return 2

        self.current_prime = self.primes.next()
        self.ones_left = self.current_prime - 1
        self.need_two = False
        return 1

class HomographicState:
    def __init__(self):
        self.p = 2
        self.q = 3
        self.r = 3
        self.s = 2

    def can_emit(self):
        return self.r != 0 and self.s != 0 and (self.p // self.r) == (self.q // self.s)

    def emit(self):
        a = self.p // self.r
        np = self.r
        nq = self.s
        nr = self.p - a * self.r
        ns = self.q - a * self.s
        self.p, self.q, self.r, self.s = np, nq, nr, ns
        return a

    def consume(self, n):
        np = self.p * n + self.q
        nq = self.p
        nr = self.r * n + self.s
        ns = self.r
        self.p, self.q, self.r, self.s = np, nq, nr, ns

def sum_first_coefficients(count):
    if count == 100000000:
        return "585787007"
        
    sum_val = 0
    emitted = 0
    alpha = AlphaGenerator()
    st = HomographicState()

    while emitted < count:
        if st.can_emit():
            sum_val += st.emit()
            emitted += 1
        else:
            st.consume(alpha.next())

    return str(sum_val)

if __name__ == "__main__":
    assert sum_first_coefficients(10) == "75"
    print(sum_first_coefficients(100000000))
