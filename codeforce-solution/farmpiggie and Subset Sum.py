import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
        
    t = int(data[0])
    results = []
    
    for i in range(1, t + 1):
        n = int(data[i])
        # Generate pairs (2, 1), (4, 3), (6, 5)... up to n
        permutation = []
        for j in range(1, n, 2):
            permutation.append(str(j + 1))
            permutation.append(str(j))
        
        results.append(" ".join(permutation))
        
    print("\n".join(results))

if __name__ == '__main__':
    solve()
