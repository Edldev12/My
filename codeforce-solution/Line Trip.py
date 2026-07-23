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
        x = int(data[idx+1])
        idx += 2
        
        # Parse the gas station coordinates
        a = [int(data[idx + i]) for i in range(n)]
        idx += n
        
        # 1. Gap from 0 to the first station
        max_gap = a[0]
        
        # 2. Gaps between consecutive stations
        for i in range(1, n):
            max_gap = max(max_gap, a[i] - a[i-1])
            
        # 3. Gap from the last station to x and back to the last station
        max_gap = max(max_gap, 2 * (x - a[-1]))
        
        out.append(str(max_gap))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
