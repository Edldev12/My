import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    for r in range(1, n + 1):
        if r % 2 != 0:
            print("#" * m)
        elif r % 4 == 0:
            print("#" + "." * (m - 1))
        else:
            print("." * (m - 1) + "#")

if __name__ == '__main__':
    solve()
