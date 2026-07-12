class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        available = Counter(digits)
        unique_even_count = 0

        for num in range(100, 1000, 2):
           
            d1, d2, d3 = num // 100, (num // 10) % 10, num % 10
            required = Counter([d1, d2, d3])
            
            if all(available[digit] >= count for digit, count in required.items()):
                unique_even_count += 1
                
        return unique_even_count
