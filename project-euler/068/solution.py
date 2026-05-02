import sys
from itertools import permutations, combinations


def solve():
    nums = list(range(1, 11))
    
    best = ""
    
    # Choose inner ring (5 numbers in cyclic order), derive outer ring from line sums.
    for mask_bits in combinations(range(10), 5):
        inner_set = [nums[i] for i in mask_bits]
        outer_set = [nums[i] for i in range(10) if i not in mask_bits]
        
        inner_set.sort()
        
        for perm_inner in permutations(inner_set):
            i1, i2, i3, i4, i5 = perm_inner
            
            for o1 in outer_set:
                target_sum = o1 + i1 + i2
                
                o2 = target_sum - i2 - i3
                o3 = target_sum - i3 - i4
                o4 = target_sum - i4 - i5
                o5 = target_sum - i5 - i1
                
                outer = [o1, o2, o3, o4, o5]
                
                # Check if all outer numbers are in the required set and used exactly once
                temp_outer = sorted(outer)
                if sorted(outer_set) != temp_outer:
                    continue
                
                # Check that the representation starts with the smallest outer number
                min_outer = min(outer)
                if outer[0] != min_outer:
                    continue
                
                # Build the string representation
                repr_parts = []
                repr_parts.append(str(outer[0]) + str(i1) + str(i2))
                repr_parts.append(str(outer[1]) + str(i2) + str(i3))
                repr_parts.append(str(outer[2]) + str(i3) + str(i4))
                repr_parts.append(str(outer[3]) + str(i4) + str(i5))
                repr_parts.append(str(outer[4]) + str(i5) + str(i1))
                
                repr_str = ''.join(repr_parts)
                
                if len(repr_str) == 16 and repr_str > best:
                    best = repr_str
    
    return int(best) if best else 0


def main():
    args = sys.argv[1:]
    
    # Parse arguments (only --skip-checkpoints is supported, but we ignore it for simplicity)
    run_checkpoints = True
    i = 0
    while i < len(args):
        if args[i] == "--skip-checkpoints":
            run_checkpoints = False
        else:
            sys.stderr.write(f"Unknown argument: {args[i]}\n")
            sys.exit(1)
        i += 1
    
    # For this problem, we just compute and print the answer
    result = solve()
    print(result)


if __name__ == "__main__":
    main()
