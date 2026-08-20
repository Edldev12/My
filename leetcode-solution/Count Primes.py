class Solution:
    def countPrimes(self, n: int) -> int:
        # Base case: there are no primes strictly less than 2
        if n <= 2:
            return 0
        
        # Initialize a boolean array tracking primality
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        
        # Sieve process: loop up to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                # Mark multiples of i starting from i*i as False
                is_prime[i*i : n : i] = [False] * len(range(i*i, n, i))
                
        # The sum of True values equals the total count of primes
        return sum(is_prime)
