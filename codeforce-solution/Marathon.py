import sys

def solve():
    # Read all input from standard input
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
        
    t = int(data[0])
    results = []
    
    idx = 1
    for _ in range(t):
        a = int(data[idx])
        b = int(data[idx+1])
        c = int(data[idx+2])
        d = int(data[idx+3])
        idx += 4
        
        # Count how many participants are strictly ahead of Timur
        count = 0
        if b > a: count += 1
        if c > a: count += 1
        if d > a: count += 1
        
        results.append(str(count))
        
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
