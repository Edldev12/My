class Solution:
    def reverse(self, x: int) -> int:
        # Define 32-bit signed integer boundaries
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Store the sign and work with the absolute value
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        reversed_num = 0
        while x > 0:
            # Pop the last digit
            digit = x % 10
            x //= 10
            
            # Push the digit to the reversed number
            reversed_num = reversed_num * 10 + digit
            
        # Reapply the sign
        reversed_num *= sign
        
        # Check if the result falls outside 32-bit integer limits
        if reversed_num < INT_MIN or reversed_num > INT_MAX:
            return 0
            
        return reversed_num
