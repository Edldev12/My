x=int(input())
y=input()
count=0
for i in range(len(y)-1):
    if y[i]==y[i+1]:
        count+=1
print(count)