import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
        
    t = int(data[0])
    
    for i in range(1, t + 1):
        s = data[i]
        if s.upper() == "YES":
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()
