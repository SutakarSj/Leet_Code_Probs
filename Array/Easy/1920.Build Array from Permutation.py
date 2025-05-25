class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans,i,n=[],0,len(nums)
        while i<n:
            a=nums[nums[i]]
            ans.append(a)
            i+=1
        return ans