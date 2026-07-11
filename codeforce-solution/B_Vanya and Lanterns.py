def solve():
    n, l = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    max_gap = 0
    for i in range(1, n):
        max_gap = max(max_gap, a[i] - a[i-1])
    radius = max(a[0], l - a[n-1], max_gap / 2.0)
    
    print(f"{radius:.10f}")

if __name__ == '__main__':
    solve()
