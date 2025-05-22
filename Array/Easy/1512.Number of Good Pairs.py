class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good_pairs=[]
        for i in range (len(nums)):
            for j in range(len(nums)):
                if nums[i]==nums[j] and i<j: 
                    k = (i,j)
                    good_pairs.append(k)
                    continue 
        return len(good_pairs)