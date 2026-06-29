class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note_counts = Counter(ransomNote)
        magazine_counts = Counter(magazine)
        
        for char, count in note_counts.items():
            if magazine_counts[char] < count:
                return False
                
        return True
