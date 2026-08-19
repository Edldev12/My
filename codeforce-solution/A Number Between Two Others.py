import sys

def solve():
    # Fast I/O
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    t = int(data[0])
    results = []
    
    # Process each test case
    idx = 1
    for _ in range(t):
        x = int(data[idx])
        y = int(data[idx+1])
        idx += 2
        
        # Check if k = y / x is greater than or equal to 3
        if y // x >= 3:
            results.append("YES")
        else:
            results.append("NO")
            
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
