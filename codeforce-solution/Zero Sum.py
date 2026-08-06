import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    idx = 1
    
    out = []
    for _ in range(t):
        n = int(data[idx])
        a = [int(x) for x in data[idx+1 : idx+1+n]]
        idx += 1 + n
        
        total_sum = sum(a)
        if total_sum % 4 == 0:
            out.append("YES")
        else:
            out.append("NO")
            
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
