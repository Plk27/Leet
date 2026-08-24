class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Quick optimization: if ransomNote is longer, it's impossible
        if len(ransomNote) > len(magazine):
            return False
            
        # Count character frequencies in the magazine
        char_counts = {}
        for char in magazine:
            char_counts[char] = char_counts.get(char, 0) + 1
            
        # Consume characters for the ransom note
        for char in ransomNote:
            # If character doesn't exist or is fully used up
            if char not in char_counts or char_counts[char] == 0:
                return False
            char_counts[char] -= 1
            
        return True
