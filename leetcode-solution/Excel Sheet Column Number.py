class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for char in columnTitle:
            # Shift base 26 and add current character's value (A=1, B=2, ...)
            ans = ans * 26 + (ord(char) - ord('A') + 1)
        return ans
