import sys

def solve():
    # Read all tokens from standard input efficiently
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    # First token is the number of test cases
    t = int(input_data[0])
    results = []
    
    # Process each pair of (a, b)
    for i in range(t):
        a = int(input_data[2 * i + 1])
        b = int(input_data[2 * i + 2])
        
        # Calculate the absolute difference
        diff = abs(a - b)
        
        # Ceil division of diff by 10
        moves = (diff + 9) // 10
        results.append(str(moves))
        
    # Output all answers separated by newline
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
