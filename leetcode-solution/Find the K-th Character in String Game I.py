class Solution:
    def kthCharacter(self, k: int) -> str:
        shift_count = bin(k - 1).count('1')
        return chr(ord('a') + shift_count)
