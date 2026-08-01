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
        
        # Read the tower heights for the current test case
        a = [int(x) for x in data[idx:idx+n]]
        idx += n
        
        total_sum = 0
        current_min = float('inf')
        
        # Track the running prefix minimum
        for height in a:
            if height < current_min:
                current_min = height
            total_sum += current_min
            
        out.append(str(total_sum))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
