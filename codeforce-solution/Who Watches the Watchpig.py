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
        k = int(data[idx+1])
        s = data[idx+2]
        idx += 3
        
        # If there aren't enough piggies to satisfy the condition
        if n < 2 * k:
            out.append("-1")
            continue
            
        # Count current differences from the optimal target structure
        flips = 0
        for i in range(n):
            # Target structure: first k must be 'R', last k must be 'L'
            if i < k:
                if s[i] != 'R':
                    flips += 1
            elif i >= n - k:
                if s[i] != 'L':
                    flips += 1
            else:
                # Midsection optimal choices: 'R' for first half, 'L' for second half
                # or keeping it matching the existing string to minimize flips.
                # However, any piggy in the middle is already guaranteed safe
                # because they see the first k 'R's and last k 'L's.
                # Thus, midsection piggies require 0 flips.
                pass
                
        out.append(str(flips))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
