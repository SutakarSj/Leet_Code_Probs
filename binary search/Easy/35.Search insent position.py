class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #binary search
        n=len(nums)
        l,r=0,n-1
        while l <= r:
            m = (l+r) // 2 
            if nums[m] > target:
                r = m-1
            elif nums[m] < target:
                l = m+1
            else:
                return m
        if nums[m] < target:
            return m + 1
        elif nums[m] > target:
            return m