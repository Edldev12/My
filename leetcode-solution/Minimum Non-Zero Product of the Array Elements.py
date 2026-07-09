class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        MOD = 10**9 + 7
        
        max_val = (1 << p) - 1          
        pair_val = max_val - 1         
        num_pairs = (1 << (p - 1)) - 1  
        half_product = pow(pair_val % MOD, num_pairs, MOD)
        
      
        return (half_product * (max_val % MOD)) % MOD
