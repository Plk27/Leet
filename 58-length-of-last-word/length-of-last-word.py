class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        # Start at the valid last index
        i = len(s) - 1 
        
        # Step 1: Skip all trailing spaces
        while i >= 0 and s[i] == " ":
            i -= 1
            
        # Step 2: Count characters of the actual last word
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
            
        return length
