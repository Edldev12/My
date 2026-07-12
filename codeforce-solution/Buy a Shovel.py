import sys

def main():
    k, r = map(int, sys.stdin.read().split())   

    for shovels in range(1, 11):
        total_cost = shovels * k
    
        if total_cost % 10 == 0 or total_cost % 10 == r:
            print(shovels)
            break

if __name__ == '__main__':
    main()
