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
        s = data[idx + 1]
        idx += 2
        
        # Split string by '*' to isolate continuous '#' segments
        segments = s.split('*')
        
        max_time = 0
        for segment in segments:
            L = len(segment)
            if L > 0:
                # Math formula equivalent to ceil(L / 2)
                time_taken = (L + 1) // 2
                if time_taken > max_time:
                    max_time = time_taken
                    
        out.append(str(max_time))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
