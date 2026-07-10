import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    k = int(input_data[1])
    
    time_left = 240 - k
    problems_solved = 0

    for i in range(1, n + 1):
        time_needed = 5 * i
        if time_left >= time_needed:
            time_left -= time_needed
            problems_solved += 1
        else:
            break  
            
    print(problems_solved)

if __name__ == '__main__':
    solve()
