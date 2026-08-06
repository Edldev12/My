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
        
        # Read the array of book counts
        a = [int(x) for x in data[idx:idx+n]]
        idx += n
        
        possible = True
        prefix_sum = 0
        
        # Check if each prefix satisfies the minimum requirement
        for i in range(n):
            prefix_sum += a[i]
            # Required sum for first (i+1) stacks is (i+1)*(i+2)//2
            required_sum = (i + 1) * (i + 2) // 2
            
            if prefix_sum < required_sum:
                possible = False
                break
                
        if possible:
            out.append("YES")
        else:
            out.append("NO")
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
