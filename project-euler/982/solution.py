import math
import sys

EPS = 1e-10

class Simplex:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.T = [[0.0] * (n + 1) for _ in range(m + 1)]
        self.basis = [-1] * m
        
    def pivot(self, r, c):
        inv = 1.0 / self.T[r][c]
        for j in range(self.n + 1):
            self.T[r][j] *= inv
        for i in range(self.m + 1):
            if i == r:
                continue
            factor = self.T[i][c]
            if abs(factor) <= EPS:
                continue
            for j in range(self.n + 1):
                self.T[i][j] -= factor * self.T[r][j]
        self.basis[r] = c
        
    def set_objective(self, c_obj):
        for j in range(self.n + 1):
            self.T[self.m][j] = 0.0
        for j in range(self.n):
            self.T[self.m][j] = -c_obj[j]
        for i in range(self.m):
            var = self.basis[i]
            if var < 0:
                continue
            coeff = c_obj[var]
            if abs(coeff) <= EPS:
                continue
            for j in range(self.n + 1):
                self.T[self.m][j] += coeff * self.T[i][j]
                
    def solve(self):
        while True:
            enter = -1
            for j in range(self.n):
                if self.T[self.m][j] < -EPS:
                    enter = j
                    break
            if enter == -1:
                return True
                
            min_ratio = 0.0
            leave = -1
            for i in range(self.m):
                a = self.T[i][enter]
                if a > EPS:
                    ratio = self.T[i][self.n] / a
                    if leave == -1 or ratio < min_ratio - 1e-12 or (abs(ratio - min_ratio) <= 1e-12 and self.basis[i] < self.basis[leave]):
                        min_ratio = ratio
                        leave = i
            if leave == -1:
                return False
            self.pivot(leave, enter)
            
    def objective_value(self):
        return self.T[self.m][self.n]

class GameData:
    def __init__(self):
        self.dice = 0
        self.actions = 0
        self.states = 0
        self.obs = 0
        self.prob = 0.0
        self.visible_max = []
        self.action_obs = []
        self.action_hidden = []

def build_game(dice):
    g = GameData()
    g.dice = dice
    g.actions = dice
    if dice == 2:
        g.states = 36
        g.obs = 6
        g.prob = 1.0 / 36.0
        g.visible_max = [v + 1 for v in range(g.obs)]
        
        n_action = g.states * g.actions
        g.action_obs = [0] * n_action
        g.action_hidden = [0] * n_action
        
        for a in range(1, 7):
            for b in range(1, 7):
                s = (a - 1) * 6 + (b - 1)
                base = s * 2
                g.action_obs[base] = b - 1
                g.action_hidden[base] = a
                g.action_obs[base + 1] = a - 1
                g.action_hidden[base + 1] = b
        return g
        
    if dice == 3:
        g.states = 216
        g.obs = 21
        g.prob = 1.0 / 216.0
        
        obs_index = [[-1] * 7 for _ in range(7)]
        g.visible_max = [0] * g.obs
        idx = 0
        for u in range(1, 7):
            for v in range(u, 7):
                obs_index[u][v] = idx
                obs_index[v][u] = idx
                g.visible_max[idx] = v
                idx += 1
                
        n_action = g.states * g.actions
        g.action_obs = [0] * n_action
        g.action_hidden = [0] * n_action
        
        for a in range(1, 7):
            for b in range(1, 7):
                for c in range(1, 7):
                    s = ((a - 1) * 6 + (b - 1)) * 6 + (c - 1)
                    base = s * 3
                    g.action_obs[base] = obs_index[b][c]
                    g.action_hidden[base] = a
                    g.action_obs[base + 1] = obs_index[a][c]
                    g.action_hidden[base + 1] = b
                    g.action_obs[base + 2] = obs_index[a][b]
                    g.action_hidden[base + 2] = c
        return g
    return g

class LPData:
    def __init__(self, rows, cols, actions, tvars, slack, art, art_s, slack_s):
        self.lp = Simplex(rows, cols)
        self.n_action = actions
        self.n_T = tvars
        self.n_slack = slack
        self.n_art = art
        self.art_start = art_s
        self.slack_start = slack_s

def build_lp(g):
    n_action = g.states * g.actions
    n_T = g.obs
    n_orig = n_action + n_T
    n_slack = g.obs * 2
    n_art = g.states
    n_total = n_orig + n_slack + n_art
    rows = g.states + n_slack
    
    slack_start = n_orig
    art_start = n_orig + n_slack
    
    data = LPData(rows, n_total, n_action, n_T, n_slack, n_art, art_start, slack_start)
    lp = data.lp
    
    for s in range(g.states):
        row = s
        base = s * g.actions
        for a in range(g.actions):
            lp.T[row][base + a] = 1.0
        lp.T[row][art_start + s] = 1.0
        lp.T[row][n_total] = 1.0
        lp.basis[row] = art_start + s
        
    for o in range(g.obs):
        for t in range(2):
            row = g.states + o * 2 + t
            tvar = n_action + o
            lp.T[row][tvar] = -1.0
            lp.T[row][slack_start + o * 2 + t] = 1.0
            lp.T[row][n_total] = 0.0
            lp.basis[row] = slack_start + o * 2 + t
            
    for idx in range(n_action):
        obs = g.action_obs[idx]
        hidden = g.action_hidden[idx]
        row_hidden = g.states + obs * 2
        row_visible = row_hidden + 1
        lp.T[row_hidden][idx] += g.prob * hidden
        lp.T[row_visible][idx] += g.prob * g.visible_max[obs]
        
    return data

def remove_artificial(lp, art_start, art_count):
    if art_count == 0:
        return
    rows_to_remove = []
    is_art = [False] * lp.n
    for i in range(art_count):
        is_art[art_start + i] = True
        
    for i in range(lp.m):
        var = lp.basis[i]
        if var < 0 or not is_art[var]:
            continue
        pivot_col = -1
        for j in range(lp.n):
            if is_art[j]: continue
            if abs(lp.T[i][j]) > EPS:
                pivot_col = j
                break
        if pivot_col != -1:
            lp.pivot(i, pivot_col)
        else:
            rows_to_remove.append(i)
            
    if rows_to_remove:
        drop = [False] * lp.m
        for r in rows_to_remove:
            drop[r] = True
        new_m = lp.m - len(rows_to_remove)
        newT = [[0.0] * (lp.n + 1) for _ in range(new_m + 1)]
        new_basis = [-1] * new_m
        r2 = 0
        for i in range(lp.m):
            if drop[i]: continue
            newT[r2] = lp.T[i][:]
            new_basis[r2] = lp.basis[i]
            r2 += 1
        newT[new_m] = lp.T[lp.m][:]
        lp.T = newT
        lp.basis = new_basis
        lp.m = new_m
        
    new_n = lp.n - art_count
    newT2 = [[0.0] * (new_n + 1) for _ in range(lp.m + 1)]
    for i in range(lp.m + 1):
        col_new = 0
        for j in range(lp.n):
            if not is_art[j]:
                newT2[i][col_new] = lp.T[i][j]
                col_new += 1
        newT2[i][new_n] = lp.T[i][lp.n]
        
    lp.n = new_n
    lp.T = newT2

def solve_game(dice):
    g = build_game(dice)
    if g.states == 0:
        return float('nan')
        
    data = build_lp(g)
    lp = data.lp
    
    c1 = [0.0] * lp.n
    for i in range(data.n_art):
        c1[data.art_start + i] = -1.0
    lp.set_objective(c1)
    
    if not lp.solve():
        return float('nan')
        
    phase1 = lp.objective_value()
    if phase1 < -1e-8:
        return float('nan')
        
    remove_artificial(lp, data.art_start, data.n_art)
    
    c2 = [0.0] * lp.n
    for i in range(data.n_T):
        c2[data.n_action + i] = -1.0
    lp.set_objective(c2)
    
    if not lp.solve():
        return float('nan')
        
    return -lp.objective_value()

def run_validation():
    expected = 145.0 / 36.0
    got = solve_game(2)
    assert abs(got - expected) <= 1e-7

def solve():
    answer = solve_game(3)
    return f"{answer:.6f}"

if __name__ == "__main__":
    run_validation()
    print(solve())
