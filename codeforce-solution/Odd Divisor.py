import sys

def solve():
    # Read all lines from standard input efficiently
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
        
    t = int(data[0])
    results = []
    
    for i in range(1, t + 1):
        n = int(data[i])
        # A number is a power of 2 if (n & (n - 1)) == 0
        if (n & (n - 1)) == 0:
            results.append("NO")
        else:
            results.append("YES")
            
    # Print all results separated by a newline
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == '__main__':
    solve()
