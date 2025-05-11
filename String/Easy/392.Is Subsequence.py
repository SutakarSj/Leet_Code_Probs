class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j=0,0
        l=len(t)
        r=len(s)
        while(i<r and j<l):
            if (s[i]==t[j]):
                i+=1
                j+=1
            else:
                j+=1
        if i==r:
            return True
        else:
            return False