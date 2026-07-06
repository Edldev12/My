import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    s = int(data[0])
    n = int(data[1])
    
    dragons = []
    index = 2
    for _ in range(n):
        x = int(data[index])
        y = int(data[index+1])
        dragons.append((x, y))
        index += 2
        
    dragons.sort(key=lambda d: d[0])
    
    for x, y in dragons:
        if s > x:
            s += y
        else:
            print("NO")
            return
            
    print("YES")

if __name__ == '__main__':
    solve()
