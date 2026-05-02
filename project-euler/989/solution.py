from __future__ import annotations

import math
import multiprocessing as mp
import sys
from array import array


MOD = 1_000_000_009
TARGET_LIMIT = 100_000_000_000_000
SAMPLE_LIMIT = 1_000
SAMPLE_SUM = 190_950_976

SQRT5_MOD = 383_008_016
PHI_MOD = 691_504_013
PSI_MOD = 308_495_997


class Options:
    __slots__ = ("allow_multiprocessing", "requested_processes")

    def __init__(self):
        self.allow_multiprocessing = True
        self.requested_processes = 0


_WORK_LIMIT = 0
_WORK_MU = None
_WORK_PHI_SQ = None
_WORK_PHI_INV_SQ = None


def mod_mul(a, b):
    return (a * b) % MOD


def mod_add(a, b):
    s = a + b
    return s - MOD if s >= MOD else s


def mod_sub(a, b):
    return a - b if a >= b else a + MOD - b


def mod_neg(a):
    return 0 if a == 0 else MOD - a


def mod_pow(base, exp):
    return pow(base, exp, MOD)


def normalize_signed_mod(value):
    return value % MOD


def sieve_primes(limit):
    if limit < 2:
        return []
    is_prime = bytearray(b"\x01") * (limit + 1)
    is_prime[0] = 0
    is_prime[1] = 0
    primes = []
    for i in range(2, limit + 1):
        if not is_prime[i]:
            continue
        primes.append(i)
        if i > limit // i:
            continue
        step = i
        start = i * i
        is_prime[start : limit + 1 : step] = b"\x00" * (((limit - start) // step) + 1)
    return primes


def mobius_sieve(limit):
    mu = array("b", [0]) * (limit + 1)
    least = array("I", [0]) * (limit + 1)
    primes = []
    mu[1] = 1

    for i in range(2, limit + 1):
        if least[i] == 0:
            least[i] = i
            primes.append(i)
            mu[i] = -1
        li = least[i]
        mui = mu[i]
        for p in primes:
            ip = i * p
            if ip > limit or p > li:
                break
            least[ip] = p
            if p == li:
                mu[ip] = 0
                break
            mu[ip] = -mui

    return mu


def g_bruteforce(n):
    count = 0
    for x in range(n):
        if (x * x + n - x - 1) % n == 0:
            count += 1
    return count


def g_from_factorization(n, primes):
    if n == 1:
        return 1

    result = 1
    for p in primes:
        if p > n // p:
            break
        if n % p != 0:
            continue

        exponent = 0
        while n % p == 0:
            n //= p
            exponent += 1

        if p == 2:
            return 0
        if p == 5:
            if exponent >= 2:
                return 0
            continue

        r = p % 5
        if r == 1 or r == 4:
            result *= 2
        elif r == 2 or r == 3:
            return 0
        else:
            raise RuntimeError("unreachable")

    if n > 1:
        if n == 2:
            return 0
        if n == 5:
            return result
        r = n % 5
        if r == 1 or r == 4:
            result *= 2
        elif r == 2 or r == 3:
            return 0
        else:
            raise RuntimeError("unreachable")

    return result


def q_form(a, b):
    return a * a - a * b - b * b


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def reduced_pair_count(n):
    count = 0
    max_b = math.isqrt(n)
    for b in range(1, max_b + 1):
        a = 2 * b
        while True:
            q = q_form(a, b)
            if q > n:
                break
            if q == n and gcd(a, b) == 1:
                count += 1
            a += 1
    return count


def direct_pair_sum(limit, base):
    acc = 0
    max_b = math.isqrt(limit)
    for b in range(1, max_b + 1):
        a = 2 * b
        while True:
            q = q_form(a, b)
            if q > limit:
                break
            if gcd(a, b) == 1:
                acc = mod_add(acc, mod_pow(base, q))
            a += 1
    return acc


class PowerSeq:
    __slots__ = ("v", "term", "delta", "delta_step")

    def __init__(self, v, term, delta, delta_step):
        self.v = v
        self.term = term
        self.delta = delta
        self.delta_step = delta_step

    @staticmethod
    def square(base):
        base_sq = mod_mul(base, base)
        return PowerSeq(0, 1, base, base_sq)

    @staticmethod
    def triangular(base):
        base_sq = mod_mul(base, base)
        return PowerSeq(0, 1, base_sq, base_sq)

    def step(self):
        self.term = mod_mul(self.term, self.delta)
        self.delta = mod_mul(self.delta, self.delta_step)
        self.v += 1

    def extend_through(self, target, window):
        while self.v <= target:
            window += self.term
            if window >= MOD:
                window -= MOD
            self.step()
        return window

    def trim_before(self, target, window):
        while self.v < target:
            window -= self.term
            if window < 0:
                window += MOD
            self.step()
        return window


def nonprimitive_sum(limit, w, winv):
    if limit == 0:
        return 0

    sqrt_limit = math.isqrt(limit)
    winv5 = mod_pow(winv, 5)
    winv10 = mod_mul(winv5, winv5)
    ans = 0

    even_t_max = sqrt_limit // 2
    if even_t_max > 0:
        add_seq = PowerSeq.square(w)
        trim_seq = PowerSeq.square(w)
        window = 0
        factor = 1
        ratio = winv5

        for t in range(1, even_t_max + 1):
            factor = mod_mul(factor, ratio)
            ratio = mod_mul(ratio, winv10)

            vmax = math.isqrt(limit + 5 * t * t)
            window = add_seq.extend_through(vmax, window)
            window = trim_seq.trim_before(3 * t, window)
            ans = mod_add(ans, mod_mul(factor, window))

    odd_t_max = (sqrt_limit - 1) // 2
    add_seq = PowerSeq.triangular(w)
    trim_seq = PowerSeq.triangular(w)
    window = 0
    factor = winv
    ratio = winv10

    for t in range(0, odd_t_max + 1):
        disc = 4 * limit + 20 * t * t + 20 * t + 5
        vmax = (math.isqrt(disc) - 1) // 2
        window = add_seq.extend_through(vmax, window)
        window = trim_seq.trim_before(3 * t + 1, window)
        ans = mod_add(ans, mod_mul(factor, window))
        factor = mod_mul(factor, ratio)
        ratio = mod_mul(ratio, winv10)

    return ans


def square_powers(base, max_g):
    out = array("I", [0]) * (max_g + 1)
    out[0] = 1
    if max_g == 0:
        return out

    base_sq = mod_mul(base, base)
    value = 1
    ratio = base
    for g in range(1, max_g + 1):
        value = mod_mul(value, ratio)
        out[g] = value
        ratio = mod_mul(ratio, base_sq)
    return out


def choose_process_count(allow_multiprocessing, requested_processes, workload):
    if not allow_multiprocessing or workload <= 1 or workload < 1_000_000:
        return 1

    processes = requested_processes
    if processes == 0:
        processes = min(mp.cpu_count() or 1, 16)
    if processes > workload:
        processes = workload
    return max(1, processes)


def _set_worker_state(limit, mu, phi_sq, phi_inv_sq):
    global _WORK_LIMIT, _WORK_MU, _WORK_PHI_SQ, _WORK_PHI_INV_SQ
    _WORK_LIMIT = limit
    _WORK_MU = mu
    _WORK_PHI_SQ = phi_sq
    _WORK_PHI_INV_SQ = phi_inv_sq


def _primitive_worker(bounds):
    start_g, end_g = bounds

    limit = _WORK_LIMIT
    mu = _WORK_MU
    phi_sq = _WORK_PHI_SQ
    phi_inv_sq = _WORK_PHI_INV_SQ

    phi_total = 0
    psi_total = 0

    for g in range(start_g, end_g):
        mu_g = mu[g]
        if mu_g == 0:
            continue

        gg = g * g
        scaled_limit = limit // gg

        phi_w = phi_sq[g]
        phi_winv = phi_inv_sq[g]
        if (g & 1) == 0:
            psi_w = phi_winv
            psi_winv = phi_w
        else:
            psi_w = mod_neg(phi_winv)
            psi_winv = mod_neg(phi_w)

        phi_value = nonprimitive_sum(scaled_limit, phi_w, phi_winv)
        psi_value = nonprimitive_sum(scaled_limit, psi_w, psi_winv)

        if mu_g > 0:
            phi_total += phi_value
            psi_total += psi_value
        else:
            phi_total -= phi_value
            psi_total -= psi_value

    return phi_total, psi_total


def build_work_chunks(max_g, process_count):
    chunk_count = max(process_count * 16, 1)
    chunk_size = max(1, (max_g + chunk_count - 1) // chunk_count)
    bounds = []
    start_g = 1
    while start_g <= max_g:
        end_g = min(max_g + 1, start_g + chunk_size)
        bounds.append((start_g, end_g))
        start_g = end_g
    return bounds


def primitive_sums(limit, mu, phi_sq, phi_inv_sq, options):
    max_g = math.isqrt(limit)
    process_count = choose_process_count(
        options.allow_multiprocessing,
        options.requested_processes,
        max_g,
    )

    _set_worker_state(limit, mu, phi_sq, phi_inv_sq)
    if process_count == 1:
        phi_total, psi_total = _primitive_worker((1, max_g + 1))
        return normalize_signed_mod(phi_total), normalize_signed_mod(psi_total)

    try:
        ctx = mp.get_context("fork")
    except ValueError:
        phi_total, psi_total = _primitive_worker((1, max_g + 1))
        return normalize_signed_mod(phi_total), normalize_signed_mod(psi_total)

    bounds = build_work_chunks(max_g, process_count)

    with ctx.Pool(process_count) as pool:
        totals = list(pool.imap_unordered(_primitive_worker, bounds, chunksize=1))

    phi_total = sum(item[0] for item in totals)
    psi_total = sum(item[1] for item in totals)
    return normalize_signed_mod(phi_total), normalize_signed_mod(psi_total)


def solve(limit, options=None):
    if options is None:
        options = Options()

    max_g = math.isqrt(limit)
    mu = mobius_sieve(max_g)

    phi_inv = mod_pow(PHI_MOD, MOD - 2)
    phi_sq = square_powers(PHI_MOD, max_g)
    phi_inv_sq = square_powers(phi_inv, max_g)

    phi_sum, psi_sum = primitive_sums(limit, mu, phi_sq, phi_inv_sq, options)
    inv_sqrt5 = mod_pow(SQRT5_MOD, MOD - 2)
    return mod_mul(mod_sub(phi_sum, psi_sum), inv_sqrt5)


def checksum_via_factorization(limit, primes):
    acc = 0
    f_prev = 0
    f_cur = 1
    for n in range(1, limit + 1):
        g = g_from_factorization(n, primes)
        acc = mod_add(acc, mod_mul(f_cur, g))
        f_prev, f_cur = f_cur, mod_add(f_prev, f_cur)
    return acc


def run_checkpoints():
    options = Options()
    options.allow_multiprocessing = False

    assert mod_mul(SQRT5_MOD, SQRT5_MOD) == 5
    assert mod_sub(mod_mul(PHI_MOD, PHI_MOD), PHI_MOD) == 1
    assert mod_sub(mod_mul(PSI_MOD, PSI_MOD), PSI_MOD) == 1
    assert mod_mul(PHI_MOD, PSI_MOD) == MOD - 1

    check_max = 250
    prime_limit = math.isqrt(check_max) + 10
    primes = sieve_primes(prime_limit)
    for n in range(1, check_max + 1):
        brute = g_bruteforce(n)
        factorized = g_from_factorization(n, primes)
        assert brute == factorized

    for n in range(1, check_max + 1):
        reduced_pairs = reduced_pair_count(n)
        factorized = g_from_factorization(n, primes)
        assert reduced_pairs == factorized

    direct_limit = min(check_max, 250)
    phi_pair_sum = direct_pair_sum(direct_limit, PHI_MOD)
    psi_pair_sum = direct_pair_sum(direct_limit, PSI_MOD)
    max_g = math.isqrt(direct_limit)
    mu = mobius_sieve(max_g)
    phi_inv = mod_pow(PHI_MOD, MOD - 2)
    phi_sq = square_powers(PHI_MOD, max_g)
    phi_inv_sq = square_powers(phi_inv, max_g)
    phi_fast, psi_fast = primitive_sums(direct_limit, mu, phi_sq, phi_inv_sq, options)
    assert phi_fast == phi_pair_sum
    assert psi_fast == psi_pair_sum

    sample_prime_limit = math.isqrt(SAMPLE_LIMIT) + 10
    sample_primes = sieve_primes(sample_prime_limit)
    sample_fast = solve(SAMPLE_LIMIT, options)
    sample_factorized = checksum_via_factorization(SAMPLE_LIMIT, sample_primes)
    assert sample_fast == SAMPLE_SUM
    assert sample_fast == sample_factorized


def usage():
    print(
        "Usage:\n"
        "  python Euler989.py [--skip-checkpoints] [--single-thread] [--threads=N]\n"
        "  python Euler989.py validate [check_max]\n"
        "  python Euler989.py sum <limit> [--single-thread] [--threads=N]\n"
        "  python Euler989.py answer [--single-thread] [--threads=N]",
        file=sys.stderr,
    )


def parse_unsigned_after_prefix(arg, prefix):
    if not arg.startswith(prefix):
        return None
    tail = arg[len(prefix) :]
    if not tail or not tail.isdigit():
        return None
    return int(tail)


def parse_command_options(args):
    options = Options()
    positional = []
    for arg in args:
        if arg in ("--single-process", "--single-thread"):
            options.allow_multiprocessing = False
            continue
        processes = parse_unsigned_after_prefix(arg, "--processes=")
        if processes is not None:
            options.requested_processes = processes
            continue
        threads = parse_unsigned_after_prefix(arg, "--threads=")
        if threads is not None:
            options.requested_processes = threads
            continue
        positional.append(arg)
    return options, positional


def main(argv):
    args = list(argv[1:])
    should_run_checkpoints = True
    if "--skip-checkpoints" in args:
        should_run_checkpoints = False
        args.remove("--skip-checkpoints")

    if should_run_checkpoints:
        run_checkpoints()

    options, positional = parse_command_options(args)

    if not positional:
        print(solve(TARGET_LIMIT, options))
        return 0

    command = positional[0]
    if command == "validate":
        if len(positional) > 2:
            usage()
            return 1
        check_max = 250 if len(positional) == 1 else int(positional[1])
        prime_limit = math.isqrt(check_max) + 10
        primes = sieve_primes(prime_limit)
        for n in range(1, check_max + 1):
            assert g_bruteforce(n) == g_from_factorization(n, primes)
            assert reduced_pair_count(n) == g_from_factorization(n, primes)
        print("ok")
        return 0

    if command == "sum" and len(positional) == 2:
        print(solve(int(positional[1]), options))
        return 0

    if command == "answer" and len(positional) == 1:
        print(solve(TARGET_LIMIT, options))
        return 0

    usage()
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
