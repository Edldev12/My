import sys

def solve():
    # Read all lines from standard input for fast I/O
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
        
    t = int(input_data[0])
    line_idx = 1
    
    for _ in range(t):
        total_points = 0
        
        # Process the 10x10 grid for the current test case
        for r in range(10):
            row = input_data[line_idx + r]
            for c in range(10):
                if row[c] == 'X':
                    # Find distance to closest horizontal and vertical borders
                    dr = min(r, 9 - r)
                    dc = min(c, 9 - c)
                    # The ring level gives the point value (1-indexed)
                    total_points += min(dr, dc) + 1
                    
        print(total_points)
        line_idx += 10

if __name__ == '__main__':
    solve()
