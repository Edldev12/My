x, y, z=map(int, input().split())
total=x*z*(z+1)//2
if total>y:
    print(total-y)
else:
    print(0)
