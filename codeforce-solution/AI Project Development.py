import sys
import math

def solve():
    # Read all input from standard input efficiently
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
    
    t = int(data[0])
    results = []
    
    idx = 1
    for _ in range(t):
        n = int(data[idx])
        x = int(data[idx+1])
        y = int(data[idx+2])
        z = int(data[idx+3])
        idx += 4
        
        # Option 1: Without AI
        # Combined speed from the beginning is x + y
        hours_without_ai = (n + (x + y) - 1) // (x + y)
        
        # Option 2: With AI
        # First z hours, only Maxim works at speed x
        lines_during_setup = z * x
        if lines_during_setup >= n:
            # If the project finishes during AI setup
            hours_with_ai = (n + x - 1) // x
        else:
            # Remaining lines after z hours
            remaining_lines = n - lines_during_setup
            # New combined speed after z hours is x + 10*y
            additional_hours = (remaining_lines + (x + 10 * y) - 1) // (x + 10 * y)
            hours_with_ai = z + additional_hours
            
        # Nikita chooses the option that minimizes total full hours
        results.append(str(min(hours_without_ai, hours_with_ai)))
        
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
