import sys

def solve():
    # Fast I/O standard for competitive programming
    input = sys.stdin.readline
    
    # Read the number of test cases
    try:
        t_cases = int(input())
    except (IOError, ValueError):
        return

    for _ in range(t_cases):
        n = int(input())
        
        arr = []
        num = 1
        
        # Keep picking numbers until our array is full
        while len(arr) < n:
            # Skip any multiples of 3 to split sums vs elements mod 3
            if num % 3 != 0:
                arr.append(num)
            num += 1
            
        # Print the final result space-separated
        print(*arr)

if __name__ == '__main__':
    solve()
