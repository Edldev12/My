colors = map(int, input().split())
unique_colors = set(colors)
print(4 - len(unique_colors))
