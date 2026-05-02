import decimal
decimal.getcontext().prec = 120

def solve():
    D = decimal.Decimal
    pi = D('3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706807')
    ln10 = D('2.30258509299404568401799145468436420760110148862877297603332790096757260967735248023599720508959829834')

    alpha = D('-2.0888430156130438559570867167749475005456937410367296732391125442446071101031945')
    beta = D('7.4614892856542545569061166121864153345090949932022092409344113914118766543223747')
    den = alpha*alpha + beta*beta
    n = 1000000; wanted = 8

    two_pi = 2*pi; raw = beta*D(n)
    theta = raw - (raw/two_pi).to_integral_value(rounding=decimal.ROUND_FLOOR)*two_pi
    # cos/sin via Taylor series
    def cos_d(x):
        s = D(1); t = D(1)
        for i in range(1, 80):
            t *= -x*x/D(2*i*(2*i-1)); s += t
        return s
    def sin_d(x):
        s = x; t = x
        for i in range(1, 80):
            t *= -x*x/D((2*i)*(2*i+1)); s += t
        return s
    c = cos_d(theta); s = sin_d(theta)
    envelope = 2*(c*alpha + s*beta)/den
    sign = D(1) if envelope >= 0 else D(-1)

    log10_eps = alpha*D(n)/ln10
    def log10_d(x):
        return x.ln()/ln10
    log10_eps += log10_d(abs(envelope))

    shift = int((-log10_eps).to_integral_value(rounding=decimal.ROUND_FLOOR))
    frac = -log10_eps - D(shift)
    # 10^(-frac)
    def pow10_d(x):
        return (x*ln10).exp()
    t = sign * pow10_d(-frac)

    base = D(2)/3 + t
    q = int(base.to_integral_value(rounding=decimal.ROUND_FLOOR))
    r = base - q
    if r < 0: r += 1

    tail = [6]*40
    carry = q
    for i in range(len(tail)-1, -1, -1):
        if carry == 0: break
        value = tail[i] + carry
        if value >= 0:
            tail[i] = value % 10; carry = value // 10
        else:
            borrow = (-value+9)//10
            tail[i] = value + 10*borrow; carry = -borrow

    out = ''
    for d in tail:
        if d != 6:
            out += str(d)
            if len(out) == wanted: return out

    # Extract from fractional part
    f = r
    while len(out) < wanted:
        f *= 10
        digit = int(f.to_integral_value(rounding=decimal.ROUND_FLOOR))
        digit = max(0, min(9, digit))
        f -= D(digit)
        if digit != 6: out += str(digit)

    return out[:wanted]

if __name__ == '__main__':
    print(solve())
