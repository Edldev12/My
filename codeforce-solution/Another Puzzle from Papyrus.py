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
        c = int(next(iterator))
        
        a = [int(next(iterator)) for _ in range(n)]
        b = [int(next(iterator)) for _ in range(n)]
        
        # Strategy 1: Check without reordering
        possible_without_reorder = True
        for i in range(n):
            if a[i] < b[i]:
                possible_without_reorder = False
                break
                
        if possible_without_reorder:
            out.append(str(sum(a) - sum(b)))
            continue
            
        # Strategy 2: Check with one reordering (Sort both arrays)
        sorted_a = sorted(a)
        sorted_b = sorted(b)
        
        possible_with_reorder = True
        for i in range(n):
            if sorted_a[i] < sorted_b[i]:
                possible_with_reorder = False
                break
                
        if possible_with_reorder:
            out.append(str(c + sum(a) - sum(b)))
        else:
            out.append("-1")
            
    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    solve()
