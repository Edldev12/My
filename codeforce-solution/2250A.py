import sys

def solve():
    # Read all inputs from standard input efficiently
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    t = int(input_data[0])
    idx = 1
    
    out = []
    for _ in range(t):
        n = int(input_data[idx])
        w = [int(x) for x in input_data[idx+1 : idx+1+n]]
        idx += 1 + n
        
        # If n is odd, it is mathematically impossible to fill all slots
        if n % 2 != 0:
            out.append("NO")
            continue
            
        max_even_pos = float('-inf')  # Maximum of elements that must move Left (2nd, 4th...)
        min_odd_pos = float('inf')    # Minimum of elements that must move Right (1st, 3rd...)
        
        for i in range(n):
            if i % 2 == 0:  # 0-indexed even is 1-indexed odd position (1st, 3rd, 5th...)
                min_odd_pos = min(min_odd_pos, w[i])
            else:           # 0-indexed odd is 1-indexed even position (2nd, 4th, 6th...)
                max_even_pos = max(max_even_pos, w[i])
        
        # We need an integer k such that max_even_pos < k < min_odd_pos
        if max_even_pos + 1 < min_odd_pos:
            out.append("YES")
        else:
            out.append("NO")

    # Print all answers separated by newline
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
