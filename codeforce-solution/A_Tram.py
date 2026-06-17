n=int(input())
count=0
z=0
for _ in range(n):
    x, y=map(int, input().split())
    count-= x 
    count+= y
    z=max(z, count)
print(z)

