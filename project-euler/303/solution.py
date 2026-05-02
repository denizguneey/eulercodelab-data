from collections import deque

def solve():
    limit = 10000

    def smallest_multiple_012(n):
        if n == 1:
            return 1
        seen = bytearray(n)
        parent = [-1] * n
        parent_digit = [-1] * n
        q = deque()
        for d in range(1, 3):
            r = d % n
            if not seen[r]:
                seen[r] = 1
                parent[r] = -2
                parent_digit[r] = d
                q.append(r)

        end_rem = -1
        while q:
            rem = q.popleft()
            if rem == 0:
                end_rem = rem
                break
            for d in range(3):
                nxt = (rem * 10 + d) % n
                if not seen[nxt]:
                    seen[nxt] = 1
                    parent[nxt] = rem
                    parent_digit[nxt] = d
                    q.append(nxt)

        digits = []
        cur = end_rem
        while cur >= 0:
            digits.append(parent_digit[cur])
            cur = parent[cur]
        digits.reverse()
        val = 0
        for d in digits:
            val = val * 10 + d
        return val

    total = 0
    for n in range(1, limit + 1):
        m = smallest_multiple_012(n)
        total += m // n

    return str(total)

if __name__ == '__main__':
    print(solve())
