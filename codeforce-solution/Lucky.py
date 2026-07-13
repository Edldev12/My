import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
        
    t = int(data[0])
    results = []
    
    for i in range(1, t + 1):
        ticket = data[i]
        
        # Calculate the sum of the first 3 digits
        sum_first = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
        
        # Calculate the sum of the last 3 digits
        sum_last = int(ticket[3]) + int(ticket[4]) + int(ticket[5])
        
        if sum_first == sum_last:
            results.append("YES")
        else:
            results.append("NO")
            
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == '__main__':
    solve()

