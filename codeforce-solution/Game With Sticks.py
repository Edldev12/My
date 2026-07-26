import sys

def main():
    # Read n and m from standard input
    n, m = map(int, sys.stdin.readline().split())
    
    # The game always lasts exactly min(n, m) turns
    if min(n, m) % 2 == 1:
        print("Akshat")
    else:
        print("Malvika")

if __name__ == '__main__':
    main()
