import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    n = int(data[0])
    coins = [int(x) for x in data[1:]]
    
    total_sum = sum(coins)
    coins.sort(reverse=True)
    
    my_sum = 0
    coin_count = 0
    
    for coin in coins:
        my_sum += coin
        coin_count += 1
        if my_sum > total_sum / 2:
            break
            
    print(coin_count)

if __name__ == '__main__':
    solve()
