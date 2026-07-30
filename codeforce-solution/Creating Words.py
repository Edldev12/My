import sys

def solve():
    # Read all lines from standard input for fast I/O
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
        
    t = int(input_data[0])
    
    for i in range(1, t + 1):
        a, b = input_data[i].split()
        
        # Swap the first characters using string slicing
        new_a = b[0] + a[1:]
        new_b = a[0] + b[1:]
        
        print(f"{new_a} {new_b}")

if __name__ == '__main__':
    solve()
