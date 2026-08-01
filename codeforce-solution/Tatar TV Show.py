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
        s = data[idx+2]
        idx += 3
        
        # Track the count of '1's for each remainder index modulo k
        counts = [0] * k
        for i, char in enumerate(s):
            if char == '1':
                counts[i % k] += 1
        
        # Check if all remainder buckets have an even number of '1's
        possible = True
        for count in counts:
            if count % 2 != 0:
                possible = False
                break
                
        if possible:
            out.append("YES")
        else:
            out.append("NO")
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
