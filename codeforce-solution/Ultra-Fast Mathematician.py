line1 = input().strip()
line2 = input().strip()
result = "".join("1" if c1 != c2 else "0" for c1, c2 in zip(line1, line2))
print(result)
