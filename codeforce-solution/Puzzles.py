def solve():
    n, m = map(int, input().split())
    f = list(map(int, input().split()))
    f.sort()
    min_diff = float('inf')
    for i in range(m - n + 1):
        current_diff = f[i + n - 1] - f[i]
        if current_diff < min_diff:
            min_diff = current_diff
            
    print(min_diff)

if __name__ == "__main__":
    solve()
