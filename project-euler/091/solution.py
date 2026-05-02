# Problem 91: Right triangles with integer coordinates
# How many right triangles with integer coordinates can be formed with
# O(0,0), P and Q in the grid 0<=x,y<=50?

def solve():
    n = 50
    count = 0
    for x1 in range(n+1):
        for y1 in range(n+1):
            if x1 == 0 and y1 == 0: continue
            for x2 in range(n+1):
                for y2 in range(n+1):
                    if x2 == 0 and y2 == 0: continue
                    if (x1, y1) >= (x2, y2): continue
                    dot_o = x1*x2 + y1*y2
                    dot_p = x1*(x1-x2) + y1*(y1-y2)
                    dot_q = x2*(x2-x1) + y2*(y2-y1)
                    if dot_o == 0 or dot_p == 0 or dot_q == 0:
                        count += 1
    print(count)

solve()
