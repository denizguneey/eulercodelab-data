def solve():
    SEED = 290797; MOD = 50515093; TARGET = 10000000

    class Solver:
        def __init__(self):
            self.stack = []; self.rc = [0]
        def process_run(self, rl, occ):
            if rl <= 0: return
            if occ: self.stack.extend([0]*rl); return
            for _ in range(rl):
                if not self.stack: break
                cmr = self.stack.pop()
                rd = cmr + 1
                while len(self.rc) <= rd: self.rc.append(0)
                self.rc[rd] += 1
                if self.stack and self.stack[-1] < rd: self.stack[-1] = rd
        def finalize(self):
            while self.stack:
                cmr = self.stack.pop()
                rd = cmr + 1
                while len(self.rc) <= rd: self.rc.append(0)
                self.rc[rd] += 1
                if self.stack and self.stack[-1] < rd: self.stack[-1] = rd
        def sos(self):
            ans = 0
            for r in range(1, len(self.rc)):
                ans += (2*r-1)*self.rc[r]
            return ans

    sol = Solver()
    s = SEED; occ = True
    for _ in range(TARGET+1):
        rl = int(s % 64) + 1
        sol.process_run(rl, occ)
        occ = not occ
        s = (s*s) % MOD
    sol.finalize()
    return str(sol.sos())

if __name__ == '__main__':
    print(solve())
