class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        target=n/2
        s=Counter(nums)
        for i in s:
            if target<nums.count(i):
                return i
                
#without inbuilt function
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash={}
        for i in nums:
            if i in hash:
                hash[i]+=1
            else:
                hash[i]=1   

        for j in hash:
            if hash[j]>len(nums)//2:
                return j   
        return -1
