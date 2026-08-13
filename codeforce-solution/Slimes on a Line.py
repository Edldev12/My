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
        # Read the n array elements for the current test case
        a = [int(x) for x in data[idx + 1 : idx + 1 + n]]
        idx += 1 + n
        
        # Calculate the span between the maximum and minimum elements
        span = max(a) - min(a)
        
        # Ceil division of span by 2
        ans = (span + 1) // 2
        out.append(str(ans))
        
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    solve()
