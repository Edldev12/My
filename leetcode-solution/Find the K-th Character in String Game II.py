class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        
        k -= 1
        shifts = 0
        
        # Traverse operations backwards from the final state
        # Each operation i corresponds to a length of 2^i before it occurs
        for i in range(len(operations) - 1, -1, -1):
            length = 1 << i  # This is 2^i
            
            # If k is in the appended second half
            if k >= length:
                # If the operation shifts characters, increment our shift count
                if operations[i] == 1:
                    shifts += 1
                # Map k back to its equivalent position in the first half
                k -= length
                
        # Calculate the final character relative to 'a'
        return chr(ord('a') + (shifts % 26))
