class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Compare structural index patterns using Python's map function
        return list(map(s.find, s)) == list(map(t.find, t))
