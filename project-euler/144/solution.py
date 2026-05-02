# Problem 144: Investigating multiple reflections of a laser beam
# Laser bounces inside ellipse 4x²+y²=100 until it exits through opening |x|<=0.01, y>0.

import math

def solve():
    # Ellipse: 4x²+y²=100
    px, py = 0.0, 10.1  # previous point (start)
    cx, cy = 1.4, -9.6  # current point (first hit)
    bounces = 0
    
    while True:
        # incoming direction
        dx, dy = cx - px, cy - py
        # normal to ellipse at (cx, cy): gradient of 4x²+y²-100 = (8x, 2y)
        nx, ny = 8*cx, 2*cy
        nlen = math.sqrt(nx*nx + ny*ny)
        nx, ny = nx/nlen, ny/nlen
        # reflect: d' = d - 2*(d·n)*n
        dot = dx*nx + dy*ny
        rdx = dx - 2*dot*nx
        rdy = dy - 2*dot*ny
        # find next intersection with 4x²+y²=100
        # parametric: (cx+t*rdx, cy+t*rdy) on ellipse
        # 4(cx+t*rdx)²+(cy+t*rdy)²=100
        a_coef = 4*rdx*rdx + rdy*rdy
        b_coef = 2*(4*cx*rdx + cy*rdy)
        # c_coef = 4*cx*cx + cy*cy - 100 = 0 (already on ellipse)
        t = -b_coef / a_coef
        nx2 = cx + t*rdx
        ny2 = cy + t*rdy
        bounces += 1
        px, py = cx, cy
        cx, cy = nx2, ny2
        if abs(cx) <= 0.01 and cy > 0:
            break
    
    print(bounces)

solve()
