import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    t = int(data[0])
    idx = 1
    
    MOD = 676767677
    out = []
    
    for _ in range(t):
        n = int(data[idx])
        a = [int(x) for x in data[idx+1 : idx+1+n]]
        idx += 1 + n
        
        # Calculate minimum cost
        ans = 0
        for x in a:
            if x > 1:
                ans += x
        
        # If the last element is 1, it costs 1 to remove
        if a[-1] == 1:
            ans += 1
            
        out.append(str(ans % MOD))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
