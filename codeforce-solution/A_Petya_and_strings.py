x=input()
y=input()
count=0
x=x.lower()
y=y.lower()
if x==y:
    count=0
else:
    if x<y:
        count=-1
    else:
        count=1
print(count)
