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
        arr = data[idx + 1 : idx + 1 + n]
        idx += 1 + n
        
        max_streak = 0
        current_streak = 0
        
        for val in arr:
            if val == '0':
                current_streak += 1
            else:
                if current_streak > max_streak:
                    max_streak = current_streak
                current_streak = 0
        
        # Final update after loop ends
        if current_streak > max_streak:
            max_streak = current_streak
            
        out.append(str(max_streak))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
