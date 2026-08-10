import sys

def solve():
    # Read all inputs from standard input for fast execution
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    t = int(input_data[0])
    results = []
    
    # Precomputed smallest palindromes for each remainder modulo 12
    # small_pals[rem] gives the smallest palindrome 'a' such that a % 12 == rem
    small_pals = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 22, 11]
    
    for i in range(1, t + 1):
        n = int(input_data[i])
        rem = n % 12
        a = small_pals[rem]
        
        if n >= a:
            results.append(f"{a} {n - a}")
        else:
            # Fallback optimization for very small values of n < 22
            found = False
            for cand_a in range(n + 1):
                if (n - cand_a) % 12 == 0:
                    s = str(cand_a)
                    if s == s[::-1]:
                        results.append(f"{cand_a} {n - cand_a}")
                        found = True
                        break
            if not found:
                results.append("-1")
                
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == '__main__':
    solve()
