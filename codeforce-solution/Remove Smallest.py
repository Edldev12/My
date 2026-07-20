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
        # Slice the next n elements for the current test case array
        a = [int(x) for x in data[idx + 1 : idx + 1 + n]]
        idx += 1 + n
        
        # Step 1: Sort the array
        a.sort()
        
        # Step 2: Check adjacent gaps
        possible = True
        for i in range(n - 1):
            if a[i + 1] - a[i] > 1:
                possible = False
                break
        
        if possible:
            out.append("YES")
        else:
            out.append("NO")
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
