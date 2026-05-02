# Problem 174: Counting the number of "hollow" square laminae that can form one, two, ... distinct arrangements.

def solve():
    limit = 1000000
    max_type = 10
    count = [0]*(limit+1)
    outer = 3
    while 4*outer - 4 <= limit:
        inner = outer - 2
        while inner > 0:
            tiles = outer*outer - inner*inner
            if tiles > limit: break
            count[tiles] += 1
            inner -= 2
        outer += 1
    ans = sum(1 for n in range(1, limit+1) if 1 <= count[n] <= max_type)
    print(ans)

solve()
