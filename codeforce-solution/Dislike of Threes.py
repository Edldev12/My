import sys

def solve():
    # Precompute the sequence of liked numbers up to k = 1000
    liked_numbers = []
    num = 1
    
    while len(liked_numbers) < 1000:
        if num % 3 != 0 and num % 10 != 3:
            liked_numbers.append(num)
        num += 1

    # Read all input from standard input
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
        
    t = int(data[0])
    results = []
    
    # Process each test case k
    for i in range(1, t + 1):
        k = int(data[i])
        # k is 1-indexed, so we access k-1 in our 0-indexed list
        results.append(str(liked_numbers[k - 1]))
        
    # Print all answers separated by newline
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
