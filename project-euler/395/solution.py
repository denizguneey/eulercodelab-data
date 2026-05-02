import heapq
import math

class Vec2:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

def norm(v):
    return math.sqrt(v.x * v.x + v.y * v.y)

def apply_transpose_mul(d, c):
    return Vec2(c.x * d.x + c.y * d.y, -c.y * d.x + c.x * d.y)

def dot(a, b):
    return a.x * b.x + a.y * b.y

def support_unit_square(d):
    return max(0.0, d.x, d.y, d.x + d.y)

class SupportSolver:
    def __init__(self):
        self.a = Vec2(16.0 / 25.0, 12.0 / 25.0)
        self.b = Vec2(9.0 / 25.0, -12.0 / 25.0)
        self.t1 = Vec2(0.0, 1.0)
        self.t2 = Vec2(16.0 / 25.0, 37.0 / 25.0)

    def support(self, direction, tol=1e-15):
        kRadialBound = 5.0
        best = support_unit_square(direction)
        
        pq = []
        heapq.heappush(pq, (-norm(direction) * kRadialBound, 0.0, direction.x, direction.y))
        
        while pq:
            neg_ub, offset, dx, dy = heapq.heappop(pq)
            ub = -neg_ub
            
            if ub <= best + tol:
                continue
                
            cur_dir = Vec2(dx, dy)
            best = max(best, offset + support_unit_square(cur_dir))
            
            dir1 = apply_transpose_mul(cur_dir, self.a)
            off1 = offset + dot(cur_dir, self.t1)
            ub1 = off1 + norm(dir1) * kRadialBound
            if ub1 > best + tol:
                heapq.heappush(pq, (-ub1, off1, dir1.x, dir1.y))
                
            dir2 = apply_transpose_mul(cur_dir, self.b)
            off2 = offset + dot(cur_dir, self.t2)
            ub2 = off2 + norm(dir2) * kRadialBound
            if ub2 > best + tol:
                heapq.heappush(pq, (-ub2, off2, dir2.x, dir2.y))
                
        return best

def solve():
    solver = SupportSolver()
    xmax = solver.support(Vec2(1.0, 0.0))
    xmin = -solver.support(Vec2(-1.0, 0.0))
    ymax = solver.support(Vec2(0.0, 1.0))
    ymin = -solver.support(Vec2(0.0, -1.0))
    
    ans = (xmax - xmin) * (ymax - ymin)
    return "{:.10f}".format(ans)

if __name__ == '__main__':
    print(solve())
