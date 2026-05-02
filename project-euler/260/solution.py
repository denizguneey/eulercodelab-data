def solve():
    limit = 1000
    side = limit + 1
    one = bytearray(side * side)
    two = bytearray(side * side)
    all_tab = bytearray(side * side)

    total = 0
    for x in range(limit + 1):
        for y in range(x, limit + 1):
            for z in range(y, limit + 1):
                yz = y * side + z
                xz = x * side + z
                xy = x * side + y
                yx_z = (y - x) * side + z
                zy_x = (z - y) * side + x
                zx_y = (z - x) * side + y
                yx_zx = (y - x) * side + (z - x)
                if (one[yz] or one[xz] or one[xy] or
                    two[yx_z] or two[zy_x] or two[zx_y] or
                    all_tab[yx_zx]):
                    continue
                total += x + y + z
                one[yz] = 1
                one[xz] = 1
                one[xy] = 1
                two[yx_z] = 1
                two[zy_x] = 1
                two[zx_y] = 1
                all_tab[yx_zx] = 1
    return str(total)

if __name__ == '__main__':
    print(solve())
