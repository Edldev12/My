import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    database = {}
    
    output = []
    for i in range(1, n + 1):
        name = data[i]
        if name not in database:
            database[name] = 0
            output.append("OK")
        else:
            database[name] += 1
            output.append(f"{name}{database[name]}")
            
    print('\n'.join(output))

if __name__ == '__main__':
    solve()
