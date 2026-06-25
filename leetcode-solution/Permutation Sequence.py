class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # Create a list of numbers to choose from
        numbers = [str(i) for i in range(1, n + 1)]
        
        # Calculate pre-computed factorials for quick lookup
        factorials = [1] * n
        for i in range(1, n):
            factorials[i] = factorials[i - 1] * i
            
        # Convert k to 0-indexed
        k -= 1
        result = []
        
        # Determine digits sequentially from left to right
        for i in range(n - 1, -1, -1):
            idx = k // factorials[i]
            result.append(numbers.pop(idx))
            k %= factorials[i]
            
        return "".join(result)
