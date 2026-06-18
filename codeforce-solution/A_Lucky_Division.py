
import sys

def solve():
    # Read the integer input
    n = int(sys.stdin.read().strip())
    
    # List of all lucky numbers up to 1000
    lucky_numbers = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]
    
    # Check if n is divisible by any lucky number
    for lucky in lucky_numbers:
        if n % lucky == 0:
            print("YES")
            return
            
    print("NO")

if __name__ == '__main__':
    solve()
