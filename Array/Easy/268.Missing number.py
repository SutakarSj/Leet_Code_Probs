class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        diff = n*(n+1)//2
        actualsum = sum(nums)
        ans = diff - actualsum
        return ans