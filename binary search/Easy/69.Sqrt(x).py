class Solution:
    def mySqrt(self, x: int) -> int:
        l,r=1,x
        while l<=r:
            mid=(l+r)//2
            m=mid*mid
            if m==x:
                return mid
            elif m<x:
                l=mid+1
            else:
                r=mid-1
        return r