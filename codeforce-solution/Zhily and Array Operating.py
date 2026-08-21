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
        
        # Read the array elements as 64-bit integers
        a = [int(x) for x in data[idx : idx + n]]
        idx += n
        
        # Process from right to left
        for i in range(n - 1, 0, -1):
            if a[i] > 0:
                a[i - 1] += a[i]
                
        # Count the remaining positive integers
        count = sum(1 for x in a if x > 0)
        out.append(str(count))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
