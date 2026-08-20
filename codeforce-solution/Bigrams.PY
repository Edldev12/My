import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    idx = 1
    
    out = []
    for _ in range(t):
        k = int(input_data[idx])
        c = [int(x) for x in input_data[idx+1 : idx+1+k]]
        idx += 1 + k
        
        # Count how many characters have at least 2 cards
        ge_2_count = 0
        has_ge_3 = False
        
        for count in c:
            if count >= 3:
                has_ge_3 = True
            if count >= 2:
                ge_2_count += 1
                
        # Condition 1: A single letter appears 3 or more times (e.g., aaa -> aa, aa)
        # Condition 2: At least two different letters appear 2 or more times (e.g., aabb -> ab occurs once, but abab -> ab, ab)
        if has_ge_3 or ge_2_count >= 2:
            out.append("YES")
        else:
            out.append("NO")
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
