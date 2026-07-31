import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
    
    t = int(data[0])
    results = []
    
    idx = 1
    for _ in range(t):
        n = int(data[idx])
        k = int(data[idx+1])
        idx += 2
        
        total_popcount = 0
        bit_val = 1
        
        while n > 0 and bit_val <= n:
            # Maximum bits we can take at this power of 2
            take = min(k, n // bit_val)
            total_popcount += take
            n -= take * bit_val
            bit_val *= 2 # Move to the next bit position
            
        results.append(str(total_popcount))
        
    print('\n'.join(results))

if __name__ == '__main__':
    solve()
