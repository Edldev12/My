class Solution:
    def trailingZeroes(self, n: int) -> bool:
        zeros = 0
        
        while n > 0:
            n //= 5      # Integer division by 5
            zeros += n   # Add the count of multiples
            
        return zeros
