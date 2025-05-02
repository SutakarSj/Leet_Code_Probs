class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split()
        if (len(set(pattern))==len(set(s))==len(set(zip_longest(pattern,s)))):
            return True 
        return False