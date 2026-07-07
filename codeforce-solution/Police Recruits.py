import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
    
    n = int(data[0])
    events = [int(x) for x in data[1:]]
    
    police_officers = 0
    untreated_crimes = 0
    
    for event in events:
        if event > 0:
            police_officers += event
        elif event == -1:
            if police_officers > 0:
                police_officers -= 1
            else:
                untreated_crimes += 1
                
    print(untreated_crimes)

if __name__ == '__main__':
    solve()
