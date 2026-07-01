import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    results = []
    
    for i in range(1, t + 1):
        n_str = data[i]
        round_numbers = []
        power = 1
        
        # Traverse the string representation from right to left
        for digit in reversed(n_str):
            if digit != '0':
                round_numbers.append(int(digit) * power)
            power *= 10
            
        results.append(f"{len(round_numbers)}\n" + " ".join(map(str, round_numbers)))
        
    print("\n".join(results))

if __name__ == '__main__':
    solve()
