import sys
from collections import Counter

def solve():
    # Read all input from standard input efficiently
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    # Count the occurrences of each group size (1, 2, 3, 4)
    counts = Counter(map(int, input_data[1:]))
    
    # 1. Groups of 4 always get their own taxi
    taxis = counts[4]
    
    # 2. Groups of 3 get their own taxi and take one group of 1 along if available
    taxis += counts[3]
    counts[1] = max(0, counts[1] - counts[3])
    
    # 3. Pair groups of 2 together
    taxis += counts[2] // 2
    leftover_2 = counts[2] % 2
    
    # 4. Handle a leftover group of 2
    if leftover_2:
        taxis += 1
        # A leftover group of 2 leaves 2 empty spaces for up to two groups of 1
        counts[1] = max(0, counts[1] - 2)
        
    # 5. Put any remaining groups of 1 into taxis (4 per taxi)
    if counts[1] > 0:
        taxis += (counts[1] + 3) // 4  # Ceiling division
        
    print(taxis)

if __name__ == '__main__':
    solve()
