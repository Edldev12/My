x=list(input())
t=0
for i in range(len(x)-1):
    if x[i]==x[i+1]:
        t+=1
        if t>=6:
            break
    else:
        t=0
if t>=6:
    print("YES")
else:
    print("NO")
