import sys
def solve():
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
        idx += 2
        rem = a % b
        if rem == 0:
            results.append("0")
        else:
            results.append(str(b - rem))
            
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
