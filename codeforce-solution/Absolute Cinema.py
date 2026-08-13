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
        idx += 1
        
        a = [int(x) for x in data[idx : idx + n]]
        idx += n
        
        b = [int(x) for x in data[idx : idx + n]]
        idx += n
        
        x = [0] * n
        y = [0] * n
        sum_y = 0
        
        for i in range(n):
            if a[i] < b[i]:
                x[i] = a[i]
                y[i] = b[i]
            else:
                x[i] = b[i]
                y[i] = a[i]
            sum_y += y[i]
            
        # Build prefix maximums for array x
        pref_max = [0] * n
        curr_max = 0
        for i in range(n):
            pref_max[i] = curr_max
            if x[i] > curr_max:
                curr_max = x[i]
                
        # Build suffix maximums for array x
        suff_max = [0] * n
        curr_max = 0
        for i in range(n - 1, -1, -1):
            suff_max[i] = curr_max
            if x[i] > curr_max:
                curr_max = x[i]
                
        # Find the maximum valid x_k
        max_xk = 0
        for k in range(n):
            max_other_x = pref_max[k] if pref_max[k] > suff_max[k] else suff_max[k]
            if y[k] >= max_other_x:
                if x[k] > max_xk:
                    max_xk = x[k]
                    
        out.append(str(sum_y + max_xk))
        
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    solve()
