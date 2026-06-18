import sys
def solve():
    n = int(sys.stdin.read().strip())
    lucky_numbers = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]
    for lucky in lucky_numbers:
        if n % lucky == 0:
            print("YES")
            return        
    print("NO")
if __name__ == '__main__':
    solve()
