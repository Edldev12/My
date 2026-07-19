import sys

def solve():
    # Read all inputs from standard input at once
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    m = int(input_data[1])
    tasks = [int(x) for x in input_data[2:]]
    
    current = 1
    total_time = 0
    
    for next_task in tasks:
        if next_task >= current:
            total_time += (next_task - current)
        else:
            total_time += (n - current + next_task)
        current = next_task
        
    print(total_time)

if __name__ == '__main__':
    solve()
