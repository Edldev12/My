import sys
import bisect

def solve():
    # Read all input from standard input at once
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    # Parse total number of shops
    n = int(input_data[0])
    
    # Slice the prices list and convert to integers
    prices = [int(x) for x in input_data[1:n+1]]
    
    # Sorting takes O(n log n) and prepares array for binary search
    prices.sort()
    
    # Parse total number of queries
    q = int(input_data[n+1])
    
    # Slice the daily budgets
    queries = [int(x) for x in input_data[n+2:n+2+q]]
    
    output = []
    for m in queries:
        # bisect_right finds the count of items less than or equal to m
        count = bisect.bisect_right(prices, m)
        output.append(str(count))
    
    # Write all results to standard output in a single batch
    sys.stdout.write('\n'.join(output) + '\n')

if __name__ == '__main__':
    solve()
