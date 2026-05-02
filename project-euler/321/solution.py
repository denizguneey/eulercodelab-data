def solve(terms=40):
    a_x, a_y = 5, 2
    b_x, b_y = 11, 4
    
    total = 0
    taken = 0
    while taken < terms:
        na = a_y - 1
        nb = b_y - 1
        if na < nb:
            total += na
            nx = 3 * a_x + 8 * a_y
            ny = a_x + 3 * a_y
            a_x, a_y = nx, ny
        else:
            total += nb
            nx = 3 * b_x + 8 * b_y
            ny = b_x + 3 * b_y
            b_x, b_y = nx, ny
        taken += 1
        
    return str(total)

if __name__ == '__main__':
    print(solve())
