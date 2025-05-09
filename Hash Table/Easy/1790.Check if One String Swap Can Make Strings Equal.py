class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1==s2:return True
        mismatch=[(a,b) for a,b in zip(s1,s2) if a!=b]
        if len(mismatch)==2 and mismatch[0]==mismatch[1][::-1]:return True
        return False