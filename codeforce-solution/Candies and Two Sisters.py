import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    t = int(data[0])
    results = []
    
    for i in range(1, t + 1):
        n = int(data[i])
        # Integer division automatically floors the result
        results.append(str((n - 1) // 2))
        
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
