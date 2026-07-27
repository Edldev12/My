no = int(input())
pairs = []

for _ in range(no):
    a = int(input()) # FIX 1: Convert the input string to an integer
    pairs.append(a)

for a in pairs:
    count_1 = 0 # FIX 2: Reset counter 1 for each test case
    count_2 = 0 # FIX 2: Reset counter 2 for each test case
    possible = True
    
    while a != 1:
        if a % 6 == 0:
            a = a // 6
            count_1 += 1
        elif a % 3 == 0: # FIX 3: Only multiply by 2 if the number is still a multiple of 3
            a = a * 2
            count_2 += 1
        else: # FIX 3: If it's not divisible by 6 or 3, it's impossible to reach 1
            possible = False
            break
            
    if possible:
        print(count_1 + count_2)
    else:
        print(-1)
