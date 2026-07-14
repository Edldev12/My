class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        MOD = 10**9 + 7
        
        # Base cases for small values
        if primeFactors <= 3:
            return primeFactors
        
        # Scenario 1: Divisible by 3
        if primeFactors % 3 == 0:
            return pow(3, primeFactors // 3, MOD)
            
        # Scenario 2: Leaves a remainder of 1 (combine into a 4, i.e., 2 * 2)
        elif primeFactors % 3 == 1:
            return (4 * pow(3, (primeFactors - 4) // 3, MOD)) % MOD
            
        # Scenario 3: Leaves a remainder of 2 (keep the 2)
        else:
            return (2 * pow(3, (primeFactors - 2) // 3, MOD)) % MOD
