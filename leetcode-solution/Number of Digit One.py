class Solution:
    def countDigitOne(self, n: int) -> int:
        # Step 1: Initialize total count and position multiplier
        total_ones = 0
        i = 1
        
        # Step 2: Loop through every digit position
        while i <= n:
            # Step 3: Extract position components
            left = n // (i * 10)
            curr = (n // i) % 10
            right = n % i
            
            # Step 4: Apply conditional math rules based on curr value
            if curr == 0:
                total_ones += left * i
            elif curr == 1:
                total_ones += (left * i) + (right + 1)
            else:
                total_ones += (left + 1) * i
                
            # Move to the next higher place value (10s, 100s, etc.)
            i *= 10
            
        return total_ones
