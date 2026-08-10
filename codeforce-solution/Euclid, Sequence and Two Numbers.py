import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    t = int(next(iterator))
    out = []
    
    for _ in range(t):
        n = int(next(iterator))
        b = [int(next(iterator)) for _ in range(n)]
        
        # 1. Sort the elements to match the required structural order
        b.sort()
        
        if n == 2:
            out.append(f"{b[1]} {b[0]}")
            continue
            
        # 2. Reverse to reconstruct the potential sequence: a_1, a_2, ..., a_n
        a = b[::-1]
        
        # 3. Verify if it strictly follows Euclid's algorithm relation
        possible = True
        for i in range(2, n):
            if a[i] != a[i-2] % a[i-1]:
                possible = False
                break
                
        if possible:
            out.append(f"{a[0]} {a[1]}")
        else:
            out.append("-1")
            
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == '__main__':
    solve()
