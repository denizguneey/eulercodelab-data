import math
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
import sys

def sieve_primes(limit):
    if limit < 2:
        return []
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(limit ** 0.5) + 1):
        if is_prime[p]:
            for q in range(p * p, limit + 1, p):
                is_prime[q] = False
    return [p for p in range(2, limit + 1) if is_prime[p]]

def mod_inverse(a, mod):
    t, new_t = 0, 1
    r, new_r = mod, a % mod
    while new_r != 0:
        q = r // new_r
        t, new_t = new_t, t - q * new_t
        r, new_r = new_r, r - q * new_r
    if r != 1:
        raise ValueError("Modular inverse does not exist")
    t %= mod
    if t < 0:
        t += mod
    return t

def build_odd_prime_top_groups(limit):
    primes = sieve_primes(limit)
    groups = []

    for p in primes:
        if p == 2:
            continue

        prime_power = p
        while prime_power <= limit // p:
            prime_power *= p

        numbers = []
        next_power = prime_power * p
        for n in range(2, limit + 1):
            if n % prime_power != 0:
                continue
            if next_power <= limit and n % next_power == 0:
                continue
            numbers.append(n)

        if not numbers:
            continue

        mod = p * p
        coeffs = []
        for n in numbers:
            m = n // prime_power
            sq = (m * m) % mod
            coeffs.append(mod_inverse(sq, mod))

        valid_masks = []
        used_union_mask = 0
        mask_count = 1 << len(numbers)

        for mask in range(mask_count):
            residue = 0
            for i, coeff in enumerate(coeffs):
                if (mask >> i) & 1:
                    residue += coeff
                    residue %= mod
            if residue == 0:
                valid_masks.append(mask)
                used_union_mask |= mask

        groups.append({
            'prime': p,
            'prime_power': prime_power,
            'numbers': numbers,
            'valid_masks': valid_masks,
            'used_union_mask': used_union_mask
        })

    return groups

def subset_sum_counts(weights):
    mask_count = 1 << len(weights)
    counts = defaultdict(int)

    for mask in range(mask_count):
        total = 0
        for i, w in enumerate(weights):
            if (mask >> i) & 1:
                total += w
        counts[total] += 1

    return dict(counts)

def count_with_meet_in_middle(free_weights, base_states, target, thread_count):
    mid = len(free_weights) // 2
    left_weights = free_weights[:mid]
    right_weights = free_weights[mid:]

    left_counts = subset_sum_counts(left_weights)
    right_counts = subset_sum_counts(right_weights)

    left_entries = list(left_counts.items())

    def count_chunk(begin, end):
        local_count = 0
        for i in range(begin, end):
            left_sum, left_ways = left_entries[i]
            for base_sum, base_ways in base_states:
                need = target - base_sum - left_sum
                if need in right_counts:
                    local_count += left_ways * right_counts[need] * base_ways
        return local_count

    if thread_count <= 1 or len(left_entries) < 12000:
        return count_chunk(0, len(left_entries))

    workers = min(thread_count, len(left_entries))
    chunk_size = 256
    next_idx = [0]
    lock = __import__('threading').Lock()

    def worker(t):
        local_count = 0
        while True:
            with lock:
                begin = next_idx[0]
                next_idx[0] += chunk_size
            if begin >= len(left_entries):
                break
            end = min(begin + chunk_size, len(left_entries))
            local_count += count_chunk(begin, end)
        return local_count

    with ThreadPoolExecutor(max_workers=workers) as executor:
        results = list(executor.map(worker, range(workers)))

    return sum(results)

def count_representations(limit, thread_count):
    if limit < 2:
        return 0

    groups = build_odd_prime_top_groups(limit)

    number_to_group = [-1] * (limit + 1)
    number_to_group_bit = [-1] * (limit + 1)

    for g_idx, group in enumerate(groups):
        for i, n in enumerate(group['numbers']):
            number_to_group[n] = g_idx
            number_to_group_bit[n] = i

    active_groups = []
    for group in groups:
        if len(group['valid_masks']) == 1 and group['valid_masks'][0] == 0:
            continue
        active_groups.append(group)

    number_is_possible = [False] * (limit + 1)
    free_numbers = []

    for n in range(2, limit + 1):
        gid = number_to_group[n]
        if gid == -1:
            number_is_possible[n] = True
            free_numbers.append(n)
            continue

        group = groups[gid]
        bit = number_to_group_bit[n]
        if (group['used_union_mask'] >> bit) & 1:
            number_is_possible[n] = True

    common = 1
    for n in range(2, limit + 1):
        if not number_is_possible[n]:
            continue
        common = common * n // math.gcd(common, n)

    common_sq = common * common
    if common_sq % 2 != 0:
        raise ValueError("Unexpected odd denominator square")

    target = common_sq // 2

    weight_by_number = [0] * (limit + 1)
    for n in range(2, limit + 1):
        if not number_is_possible[n]:
            continue
        nn = n * n
        if common_sq % nn != 0:
            raise ValueError("Weight is not integral")
        weight_by_number[n] = common_sq // nn

    base_states = {0: 1}

    for group in active_groups:
        option_counts = defaultdict(int)

        for mask in group['valid_masks']:
            total = 0
            for i, n in enumerate(group['numbers']):
                if (mask >> i) & 1:
                    total += weight_by_number[n]
            option_counts[total] += 1

        next_states = defaultdict(int)
        for base_sum, base_ways in base_states.items():
            for opt_sum, opt_ways in option_counts.items():
                next_states[base_sum + opt_sum] += base_ways * opt_ways

        base_states = next_states

    free_weights = [weight_by_number[n] for n in free_numbers]

    base_entries = list(base_states.items())

    return count_with_meet_in_middle(free_weights, base_entries, target, thread_count)

def brute_force_count(limit):
    if limit < 2:
        return 0

    common = 1
    for n in range(2, limit + 1):
        common = common * n // math.gcd(common, n)

    common_sq = common * common
    if common_sq % 2 != 0:
        raise ValueError("Unexpected odd brute-force denominator square")

    target = common_sq // 2

    weights = []
    for n in range(2, limit + 1):
        weights.append(common_sq // (n * n))

    if len(weights) > 26:
        raise ValueError("Brute-force checkpoint requested above safe size.")

    count = 0
    mask_count = 1 << len(weights)
    for mask in range(mask_count):
        total = 0
        for i, w in enumerate(weights):
            if (mask >> i) & 1:
                total += w
        if total == target:
            count += 1

    return count

def subset_sums_to_half(subset):
    common = 2
    for n in subset:
        common = common * n // math.gcd(common, n)

    common_sq = common * common

    lhs = 0
    for n in subset:
        lhs += common_sq // (n * n)

    return lhs * 2 == common_sq

def run_checkpoints(thread_count):
    known_one = [2, 3, 4, 5, 7, 12, 15, 20, 28, 35]
    known_two = [2, 3, 4, 6, 7, 9, 10, 20, 28, 35, 36, 45]
    known_three = [2, 3, 4, 6, 7, 9, 12, 15, 28, 30, 35, 36, 45]

    if not subset_sums_to_half(known_one):
        sys.stderr.write("Checkpoint failed: first known decomposition is invalid.\n")
        return False
    if not subset_sums_to_half(known_two):
        sys.stderr.write("Checkpoint failed: second known decomposition is invalid.\n")
        return False
    if not subset_sums_to_half(known_three):
        sys.stderr.write("Checkpoint failed: third known decomposition is invalid.\n")
        return False

    count_45 = count_representations(45, thread_count)
    if count_45 != 3:
        sys.stderr.write(f"Checkpoint failed: expected 3 solutions for 2 <= n <= 45, got {count_45}.\n")
        return False

    brute_limit = 18
    brute = brute_force_count(brute_limit)
    fast = count_representations(brute_limit, 1)
    if brute != fast:
        sys.stderr.write(f"Checkpoint failed: fast/brute mismatch at limit {brute_limit} (fast={fast}, brute={brute}).\n")
        return False

    return True

def main():
    args = sys.argv[1:]

    limit = 80
    run_checkpoints_flag = True
    requested_threads = 0

    for arg in args:
        if arg == "--skip-checkpoints":
            run_checkpoints_flag = False
        elif arg.startswith("--threads="):
            try:
                requested_threads = int(arg[10:])
            except ValueError:
                sys.stderr.write(f"Invalid thread count: {arg}\n")
                return 1
        elif arg.startswith("--limit="):
            try:
                limit = int(arg[8:])
            except ValueError:
                sys.stderr.write(f"Invalid limit: {arg}\n")
                return 1
        else:
            sys.stderr.write(f"Unknown argument: {arg}\n")
            return 1

    if limit < 2 or limit > 80:
        sys.stderr.write("Please use --limit in [2, 80].\n")
        return 1

    if requested_threads == 0:
        import os
        hw = os.cpu_count()
        requested_threads = hw if hw else 4

    try:
        if run_checkpoints_flag and not run_checkpoints(requested_threads):
            return 1

        answer = count_representations(limit, requested_threads)
        print(answer)
    except Exception as ex:
        sys.stderr.write(f"Error: {ex}\n")
        return 1

if __name__ == "__main__":
    main()
