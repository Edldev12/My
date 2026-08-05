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
        w = [int(x) for x in data[idx + 1 : idx + 1 + n]]
        idx += 1 + n
        
        # 1. n MUST be even. If n is odd, it's structurally impossible 
        # to fill every position from 1 to n.
        if n % 2 != 0:
            out.append("NO")
            continue
            
        max_even = -1
        min_odd = float('inf')
        
        for i in range(n):
            # 1-indexed odd positions are at 0-indexed even positions (0, 2, 4...)
            if i % 2 == 0: 
                min_odd = min(min_odd, w[i])
            # 1-indexed even positions are at 0-indexed odd positions (1, 3, 5...)
            else: 
                max_even = max(max_even, w[i])
        
        # We need an integer k such that max_even < k < min_odd
        # For a valid integer to sit strictly between them, 
        # min_odd must be at least max_even + 2.
        if max_even + 1 < min_odd:
            out.append("YES")
        else:
            out.append("NO")
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
