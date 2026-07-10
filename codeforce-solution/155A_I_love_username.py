import sys

def solve():
    data = sys.stdin.read().split()
    
    if not data:
        return
        
    n = int(data[0])
    scores = [int(x) for x in data[1:n+1]]
    
    current_min = scores[0]
    current_max = scores[0]
    amazing_count = 0
    for score in scores[1:]:
        if score > current_max:
            amazing_count += 1
            current_max = score  
        elif score < current_min:
            amazing_count += 1
            current_min = score  
            
    print(amazing_count)

if __name__ == '__main__':
    solve()
