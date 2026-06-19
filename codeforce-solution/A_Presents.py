n = int(input())
giver = list(map(int, input().split()))
ans = [0] * (n + 1)
for i in range(n):
    # i + 1 is the giver, giver[i] is the receiver
    ans[giver[i]] = i + 1
print(*(ans[1:]))
