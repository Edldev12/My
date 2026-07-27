no = int(input())
pairs = []

for _ in range(no):
    a, b = map(int, input().split())
    pairs.append((a, b))

for a, b in pairs:
    print(b - a)
