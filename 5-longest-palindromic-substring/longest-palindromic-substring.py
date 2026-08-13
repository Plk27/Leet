class Solution:
    def longestPalindrome(self, s: str) -> str:

        if not s:
            return ""
        
        start=0
        maxlen=0

        def palength(left: int, right: int) -> int:
            while(left>=0 and right<len(s) and s[left]==s[right]):
                left-=1
                right+=1
            return right-left-1

        for i in range(len(s)):
            len1 = palength(i,i)
            len2 = palength(i, i+1)
            currentlen = max(len1,len2)

            if currentlen > maxlen:
                maxlen = currentlen
                start = i- (currentlen-1)//2
        
        return s[start: start+maxlen]
            

        