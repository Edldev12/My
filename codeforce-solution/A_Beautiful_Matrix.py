matrix = []
for i in range(5):
    matrix.append(list(map(int, input().split())))
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            row = i + 1     
            col = j + 1
moves = abs(row - 3) + abs(col - 3)
print(moves)
