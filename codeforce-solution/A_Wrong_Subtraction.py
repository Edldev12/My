x, y=map(int, input().split())
for i in range (0 ,y):
    if x%10==0:
        x//=10
    else:
        x-=1
print(x)
