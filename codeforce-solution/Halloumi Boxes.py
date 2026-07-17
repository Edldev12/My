import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return

    t = int(data[0])
    idx = 1
    
    out = []
    for _ in range(t):
        n = int(data[idx])
        k = int(data[idx+1])
        idx += 2
        
        # Read the array elements
        a = [int(x) for x in data[idx : idx + n]]
        idx += n
        
        # If k >= 2, we can always sort it using adjacent swaps (like Bubble Sort)
        # If k == 1, we can only sort it if it's already sorted
        if k >= 2:
            out.append("YES")
        else:
            # Check if the array is already sorted
            is_sorted = True
            for i in range(n - 1):
                if a[i] > a[i+1]:
                    is_sorted = False
                    break
            
            if is_sorted:
                out.append("YES")
            else:
                out.append("NO")
                
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
