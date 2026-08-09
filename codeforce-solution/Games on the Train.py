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
        # Read the next n elements as heights
        h = [int(x) for x in data[idx+1 : idx+1+n]]
        idx += 1 + n
        
        # Calculate minimum k
        max_h = max(h)
        min_h = min(h)
        k = max_h + 1 - min_h
        
        out.append(str(k))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
