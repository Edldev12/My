import sys

def solve():
    input = sys.stdin.readline
    
    try:
        t_cases = int(input())
    except (IOError, ValueError):
        return

    for _ in range(t_cases):
        n, a, b = map(int, input().split())
        
        # Strategy 1: Buy only individual keys
        only_individuals = n * a
        
        # Strategy 2: Buy only group keys (rounding up for leftovers)
        only_groups = ((n + 2) // 3) * b
        
        # Strategy 3: Maximize full groups of 3, pay individuals for the remainder
        full_groups = n // 3
        remainder = n % 3
        mixed = (full_groups * b) + (remainder * a)
        
        # The best choice is simply the cheapest of the three
        print(min(only_individuals, only_groups, mixed))

if __name__ == '__main__':
    solve()
