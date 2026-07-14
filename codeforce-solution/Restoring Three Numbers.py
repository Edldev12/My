import sys

def solve():
    # Read the 4 integers
    nums = list(map(int, sys.stdin.readline().split()))
    
    # Sort the list to find the total sum at the last position
    nums.sort()
    
    # Calculate each element
    a = nums[3] - nums[0]
    b = nums[3] - nums[1]
    c = nums[3] - nums[2]
    
    print(a, b, c)

if __name__ == '__main__':
    solve()
