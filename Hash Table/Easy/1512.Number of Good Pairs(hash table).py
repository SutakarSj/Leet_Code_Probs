class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good_pair=0
        count=defaultdict(int)
        for i in nums:
            good_pair += count[i]
            count[i] += 1
        
        return good_pair