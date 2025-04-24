class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        num = n+m
        for i in range(m,num):
            nums1[i]=nums2[i-m]
        nums1.sort()
