import sys
import math

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    queries = [int(x) for x in input_data[1:]]
    
    LIMIT = 1000000
    is_prime = [True] * (LIMIT + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(math.isqrt(LIMIT)) + 1):
        if is_prime[i]:
            for j in range(i * i, LIMIT + 1, i):
                is_prime[j] = False

    output = []
    for x in queries:
        root = math.isqrt(x)
        if root * root == x and is_prime[root]:
            output.append("YES")
        else:
            output.append("NO")
    print('\n'.join(output))

if __name__ == '__main__':
    solve()
