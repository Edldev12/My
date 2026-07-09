class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        even_positions = (n + 1) // 2
        odd_positions = n // 2
        even_combinations = pow(5, even_positions, MOD)
        odd_combinations = pow(4, odd_positions, MOD)
        return (even_combinations * odd_combinations) % MOD
