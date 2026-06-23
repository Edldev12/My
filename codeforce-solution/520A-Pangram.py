n = int(input())
s = input().lower()
unique_chars = set(s)
if len(unique_chars) == 26:
    print("YES")
else:
    print("NO")
