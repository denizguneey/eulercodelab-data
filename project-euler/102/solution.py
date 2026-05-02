# Problem 102: Triangle containment
# How many triangles in the file contain the origin?

import os

def solve():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, '..', 'resources', 'documents', '0102_triangles.txt')
    
    def contains_origin(x1, y1, x2, y2, x3, y3):
        # Cross product method
        d1 = x1 * (y2 - y3) - y1 * (x2 - x3) + (x2 * y3 - x3 * y2)
        d2 = 0  # sub-triangles with origin
        # Check using sign of cross products
        def sign(x):
            return (x > 0) - (x < 0)
        def cross(ax, ay, bx, by):
            return ax * by - ay * bx
        
        c1 = cross(x1, y1, x2, y2)
        c2 = cross(x2, y2, x3, y3)
        c3 = cross(x3, y3, x1, y1)
        
        has_neg = (c1 < 0) or (c2 < 0) or (c3 < 0)
        has_pos = (c1 > 0) or (c2 > 0) or (c3 > 0)
        return not (has_neg and has_pos)
    
    with open(file_path) as f:
        lines = f.readlines()
    
    count = 0
    for line in lines:
        coords = list(map(int, line.strip().split(',')))
        if contains_origin(*coords):
            count += 1
    print(count)

solve()
