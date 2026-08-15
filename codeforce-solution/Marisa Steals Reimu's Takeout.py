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
        w = [int(x) for x in data[idx+1 : idx+1+n]]
        idx += 1 + n
        
        c0 = w.count(0)
        c1 = w.count(1)
        c2 = w.count(2)
        
        # 0s are self-divisible by 3
        # 1 and 2 pair up to make 3
        # Leftover 1s or 2s form triplets (1+1+1=3 or 2+2+2=6)
        ans = c0 + min(c1, c2) + abs(c1 - c2) // 3
        out.append(str(ans))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
