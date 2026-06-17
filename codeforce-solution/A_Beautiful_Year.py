y = int(input())
year = y + 1
while True:
    if len(str(year)) == len(set(str(year))):
        print(year)
        break
    year += 1