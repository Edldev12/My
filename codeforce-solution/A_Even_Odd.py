n, k = map(int, input().split())
num_odds = (n + 1) // 2
if k <= num_odds:
    print(2 * k - 1)
else:
    print(2 * (k - num_odds))
