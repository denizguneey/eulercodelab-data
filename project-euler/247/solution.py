import math
import heapq

def largest_side(x, y):
    # Solve y + t = 1/(x + t) for t > 0
    return (math.sqrt((x - y)**2 + 4.0) - (x + y)) / 2.0

def binom(n, k):
    if k < 0 or k > n: return 0
    if k == 0 or k == n: return 1
    numer = 1
    denom = 1
    kk = min(k, n - k)
    for i in range(1, kk + 1):
        numer *= (n - kk + i)
        denom *= i
    return numer // denom

class Node:
    def __init__(self, left, below, x, y, side):
        self.left = left
        self.below = below
        self.x = x
        self.y = y
        self.side = side
        
    def __lt__(self, other):
        # We want a max-heap based on side, so return True if self.side > other.side
        return self.side > other.side

def solve(target_left=3, target_below=3):
    target_occurrences = binom(target_left + target_below, target_left)
    
    pq = []
    
    root_x = 1.0
    root_y = 0.0
    root_side = largest_side(root_x, root_y)
    root = Node(0, 0, root_x, root_y, root_side)
    
    heapq.heappush(pq, root)
    
    index = 0
    seen = 0
    answer = 0
    
    while seen < target_occurrences:
        cur = heapq.heappop(pq)
        index += 1
        
        if cur.left == target_left and cur.below == target_below:
            seen += 1
            answer = index
            
        right_x = cur.x + cur.side
        right_y = cur.y
        right_side = largest_side(right_x, right_y)
        right = Node(cur.left + 1, cur.below, right_x, right_y, right_side)
        heapq.heappush(pq, right)
        
        up_x = cur.x
        up_y = cur.y + cur.side
        up_side = largest_side(up_x, up_y)
        up = Node(cur.left, cur.below + 1, up_x, up_y, up_side)
        heapq.heappush(pq, up)
        
    return str(answer)

if __name__ == '__main__':
    print(solve())
