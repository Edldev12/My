def solve():
    n = int(input())
    cards = list(map(int, input().split()))
    
    left = 0
    right = n - 1
    
    sereja_score = 0
    dima_score = 0
    sereja_turn = True
    
    while left <= right:
        if cards[left] > cards[right]:
            chosen_card = cards[left]
            left += 1
        else:
            chosen_card = cards[right]
            right -= 1
        if sereja_turn:
            sereja_score += chosen_card
        else:
            dima_score += chosen_card
            
        sereja_turn = not sereja_turn
        
    print(sereja_score, dima_score)

if __name__ == '__main__':
    solve()
