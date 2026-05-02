def letters_for_number(n):
    ones = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4]
    teens = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
    tens = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6]

    if n == 1000:
        return 11  # "onethousand"
    count = 0
    if n >= 100:
        count += ones[n // 100] + 7  # "xhundred"
        n %= 100
        if n != 0:
            count += 3  # "and"
    if n >= 20:
        count += tens[n // 10] + ones[n % 10]
    elif n >= 10:
        count += teens[n - 10]
    else:
        count += ones[n]
    return count

def solve(limit=1000):
    return sum(letters_for_number(n) for n in range(1, limit + 1))

if __name__ == "__main__":
    assert solve(5) == 19, "Checkpoint failed for limit=5"
    assert letters_for_number(342) == 23, "Checkpoint failed for n=342"
    print(solve())
