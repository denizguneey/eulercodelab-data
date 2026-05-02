import sys
import os

sys.setrecursionlimit(20000)

MOD = 1000000000

class VarNode:
    def __init__(self, name):
        self.type = 'VAR'
        self.name = name

class INode:
    def __init__(self, left, right):
        self.type = 'I'
        self.left = left
        self.right = right

def serialize(n):
    if n.type == 'VAR':
        return n.name
    return 'I(' + serialize(n.left) + ',' + serialize(n.right) + ')'

class Parser:
    def __init__(self, input_str):
        self.s = input_str
        self.pos = 0
        self.n = len(self.s)
        
    def skip(self):
        while self.pos < self.n and self.s[self.pos].isspace():
            self.pos += 1
            
    def consume(self, c):
        self.skip()
        if self.pos < self.n and self.s[self.pos] == c:
            self.pos += 1
            return True
        return False
        
    def matchString(self, string):
        self.skip()
        if self.s.startswith(string, self.pos):
            self.pos += len(string)
            return True
        return False
        
    def parse_term(self):
        if self.matchString('I(') or self.matchString('J('):
            left = self.parse_term()
            self.consume(',')
            right = self.parse_term()
            self.consume(')')
            return INode(left, right)
        else:
            self.skip()
            start = self.pos
            while self.pos < self.n and (self.s[self.pos].isalnum() or self.s[self.pos] == '_'):
                self.pos += 1
            name = self.s[start:self.pos]
            return VarNode(name)
            
    def has_more(self):
        self.skip()
        return self.pos < self.n

def resolve(node, bindings):
    if node.type == 'VAR' and node.name in bindings:
        return resolve(bindings[node.name], bindings)
    return node

def occurs(var_name, term, bindings, visited):
    r = resolve(term, bindings)
    if id(r) in visited:
        return False
    visited.add(id(r))
    
    if r.type == 'VAR':
        return r.name == var_name
    return occurs(var_name, r.left, bindings, visited) or occurs(var_name, r.right, bindings, visited)

def unify(t1, t2, bindings):
    r1 = resolve(t1, bindings)
    r2 = resolve(t2, bindings)
    
    if r1 is r2: return True
    
    if r1.type == 'VAR':
        if r2.type == 'VAR' and r2.name == r1.name: return True
        visited = set()
        if occurs(r1.name, r2, bindings, visited): return False
        bindings[r1.name] = r2
        return True
        
    if r2.type == 'VAR':
        visited = set()
        if occurs(r2.name, r1, bindings, visited): return False
        bindings[r2.name] = r1
        return True
        
    if r1.type == 'I' and r2.type == 'I':
        return unify(r1.left, r2.left, bindings) and unify(r1.right, r2.right, bindings)
        
    return False

def evalJ(x, y):
    s = (1 + x + y) % MOD
    term1 = (s * s) % MOD
    diff = (y - x) % MOD
    res = (term1 + diff) % MOD
    return res

def evaluate(node, bindings, cache):
    r = resolve(node, bindings)
    if id(r) in cache:
        return cache[id(r)]
        
    if r.type == 'VAR':
        res = 0
    else:
        lv = evaluate(r.left, bindings, cache)
        rv = evaluate(r.right, bindings, cache)
        res = evalJ(lv, rv)
        
    cache[id(r)] = res
    return res

def solve_pair(e1, e2):
    bindings = {}
    if unify(e1, e2, bindings):
        return evaluate(e1, bindings, {})
    return 0

def solve():
    content = ""
    paths = ['I-expressions.txt', 'solutionsCpp/I-expressions.txt', '../I-expressions.txt']
    for path in paths:
        if os.path.exists(path):
            with open(path, 'r') as f:
                content = f.read()
            break
    if not content:
        return "File not found"
        
    parser = Parser(content)
    file_exprs = []
    while parser.has_more():
        file_exprs.append(parser.parse_term())
        
    str_to_id = {}
    unique_exprs = []
    file_ids = []
    
    for e in file_exprs:
        s = serialize(e)
        if s not in str_to_id:
            str_to_id[s] = len(unique_exprs)
            unique_exprs.append(e)
        file_ids.append(str_to_id[s])
        
    n_unique = len(unique_exprs)
    pair_cache = {}
    
    for i in range(n_unique):
        for j in range(i, n_unique):
            val = solve_pair(unique_exprs[i], unique_exprs[j])
            pair_cache[(i, j)] = val
            pair_cache[(j, i)] = val
            
    total_sum = 0
    total_exprs = len(file_exprs)
    for i in range(total_exprs):
        for j in range(i + 1, total_exprs):
            id1 = file_ids[i]
            id2 = file_ids[j]
            if id1 == id2:
                continue
            total_sum = (total_sum + pair_cache[(id1, id2)]) % MOD
            
    return str(total_sum)

if __name__ == '__main__':
    print(solve())
