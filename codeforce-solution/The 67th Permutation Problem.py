def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
        
    t = int(data[0])
    out = []
    
    for k in range(1, t + 1):
        n = int(data[k])
        ans = []
        
        for i in range(n):
            minimum = 1 + i
            median = 3 * n - 1 - 2 * i
            maximum = 3 * n - 2 * i
            ans.extend([minimum, median, maximum])
            
        out.append(" ".join(map(str, ans)))
        
    print("\n".join(out))

if __name__ == '__main__':
    solve()
