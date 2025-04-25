class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low,high=0,len(letters)-1
        while low<=high:
            m=(low+high)//2
            if target>=letters[-1] or target<letters[0]:
                return letters[0]
            elif letters[m]<=target:
                low=m+1
            else:
                high=m-1
        return letters[low]
                
