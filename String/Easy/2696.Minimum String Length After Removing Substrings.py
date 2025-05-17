class Solution:
    def minLength(self, s: str) -> int:
        u=len(s)
        A,B="AB","CD"
        for i in s:
            if A in s:s=s.replace(A,'')
            elif B in s:s=s.replace(B,'')
        return len(s)