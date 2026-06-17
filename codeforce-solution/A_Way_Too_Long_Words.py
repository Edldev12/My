t=int(input())

for i in range(t):
    x = input()
    count=0
    if len(x)>10:

        print(x[0]+str(len(x) - 2)+x[len(x)-1])
    else:
        print(x)
