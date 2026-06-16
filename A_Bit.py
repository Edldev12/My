X=0
y=int(input())
for i in range(y):
    z=input()
    if z=="++X":
        X+=1
    elif z=="X++":
        X+=1
    elif z=="X--":
        X-=1
    else:
        X-=1
   
print(X)

