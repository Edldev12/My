import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    k = int(input_data[1])
    l = int(input_data[2])
    c = int(input_data[3])
    d = int(input_data[4])
    p = int(input_data[5])
    nl = int(input_data[6])
    np = int(input_data[7])
    total_drink_toasts = (k * l) // nl
    total_lime_toasts = c * d
    total_salt_toasts = p // np
    max_total_toasts = min(total_drink_toasts, total_lime_toasts, total_salt_toasts)
    
    toasts_per_friend = max_total_toasts // n
    
    print(toasts_per_friend)

if __name__ == '__main__':
    solve()
