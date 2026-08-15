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
        arr = [int(x) for x in data[idx+1 : idx+1+n]]
        idx += 1 + n
        
        A, B, C, D = [], [], [], []
        
        for x in arr:
            if x % 6 == 0:
                A.append(x)
            elif x % 2 == 0:
                B.append(x)
            elif x % 3 == 0:
                C.append(x)
            else:
                D.append(x)
                
        # Combine in the optimal order: A followed by B, then buffer D, then C
        result = A + B + D + C
        out.append(" ".join(map(str, result)))
        
    print("\n".join(out))

if __name__ == '__main__':
    solve()
