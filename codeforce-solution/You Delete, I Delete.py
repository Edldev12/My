import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
        
    t = int(data[0])
    out = []
    
    for case_idx in range(1, t + 1):
        s = data[case_idx]
        
        # --- ALICE'S TURN ---
        # Alice wants to maximize the string.
        # She should look for the first '0' that is immediately followed by a '1' 
        # to expose the '1' earlier. If none exists, she just deletes the last '0'.
        alice_del_idx = -1
        for i in range(len(s)):
            if s[i] == '0':
                alice_del_idx = i
                # If it's a 0 followed by a 1, this is the best spot to maximize
                if i + 1 < len(s) and s[i+1] == '1':
                    break
                    
        # Construct the string after Alice's deletion
        s_after_alice = s[:alice_del_idx] + s[alice_del_idx + 1:]
        
        # --- BOB'S TURN ---
        # Bob wants to minimize the string.
        # He should look for the first '1' that is immediately followed by a '0' 
        # to expose the '0' earlier. If none exists, he just deletes the last '1'.
        bob_del_idx = -1
        for i in range(len(s_after_alice)):
            if s_after_alice[i] == '1':
                bob_del_idx = i
                # If it's a 1 followed by a 0, this is the best spot to minimize
                if i + 1 < len(s_after_alice) and s_after_alice[i+1] == '0':
                    break
                    
        # Construct final string
        final_str = s_after_alice[:bob_del_idx] + s_after_alice[bob_del_idx + 1:]
        out.append(final_str)
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
