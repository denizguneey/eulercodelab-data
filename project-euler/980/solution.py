MOD = 888888883
MUL = 8888
A0  = 88888888

def compute_F(N):
    cnt = [[0] * 2 for _ in range(8)]
    
    a = A0
    
    for _ in range(N):
        px, py, pz = 0, 0, 0
        inv = 0
        
        for _ in range(50):
            b = a % 3
            if b == 0:
                inv ^= (py ^ pz)
                px ^= 1
            elif b == 1:
                inv ^= pz
                py ^= 1
            else:
                pz ^= 1
                
            a = (a * MUL) % MOD
            
        mask = (px << 2) | (py << 1) | pz
        cnt[mask][inv] += 1
        
    total = 0
    for mask in range(8):
        c0 = cnt[mask][0]
        c1 = cnt[mask][1]
        if mask == 0:
            total += c0 * c0 + c1 * c1
        else:
            total += 2 * c0 * c1
            
    return total

def run_checkpoints():
    assert compute_F(10) == 13
    assert compute_F(100) == 1224

def solve():
    return str(compute_F(1000000))

if __name__ == "__main__":
    run_checkpoints()
    print(solve())
