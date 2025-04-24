class Solution:
    def reverseString(self, s: List[str]) -> None:
        m = 0
        n = len(s)-1
        while (m<n):
                s[m],s[n]=s[n],s[m]
                m+=1
                n-=1
        return s