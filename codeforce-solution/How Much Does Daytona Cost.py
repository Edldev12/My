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
        k = int(data[idx+1])
        idx += 2
        
        # Read the array slice
        a = [int(x) for x in data[idx : idx + n]]
        idx += n
        
        # k is the most common if we pick a subsegment of length 1 containing just k
        if k in a:
            out.append("YES")
        else:
            out.append("NO")
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
