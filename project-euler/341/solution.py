def precompute_golomb_until(max_query_position):
    golomb = [0, 1]
    
    products = 1
    i = 2
    
    while products < max_query_position:
        prev = i - 1
        g_prev = golomb[prev]
        nested = golomb[g_prev]
        idx = i - nested
        current = 1 + golomb[idx]
        
        golomb.append(current)
        products += i * current
        i += 1
        
    return golomb

class QueryState:
    def __init__(self):
        self.index = 1
        self.sum = 1
        self.products = 1
        self.prev_sum = 0
        self.prev_products = 0

def golomb_at(x, golomb, st):
    while st.products < x:
        st.index += 1
        st.prev_sum = st.sum
        st.prev_products = st.products
        
        g = golomb[st.index]
        st.sum += g
        st.products += st.index * g
        
    span_index = st.index
    offset = (x - st.prev_products + span_index - 1) // span_index
    return st.prev_sum + offset

def sum_golomb_cubes(limit, golomb):
    st = QueryState()
    total_sum = 0
    
    for n in range(1, limit):
        cube = n * n * n
        total_sum += golomb_at(cube, golomb, st)
        
    return total_sum

def solve():
    limit = 1000000
    max_query_position = (limit - 1) ** 3
    golomb = precompute_golomb_until(max_query_position)
    ans = sum_golomb_cubes(limit, golomb)
    return str(ans)

if __name__ == '__main__':
    print(solve())
