import sys

# Increase recursion depth just in case, though the solution is iterative
sys.setrecursionlimit(200000)

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.tree = [float('inf')] * (n + 2)

    def update(self, idx, val):
        idx += 1  # Convert to 1-based index
        while idx <= self.n + 1:
            if val < self.tree[idx]:
                self.tree[idx] = val
            idx += idx & -idx

    def query(self, idx):
        idx += 1
        if idx <= 0:
            return float('inf')
        if idx > self.n + 1:
            idx = self.n + 1
        res = float('inf')
        while idx > 0:
            if self.tree[idx] < res:
                res = self.tree[idx]
            idx -= idx & -idx
        return res

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    t = int(data[0])
    idx = 1
    
    out = []
    for _ in range(t):
        n = int(data[idx])
        s = data[idx+1]
        idx += 2
        
        if n % 2 != 0:
            out.append("NO")
            continue
            
        total_opens = s.count('(')
        if total_opens != n // 2:
            out.append("NO")
            continue

        b = [0] * (n + 1)
        opens_pref = [0] * (n + 1)
        for i in range(n):
            b[i + 1] = b[i] + (1 if s[i] == '(' else -1)
            opens_pref[i + 1] = opens_pref[i] + (1 if s[i] == '(' else 0)

        min_bal_A = [0] * (n + 1)
        for i in range(1, n + 1):
            min_bal_A[i] = min(min_bal_A[i - 1], b[i])

        suff_min_b = [0] * (n + 1)
        suff_min_b[n] = b[n]
        for i in range(n - 1, -1, -1):
            suff_min_b[i] = min(suff_min_b[i + 1], b[i])

        bit = Fenwick(n)
        possible = False

        for i in range(n, -1, -1):
            opens_C = opens_pref[n] - opens_pref[i]
            min_bal_C = suff_min_b[i] - b[i]
            U = opens_C
            V = opens_C - min_bal_C
            bit.update(U, V)

            X = min_bal_A[i] - opens_pref[i] + n // 2
            Y = b[i] - opens_pref[i] + n // 2

            if X >= 0:
                if bit.query(X) <= Y:
                    possible = True
                    break

        out.append("YES" if possible else "NO")
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
