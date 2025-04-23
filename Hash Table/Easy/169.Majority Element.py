class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        target=n/2
        s=Counter(nums)
        for i in s:
            if target<nums.count(i):
                return i