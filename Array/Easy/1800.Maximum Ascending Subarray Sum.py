class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxi=0
        n=len(nums)
        current=nums[0]
        for i in range(1,n):
            if nums[i-1]<nums[i]:
                current+=nums[i]
            else:
                maxi=max(maxi,current)
                current=nums[i]
        return max(maxi,current)