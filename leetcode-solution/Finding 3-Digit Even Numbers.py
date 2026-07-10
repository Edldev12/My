class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        digit_counts = Counter(digits)
        result = []
        
        # Iterate over all possible 3-digit even numbers
        for num in range(100, 1000, 2):
            d1 = num // 100
            d2 = (num // 10) % 10
            d3 = num % 10
            
            # Form a frequency map for the current number's digits
            required_counts = Counter([d1, d2, d3])
            
            # Check if we have enough of each digit available
            if all(digit_counts[d] >= required_counts[d] for d in required_counts):
                result.append(num)
                
        return result
