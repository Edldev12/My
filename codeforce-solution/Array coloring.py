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
        idx += 1
        
        # Read the array elements for the current test case
        a = [int(x) for x in data[idx:idx+n]]
        idx += n
        
        # Check if the total sum of the array is even
        if sum(a) % 2 == 0:
            out.append("YES")
        else:
            out.append("NO")
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
