import sys

def solve():
    # Read all input from standard input efficiently
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    results = []
    
    # Process each test case
    for i in range(1, t + 1):
        n = int(input_data[i])
        total_triples = 0
        
        # Calculate the sum of (n // b) ** 2 for all b from 1 to n
        for b in range(1, n + 1):
            count = n // b
            total_triples += count * count
            
        results.append(str(total_triples))
    
    # Print all answers separated by newline
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == '__main__':
    solve()
