class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l,r=0,1
        for i in range(len(nums)-1):
            if nums[l]==0 and nums[r]!=0 and r<len(nums):
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                r+=1
            elif nums[l]!=0 and r<len(nums):
                l+=1
                r+=1
            elif nums[l]==0 and nums[r]==0 and r<len(nums):
                r+=1
        return nums