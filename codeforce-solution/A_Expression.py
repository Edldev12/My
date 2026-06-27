import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    a = int(input_data[0])
    b = int(input_data[1])
    c = int(input_data[2])
    
    ans1 = a + b + c
    ans2 = a * b * c
    ans3 = a + b * c
    ans4 = a * b + c
    ans5 = (a + b) * c
    ans6 = a * (b + c)
    
    # Find the maximum value
    max_val = max(ans1, ans2, ans3, ans4, ans5, ans6)
    
    print(max_val)

if __name__ == '__main__':
    solve()
