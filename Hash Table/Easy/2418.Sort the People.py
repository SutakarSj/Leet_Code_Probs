class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        about_heights = {} #Hash Table
        for x,y in zip(heights,names):
            about_heights[x] = y
        ans = []
        for i in reversed(sorted(heights)):
            ans.append(about_heights[i])
        return ans        