import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
        
    t = int(data[0])
    idx = 1
    
    results = []
    for _ in range(t):
        k = int(data[idx])
        counts = [int(x) for x in data[idx+1 : idx+1+k]]
        idx += 1 + k
        
        # Count how many characters appear 2 or more times
        twos_or_more = 0
        has_three_or_more = False
        
        for c in counts:
            if c >= 3:
                has_three_or_more = True
            if c >= 2:
                twos_or_more += 1
                
        # Condition check
        if has_three_or_more or twos_or_more >= 2:
            results.append("YES")
        else:
            results.append("NO")
            
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
