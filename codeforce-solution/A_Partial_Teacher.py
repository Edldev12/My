n = int(input())
s = input()
a = [1] * n
for i in range(n - 1):
    if s[i] == 'R':
        a[i + 1] = a[i] + 1
    elif s[i] == '=':
        a[i + 1] = a[i]
for i in range(n - 2, -1, -1):
    if s[i] == 'L':
        a[i] = max(a[i], a[i + 1] + 1)
    elif s[i] == '=':
        a[i] = a[i + 1]

print(*a)