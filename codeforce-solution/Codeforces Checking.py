import sys

def solve():
    # Read all inputs efficiently from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    t = int(input_data[0])
    # Use a set for O(1) lookups
    target_letters = set("codeforces")
    
    # Process each character test case
    for i in range(1, t + 1):
        c = input_data[i]
        if c in target_letters:
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve()
