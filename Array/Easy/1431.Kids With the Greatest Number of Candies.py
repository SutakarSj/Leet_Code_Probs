class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans,n,m=[],len(candies),extraCandies
        val=max(candies)
        for i in range(n):
            if (candies[i]+m)>=val:
                ans.append(True)
            else:
                ans.append(False) 
        return ans