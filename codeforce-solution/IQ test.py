n = int(input())
numbers = list(map(int, input().split()))
evens = []
odds = []
for i in range(n):
    if numbers[i] % 2 == 0:
        evens.append(i + 1)
    else:
        odds.append(i + 1)
if len(evens) == 1:
    print(evens[0])
else:
    print(odds[0])
