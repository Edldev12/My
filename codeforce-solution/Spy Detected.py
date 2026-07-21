import sys

def solve():
    # Read all inputs from standard input
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
    
    # First element is the number of test cases
    t = int(data[0])
    idx = 1
    
    out = []
    for _ in range(t):
        n = int(data[idx])
        # Extract the array elements for the current test case
        a = [int(x) for x in data[idx + 1 : idx + 1 + n]]
        idx += 1 + n
        
        # Determine the common value using the first three elements
        if a[0] == a[1]:
            common = a[0]
        elif a[0] == a[2]:
            common = a[0]
        else:
            common = a[1]
            
        # Find the 1-based index of the unique element
        for i in range(n):
            if a[i] != common:
                out.append(str(i + 1))
                break
                
    # Print all outputs separated by a newline
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
