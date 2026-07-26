import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    t = int(input_data[0])
    results = []
    
    # Process each test case using index tracking
    idx = 1
    for _ in range(t):
        a = int(input_data[idx])
        b = int(input_data[idx+1])
        c = int(input_data[idx+2])
        idx += 3
        
        # Check if the sum of the two largest numbers is >= 10
        if (a + b + c - min(a, b, c)) >= 10:
            results.append("YES")
        else:
            results.append("NO")
            
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
