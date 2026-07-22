import sys

def solve():
    # Read the number of test cases
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    results = []
    
    # Process each test case
    idx = 1
    for _ in range(t):
        a = int(data[idx])
        b = int(data[idx+1])
        c = int(data[idx+2])
        idx += 3
        
        # XOR cancels out the two equal numbers
        odd_one = a ^ b ^ c
        results.append(str(odd_one))
        
    # Print all results separated by a newline
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
