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
        
        # If there's only 1 element, it can never stay in the range [1, n]
        if n == 1:
            out.append("NO")
            continue
            
        # Elements at index 0 (position 1) must move right -> w[0] > k
        # Thus, odd positions (1-based) move right, even positions move left.
        max_left = -1
        min_right = float('inf')
        
        for i in range(n):
            if i % 2 == 0:
                # 1-based odd position: moves right -> w[i] > k
                min_right = min(min_right, w[i])
            else:
                # 1-based even position: moves left -> w[i] < k
                max_left = max(max_left, w[i])
        
        # We need an integer k such that max_left < k < min_right
        # This requires at least one integer to fit strictly between them.
        if max_left + 1 <= min_right - 1:
            out.append("YES")
        else:
            out.append("NO")
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
