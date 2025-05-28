class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans=[[],[]] #[0,1]
        n1=list(set(nums1))
        n2=list(set(nums2))
        for i in range(len(n1)):
            if n1[i] not in n2:
                ans[0].append(n1[i])
        for j in range(len(n2)):
            if n2[j] not in n1:
                ans[1].append(n2[j])
        return ans