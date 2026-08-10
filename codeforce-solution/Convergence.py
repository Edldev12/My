import sys

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
        a = [int(x) for x in data[idx+1 : idx+1+n]]
        idx += 1 + n
        
        # Find the minimum max(L, R) by testing each unique position as the meeting point
        min_calls = n
        unique_positions = set(a)
        
        for x in unique_positions:
            L = 0
            R = 0
            for pos in a:
                if pos < x:
                    L += 1
                elif pos > x:
                    R += 1
            
            min_calls = min(min_calls, max(L, R))
            
        out.append(str(min_calls))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
