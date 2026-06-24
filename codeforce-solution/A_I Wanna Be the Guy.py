def solve():
    n = int(input())
    
    # Read Little X's line, ignore the first number (p), and take the rest
    x_input = list(map(int, input().split()))
    x_levels = x_input[1:] if x_input[0] > 0 else []
    
    # Read Little Y's line, ignore the first number (q), and take the rest
    y_input = list(map(int, input().split()))
    y_levels = y_input[1:] if y_input[0] > 0 else []
    
    # Combine both lists into a set to find all unique levels they can clear
    combined_levels = set(x_levels + y_levels)
    
    # If the number of unique clearable levels equals n, they pass the game
    if len(combined_levels) == n:
        print("I become the guy.")
    else:
        print("Oh, my keyboard!")

if __name__ == "__main__":
    solve()
