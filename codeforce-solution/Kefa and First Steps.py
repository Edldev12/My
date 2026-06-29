import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    a = [int(x) for x in input_data[1:]]
    
    max_len = 1
    current_len = 1
    
    for i in range(1, n):
        if a[i] >= a[i-1]:
            current_len += 1
        else:
            current_len = 1
            
        if current_len > max_len:
            max_len = current_len
            
    print(max_len)

if __name__ == '__main__':
    solve()
