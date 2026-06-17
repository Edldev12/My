n = int(input())
groups = 1
prev = input()
for _ in range(n - 1):
    current = input()
    if current != prev:
        groups += 1
    prev = current
print(groups)