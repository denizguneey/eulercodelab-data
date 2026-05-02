# Problem 184: Triangles containing the origin in a circle of radius 105.
import math

def solve():
    R = 105
    EPS = 1e-8
    PI = math.pi
    angles = []
    for x in range(-R, R+1):
        for y in range(-R, R+1):
            if (x==0 and y==0) or x*x+y*y >= R*R: continue
            angles.append(math.atan2(y, x))
    angles.sort()
    n = len(angles)
    # Duplicate for circular handling
    angles2 = angles + [a + 2*PI for a in angles]
    # Count triangles containing origin
    ans = n*(n-1)*(n-2)//6
    half = n // 2
    # Subtract collinear/half-plane cases
    i = 0
    while i < half:
        cnt = 1
        while i+cnt < half and angles[i+cnt] - angles[i] <= EPS:
            cnt += 1
        ans -= (half-cnt)*(half-cnt-1)*cnt
        ans -= cnt*cnt*(n-2*cnt) + cnt*(cnt-1)*(half-cnt)
        doubled = 2*cnt
        ans -= doubled*(doubled-1)*(doubled-2)//6
        i += cnt
    print(ans)

solve()
