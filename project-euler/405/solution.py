def mod_pow(base, exp, mod):
    return pow(base, exp, mod)

def solve():
    kMod = 410338673 # 17^7
    kPhi = 386201104 # phi(17^7)
    k = 1000000000000000000

    n_mod_phi = mod_pow(10, k, kPhi)

    inv3 = mod_pow(3, kPhi - 1, kMod)
    inv5 = mod_pow(5, kPhi - 1, kMod)
    inv15 = (inv3 * inv5) % kMod

    p2 = mod_pow(2, n_mod_phi, kMod)
    p4 = mod_pow(4, n_mod_phi, kMod)

    ans = 1
    ans = (ans - inv15) % kMod
    ans = (ans - 4 * p2 * inv3) % kMod
    ans = (ans + 2 * p4 * inv5) % kMod

    return str((ans + kMod) % kMod)

if __name__ == '__main__':
    print(solve())
