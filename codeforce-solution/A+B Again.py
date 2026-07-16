import sys

def main():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
        
    t = int(data[0])
    results = []
    
    for i in range(1, t + 1):
        n = int(data[i])
        # Calculate sum of tens and ones digit
        digit_sum = (n // 10) + (n % 10)
        results.append(str(digit_sum))
        
    print("\n".join(results))

if __name__ == '__main__':
    main()
