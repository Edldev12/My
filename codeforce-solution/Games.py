import sys

def solve():
    # Read all inputs from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    
    home = []
    guest = []
    
    # Parse the home and guest uniform colors
    idx = 1
    for _ in range(n):
        home.append(int(input_data[idx]))
        guest.append(int(input_data[idx+1]))
        idx += 2
        
    # Count how many times home[i] matches guest[j]
    count = 0
    for i in range(n):
        for j in range(n):
            if i != j and home[i] == guest[j]:
                count += 1
                
    print(count)

if __name__ == '__main__':
    solve()
