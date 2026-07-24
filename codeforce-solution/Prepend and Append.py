import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    idx = 1
    
    out = []
    for _ in range(t):
        n = int(data[idx])
        s = data[idx+1]
        idx += 2
        
        l, r = 0, n - 1
        while l < r and s[l] != s[r]:
            l += 1
            r -= 1
            
        out.append(str(r - l + 1))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
