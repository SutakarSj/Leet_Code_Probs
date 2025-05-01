class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_cnt=defaultdict(int)
        pair_cnt=defaultdict(int)
        for i in range(len(nums)):
            for j  in range(i+1,len(nums)):
                product=nums[i]*nums[j]
                product_cnt[product]+=1
        res=0
        for k in product_cnt.values():
            pairs=(k*(k-1))//2
            res+=8*pairs
        return res