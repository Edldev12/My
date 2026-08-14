import sys

def solve():
    # Read all tokens from standard input efficiently
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    idx = 1
    out = []
    
    for _ in range(t):
        a = int(input_data[idx])
        b = int(input_data[idx+1])
        c = int(input_data[idx+2])
        idx += 3
        
        rounds = 0
        while True:
            # Check condition: if any two players have identical counts, game over
            if a == b or b == c or a == c:
                break
            
            # Sort the player token values to quickly pinpoint min, mid, and max
            tokens = [a, b, c]
            tokens.sort()
            
            # Max player gives exactly 1 token to the Min player
            tokens[2] -= 1
            tokens[0] += 1
            
            # Update variables and increment round counter
            a, b, c = tokens[0], tokens[1], tokens[2]
            rounds += 1
            
        out.append(str(rounds))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
