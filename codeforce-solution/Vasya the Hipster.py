import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    a = int(input_data[0])
    b = int(input_data[1])
    
    diff_days = min(a, b)
    same_days = abs(a - b) // 2
    
    print(f"{diff_days} {same_days}")

if __name__ == '__main__':
    main()
