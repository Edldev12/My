import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
        
    t = int(data[0])
    idx = 1
    
    out = []
    for _ in range(t):
        n = int(data[idx])
        a = [int(x) for x in data[idx + 1 : idx + 1 + n]]
        idx += 1 + n
        
        # Target bitmask representing all bits from 0 to 100*n being set to 1
        # (1 << (100 * n + 1)) - 1 creates a number with exactly 100*n + 1 ones.
        target_mask = (1 << (100 * n + 1)) - 1
        
        # dp stores reachable numbers as set bits. Base case: score 0 is reachable.
        dp = 1
        
        for subtasks in a:
            step = 100 // subtasks
            
            # Step 1: Create a mask of achievable scores for *this problem alone*
            prob_mask = 0
            for score_gain in range(0, 101, step):
                prob_mask |= (1 << score_gain)
            
            # Step 2: Transition the DP using fast bitwise operations
            next_dp = 0
            # Shift the existing DP state by each possible score gain of the current problem
            for score_gain in range(0, 101, step):
                next_dp |= (dp << score_gain)
                
            dp = next_dp
            
        # Check if all bits from 0 to 100*n are set to 1
        if (dp & target_mask) == target_mask:
            out.append("Yes")
        else:
            out.append("No")
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
