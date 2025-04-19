class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        strs= Counter(s)
        strt = Counter(t)
        if strs == strt:
            return True 
        return False