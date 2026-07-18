import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    lengths = [int(input_data[1]), int(input_data[2]), int(input_data[3])]
    
    # Initialize DP array with a very small number representing invalid states
    dp = [-1] * (n + 1)
    dp[0] = 0  # Base case: 0 pieces for 0 length
    
    # Compute the maximum pieces for each length up to n
    for i in range(1, n + 1):
        max_prev = -1
        for l in lengths:
            if i >= l and dp[i - l] != -1:
                max_prev = max(max_prev, dp[i - l])
        
        if max_prev != -1:
            dp[i] = max_prev + 1
            
    print(dp[n])

if __name__ == '__main__':
    solve()

