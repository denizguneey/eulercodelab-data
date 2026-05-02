# Problem 173: Using up to one million tiles how many hollow square laminae can be formed?

def solve():
    limit = 1000000
    count = 0
    outer = 3
    while 4*outer - 4 <= limit:
        inner = outer - 2
        while inner > 0:
            tiles = outer*outer - inner*inner
            if tiles > limit: break
            count += 1
            inner -= 2
        outer += 1
    print(count)

solve()
