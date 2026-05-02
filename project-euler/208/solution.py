# Problem 208: Robot Walks
# Robot makes 70 steps, each 1/5 of a circle, clockwise or anticlockwise.
# Count paths that return to start.

def solve():
    steps = 70
    # State = tuple of 5 values tracking cumulative position in each direction
    # Transitions: clockwise rotates state and decrements, anticlockwise rotates and increments
    current = {(0,0,0,0,0): 1}
    for _ in range(steps):
        nxt = {}
        for state, count in current.items():
            s = state
            # Clockwise: new_state = (s[2], s[3], s[4], -s[0], -s[1]-1)
            cw = (s[2], s[3], s[4], -s[0], -s[1]-1)
            nxt[cw] = nxt.get(cw, 0) + count
            # Anticlockwise: new_state = (-s[3], -s[4]+1, s[0], s[1], s[2])
            acw = (-s[3], -s[4]+1, s[0], s[1], s[2])
            nxt[acw] = nxt.get(acw, 0) + count
        current = nxt

    # is_closed: s[1]+s[4]==0 and s[2]+s[3]==0 and s[1]+s[2]==0 and s[0]+s[1]==0
    ans = 0
    for s, cnt in current.items():
        if s[1]+s[4]==0 and s[2]+s[3]==0 and s[1]+s[2]==0 and s[0]+s[1]==0:
            ans += cnt
    print(ans)

solve()
