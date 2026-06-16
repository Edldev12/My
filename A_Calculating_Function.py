x=int(input())
counter=0
if x==0:
    counter=0
else:
    for i in range(1,x+1):
        if i%2==0:
            counter+=i
        else:
            counter-=i
print(counter)