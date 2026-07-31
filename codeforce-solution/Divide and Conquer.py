import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
    
    t = int(data[0])
    results = []
    
    idx = 1
    for _ in range(t):
        x = int(data[idx])
        y = int(data[idx+1])
        idx += 2
        
        if x % y == 0:
            results.append("YES")
        else:
            results.append("NO")
            
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
