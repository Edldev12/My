def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return

    t = int(data[0])
    idx = 1
    
    out = []
    for _ in range(t):
        n = int(data[idx])
        a = [int(x) for x in data[idx+1 : idx+1+n]]
        idx += 1 + n
        
        # Check for duplicates
        if len(a) != len(set(a)):
            out.append("-1")
        else:
            # Sort in descending order
            a.sort(reverse=True)
            out.append(" ".join(map(str, a)))
            
    print("\n".join(out))

if __name__ == '__main__':
    solve()
