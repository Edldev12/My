x = input()
count = []
i = 0
while i <len(x):
    if x[i] == ".":
        count.append(0)
        i += 1
    elif x[i] == "-":
        if x[i + 1] == ".":
            count.append(1)
        elif x[i + 1] == "-":
            count.append(2)
        else:
            print("invalid")
        i += 2
    else:
        print("invalid")
result = "".join(map(str, count))
print(result)
