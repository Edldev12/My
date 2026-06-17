x=int(input())
y=list(str(input()))
a=0
b=0
for i in y:
    if i=='A':
        a+=1
    else:
        b+=1
if a>b:
    print("Anton")
elif a<b:
    print("Danik")
else:
    print("Friendship")
