import sys

def solve():
    # Read all tokens from standard input efficiently
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    idx = 1
    out = []
    
    for _ in range(t):
        b1 = int(input_data[idx])
        b2 = int(input_data[idx+1])
        b3 = int(input_data[idx+2])
        idx += 3
        
        # 1. Sort the three blackboard numbers so x <= y <= z
        blackboard = [b1, b2, b3]
        blackboard.sort()
        x, y, z = blackboard
        
        # 2. The mathematical formula derived from the editorial
        ans = min(z - x, y)
        out.append(str(ans))
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
