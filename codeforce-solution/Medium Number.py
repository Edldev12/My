import sys

def solve():
    # Fast I/O setup
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    t = int(input_data[0])
    results = []
    
    idx = 1
    for _ in range(t):
        # Extract the three distinct numbers
        a = int(input_data[idx])
        b = int(input_data[idx+1])
        c = int(input_data[idx+2])
        idx += 3
        
        # Sort the three numbers to find the middle one
        nums = [a, b, c]
        nums.sort()
        
        results.append(str(nums[1]))
        
    # Output all results efficiently
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
