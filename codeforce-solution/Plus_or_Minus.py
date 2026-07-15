import sys

def solve():
    # Read all input from standard input
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
    
    # The first element is the number of test cases
    t = int(data[0])
    
    results = []
    idx = 1
    for _ in range(t):
        a = int(data[idx])
        b = int(data[idx+1])
        c = int(data[idx+2])
        idx += 3
        
        # Check if addition yields c
        if a + b == c:
            results.append("+")
        else:
            results.append("-")
            
    # Print each result on a new line
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
