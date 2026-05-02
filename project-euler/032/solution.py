import sys

def is_1_to_9_pandigital_triplet(a, b, product):
    used = [False] * 10
    digits_seen = 0
    
    def add_digits(value):
        nonlocal digits_seen
        while value > 0:
            d = value % 10
            if d == 0 or used[d]:
                return False
            used[d] = True
            digits_seen += 1
            value //= 10
        return True
    
    if not add_digits(a) or not add_digits(b) or not add_digits(product):
        return False
    
    if digits_seen != 9:
        return False
    
    for d in range(1, 10):
        if not used[d]:
            return False
    
    return True

def solve():
    products = set()
    
    for a in range(1, 10):
        for b in range(1234, 9877):
            p = a * b
            if is_1_to_9_pandigital_triplet(a, b, p):
                products.add(p)
    
    for a in range(12, 99):
        for b in range(123, 988):
            p = a * b
            if is_1_to_9_pandigital_triplet(a, b, p):
                products.add(p)
    
    return sum(products)

def run_checkpoints():
    if not is_1_to_9_pandigital_triplet(39, 186, 7254):
        sys.stderr.write("Checkpoint failed for example identity\n")
        return False
    if is_1_to_9_pandigital_triplet(12, 34, 408):
        sys.stderr.write("Checkpoint failed for non-pandigital identity\n")
        return False
    return True

def main():
    args = sys.argv[1:]
    run_checkpoints_flag = True
    
    for arg in args:
        if arg == "--skip-checkpoints":
            run_checkpoints_flag = False
        else:
            sys.stderr.write(f"Unknown argument: {arg}\n")
            return 1
    
    if run_checkpoints_flag and not run_checkpoints():
        return 2
    
    print(solve())
    return 0

if __name__ == "__main__":
    sys.exit(main())
